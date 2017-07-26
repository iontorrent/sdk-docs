.. _api_examples:

API Examples
============

See :ref:`api_reference` for a listing of all available APIs. This section has the setup common to all the API examples.
See :ref:`api_authentication` for more information on the authentication header. All examples use the third-party python
library `requests <http://docs.python-requests.org/>`_.

.. code-block:: python

    import requests

    BASE_URL = "http://example.xyz"
    USERNAME = "ionadmin"
    API_KEY = "efb7a14021732d773a4258b69d9452042a31a6b6"

.. testsetup:: *

    import requests

    BASE_URL = "http://ts-docs.titan.itw"
    USERNAME = "ionadmin"
    API_KEY = "9b9d9723b21e4dc06b88c979d2aa0e2062d59bc3"

Fetching all Chips
------------------

Using the :ref:`api_reference_chip` API.

.. testcode::

    headers = {"Authorization": "ApiKey " + USERNAME + ":" + API_KEY}
    object_list = []

    next_url = "/rundb/api/v1/chip/"
    while next_url:
        response = requests.get(BASE_URL + next_url, headers=headers, params={})
        response.raise_for_status()
        response_data = response.json()

        object_list += response_data["objects"]
        next_url = response_data["meta"]["next"] or None

    print object_list

.. testoutput::

    [...]



Adding Filters
--------------

Using the :ref:`api_reference_chip` API.

.. testcode::

    headers = {"Authorization": "ApiKey " + USERNAME + ":" + API_KEY}
    object_list = []

    next_url = "/rundb/api/v1/chip/"
    while next_url:
        response = requests.get(BASE_URL + next_url, headers=headers, params={"name__startswith": "31"})
        response.raise_for_status()
        response_data = response.json()

        object_list += response_data["objects"]
        next_url = response_data["meta"]["next"] or None

    for chip in object_list[0:3]:
        print chip["name"]

.. testoutput::

    314
    316
    318

Completed Runs and Reports
--------------------------

Using the :ref:`api_reference_compositeexperiment` API.

.. testcode::

    headers = {"Authorization": "ApiKey " + USERNAME + ":" + API_KEY}
    object_list = []

    next_url = "/rundb/api/v1/compositeexperiment/"
    while next_url:
        response = requests.get(BASE_URL + next_url, headers=headers)
        response.raise_for_status()
        response_data = response.json()

        object_list += response_data["objects"]
        next_url = response_data["meta"]["next"] or None

    for experiment in object_list[0:3]:
        print experiment["displayName"]
        for report in experiment["results"]:
            print "    " + report["resultsName"] + " " + report["status"]

.. testoutput::

    S5-530 cfDNA
        Reanalyze Completed
        S5-530_cfDNA Completed
        Auto_S5-530_cfDNA_89 Completed
    S5-540 AmpliSeqExome
        S5-540_AmpliSeqExome Importing Failed
        Auto_S5-540_AmpliSeqExome_90 Completed
    S5-540 WholeTranscriptomeRNA
        Auto_S5-540_WholeTranscriptomeRNA_91 Importing Failed


Fetching a Report
-----------------

Using the :ref:`api_reference_results` API.

.. testcode::

    headers = {"Authorization": "ApiKey " + USERNAME + ":" + API_KEY}

    report_response = requests.get(BASE_URL + "/rundb/api/v1/results/3/", headers=headers)
    report_response.raise_for_status()
    report_response_data = report_response.json()

    print report_response_data["resultsName"]

    for plugin_name, plugin_status in report_response_data["pluginState"].items():
        print "    " + plugin_name, plugin_status

    lib_metrics_response = requests.get(BASE_URL + report_response_data["libmetrics"][0], headers=headers)
    lib_metrics_response.raise_for_status()
    lib_metrics_response_data = lib_metrics_response.json()

    print "%.1f million reads" % (lib_metrics_response_data["totalNumReads"]/1000000.0)

.. testoutput::

    Auto_S5-540_WholeTranscriptomeRNA_91
        DataExport Completed
        ERCC_Analysis Completed
        sampleID Error
        coverageAnalysis Error
        AssemblerSPAdes Started
        FilterDuplicates Completed
        RunTransfer Completed
    94.0 million reads


Planning a Non-barcoded Run
---------------------------

Using the :ref:`api_reference_plannedexperiment` API.

.. testcode::

    headers = {"Authorization": "ApiKey " + USERNAME + ":" + API_KEY}
    plan_json = {
        "library": "hg19",
        "planName": "DOCS_my_plan",
        "sample": "my_sample",
        "chipType": "520",
        "sequencekitname": "Ion S5 Sequencing Kit",
        "librarykitname": "Ion Xpress Plus Fragment Library Kit",
        "templatingKitName": "Ion 520/530 Kit-OT2"
    }
    response = requests.post(BASE_URL + "/rundb/api/v1/plannedexperiment/", headers=headers, json=plan_json)
    response.raise_for_status()
    print response.status_code

.. testoutput::

    201

Planning a Barcoded Run
-----------------------

Using the :ref:`api_reference_plannedexperiment` API.

.. testcode::

    headers = {"Authorization": "ApiKey " + USERNAME + ":" + API_KEY}
    plan_json = {
        "library": "hg19",
        "planName": "DOCS_my_plan",
        "sample": "my_sample",
        "chipType": "520",
        "sequencekitname": "Ion S5 Sequencing Kit",
        "librarykitname": "Ion Xpress Plus Fragment Library Kit",
        "templatingKitName": "Ion 520/530 Kit-OT2",
        "barcodeId": "IonXpress",
        "barcodedSamples": {
            'demo sample 1': {
                'barcodeSampleInfo': {
                    'IonXpress_003': {
                        'description': 'description here',
                        'hotSpotRegionBedFile': '',
                        'nucleotideType': 'DNA',
                        'reference': 'hg19',
                        'targetRegionBedFile': ''
                    }
                },
                'barcodes': ['IonXpress_003']
            },
            'demo sample 2': {
                'barcodeSampleInfo': {
                    'IonXpress_004': {
                        'description': 'description here',
                        'hotSpotRegionBedFile': '',
                        'nucleotideType': 'DNA',
                        'reference': 'hg19',
                        'targetRegionBedFile': ''
                    }
                },
                'barcodes': ['IonXpress_004']
            }
        }
    }
    response = requests.post(BASE_URL + "/rundb/api/v1/plannedexperiment/", headers=headers, json=plan_json)
    response.raise_for_status()
    print response.status_code

.. testoutput::

    201