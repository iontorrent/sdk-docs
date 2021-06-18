.. _codes_get_fasta_fastq:


Downloading Files: FASTA and FASTQ
===================================

The example below is a CLI script to download FASTA and FASTQ files from
two plugins output with given report (Results) ID. One of plugin output
has a non-deterministic file output name.  


.. code-block:: bash

    ~$ python get_fasta_and_fastq.py -h
    usage: get_plugin_fasta_fastq_data.py [-h] [--host [HOST]]
                                        [--username [USERNAME]]
                                        [--password [PASSWORD]]
                                        [--resultPK [RESULTPK]]

    Get the FASTA and FASTQ from generateConsensus and FileExporter for all the
    barcodes for the requested Result id

    optional arguments:
    -h, --help            show this help message and exit
    --host [HOST]         target host to download files. (default: None)
    --username [USERNAME]
                            TB account username. (default: ionadmin)
    --password [PASSWORD]
                            TB account password. (default: ionadmin)
    --resultPK [RESULTPK]
                            the result primary key or ID. Case insensitive.




.. code-block:: python

    # Copyright (C) 2021 Thermo Fisher Scientific. All Rights Reserved.

    import os
    import sys
    import json
    import argparse
    import requests
    from bs4 import BeautifulSoup

    help_text = """
    Requirement:
        one of these options must be used: '--host', '--resultPK', .

    Logic:
    - Downloads all Sample Consensus Sequences FASTA from the Generate Consensus
    - Downloads  compressed Zip which contains all FASTQ from FileExporter
    - Make sure requests, bs4(BeautifulSoup4) modules are installed via pip
    """


    class GetPluginResults:
        api_name = "results"
        deleted_count = 0
        ignored_names = []

        def __init__(self, inputArgs):
            self.host = inputArgs["host"]
            self.auth = (inputArgs["username"], inputArgs["password"])
            self.resultPK = inputArgs["resultPK"]

        def get_objects(self, url):
            try:
                out = requests.get(url, auth=self.auth)
                if out.ok:
                    return out.json()
                else:
                    print(
                        ">>>> (Status Code: %d) Unable to retrieve %s"
                        % (out.status_code, out.url)
                    )
            except requests.ConnectionError:
                print(">>>> Unable to connect %s" % (url))

        def getFastaFastq(self):
            if self.resultPK:
                url = os.path.join(self.host, "rundb/api/v1", self.api_name, self.resultPK)

            for obj in self.get_objects(url).get("pluginresults"):
                pluginUrl = str(self.host + obj)
                pluginOut = self.get_objects(pluginUrl)
                if pluginOut.get("pluginName") == "generateConsensus":
                    self.download_fasta(pluginOut)
                if pluginOut.get("pluginName") == "FileExporter":
                    self.download_fastq(pluginOut)

        def getStartPluginJson(self, pluginOut):
            startPluginUrl = self.host + pluginOut.get("URL") + "startplugin.json"
            req = requests.get(startPluginUrl, auth=self.auth)
            return req.json()

        def download_fasta(self, pluginOut):
            print("Starting FASTA download...")
            startPluginUrl = self.host + pluginOut.get("URL") + "startplugin.json"
            req = requests.get(startPluginUrl, auth=self.auth)
            data = req.json()
            allConsenusFastaIn = (
                data.get("expmeta").get("output_file_name_stem") + ".consensus.fasta"
            )
            allConsenusFastaOut = (
                data.get("expmeta").get("output_file_name_stem")
                + "_"
                + str(pluginOut.get("id"))
                + ".consensus.fasta"
            )
            try:
                file_url = self.host + pluginOut.get("URL") + allConsenusFastaIn
                req = requests.get(file_url, auth=self.auth)
                with open(allConsenusFastaOut, "wb") as f:
                    f.write(req.content)
                print(allConsenusFastaIn)
            except Exception as Err:
                print("FASTQ download failed. Please check %s" % Err)
            print("Completed FASTA download")

        def download_fastq(self, pluginOut):
            print("Starting the FASTQ download...")
            resultDirPath = (
                self.getStartPluginJson(pluginOut)
                .get("runinfo")
                .get("results_dir")
                .split("/")
            )
            metal_url = os.path.join(
                self.host,
                "report",
                str(self.resultPK),
                "metal",
                resultDirPath[-2],
                resultDirPath[-1],
            )

            req = requests.get(metal_url, auth=self.auth)
            soup = BeautifulSoup(req.content, features="html.parser")
            rows = soup.find("table").find_all("tr")
            fastq_zip = None
            for row in rows:
                try:
                    fileName = row.find("a").get_text()
                    if "zip" in fileName:
                        fastq_zip = fileName
                        exit()
                except Exception:
                    continue

            if fastq_zip:
                zipUrlIn = self.host + pluginOut.get("URL") + fastq_zip
                zipUrlOut = str(pluginOut.get("id")) + "_" + fastq_zip
                response = requests.get(
                    zipUrlIn, stream=True, auth=("ionadmin", "ionadmin")
                )
                with open(zipUrlOut, "wb") as zip:
                    for chunk in response.iter_content(chunk_size=512):
                        if chunk:  # filter out keep-alive new chunks
                            zip.write(chunk)
                print(fastq_zip)
            else:
                print("FASTQ download did not complete")
                exit()
            print("Completed FASTA download")


    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            prog="get_plugin_fasta_fastq_data.py",
            description="Get the FASTA and FASTQ from generateConsensus and FileExporter "
            "for all the barcodes for the requested "
            "Result id",
        )

        parser.add_argument(
            "--host",
            nargs="?",
            help="target host to download files. (default: %(default)s)",
        )

        parser.add_argument(
            "--username",
            nargs="?",
            default="ionadmin",
            help="TB account username. (default: %(default)s)",
        )

        parser.add_argument(
            "--password",
            nargs="?",
            default="ionadmin",
            help="TB account password. (default: %(default)s)",
        )

        parser.add_argument(
            "--resultPK",
            nargs="?",
            help="the result primary key or ID. " + "Case insensitive.",
        )

        args = vars(parser.parse_args())

        if args.get("host") and args.get("resultPK"):
            if "http" not in args.get("host"):
                print("need to specifiy HTTP or HTTPS")
                sys.exit(1)

            pluginResultData = GetPluginResults(args)
            pluginResultData.getFastaFastq()

        else:
            print("Error: one of the required options is not used")
            print(help_text)
            parser.parse_args(["-h"])
            sys.exit(1)
