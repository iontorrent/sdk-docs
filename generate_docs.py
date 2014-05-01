#!/usr/bin/env python
import subprocess
import requests
import urlparse
import json
import os

from lib.model_doc_scraper import ModelDocScraper

from settings import TS_URL, TS_USERNAME, TS_PASSWORD


#modified from http://stackoverflow.com/a/12539081/56069
def make_table(grid):
    max_cols = [max(out) for out in map(list, zip(*[[len(item) for item in row] for row in grid]))]
    rst = table_div(max_cols, 1)

    for i, row in enumerate(grid):
        header_flag = False
        if i == 0 or i == len(grid) - 1:
            header_flag = True
        rst += normalize_row(row, max_cols)
        rst += table_div(max_cols, header_flag)
    return rst


def table_div(max_cols, header_flag=1):
    out = ""
    if header_flag == 1:
        style = "="
    else:
        style = "-"

    for max_col in max_cols:
        out += max_col * style + " "

    out += "\n"
    return out


def normalize_row(row, max_cols):
    r = ""
    for i, max_col in enumerate(max_cols):
        r += row[i] + (max_col - len(row[i]) + 1) * " "
    return r + "\n"

###Auth
auth = (TS_USERNAME, TS_PASSWORD)


##API Docs Settings

API_BASE_URL = urlparse.urljoin(TS_URL, "/rundb/api/v1/")

API_DOCS_OUTPUT_PATH = os.path.join("source", "auto_api_ref_docs")
EXCLUDE_RESOURCES = [
    "publisher",  #404
    "account",  #401
    "ionreporter",  #400
    "network",  #500
    "torrentsuite",  #500
]
API_VERSION = "v1"
DEMO_API_BASE_URL = "http://mytorrentserver/rundb/api/v1/"
DEMO_URL_ARGS = "?format=json&limit=1"

#Python examples
PYTHON_READ_EXAMPLE = """
import requests

ts_api_request = requests.get("{request_url}", params={{"format": "json", "limit": 1}})
ts_api_response = ts_api_request.json()

{resource_name}s = ts_api_response["objects"]

for {resource_name} in {resource_name}s:
    print {resource_name}
"""

##Database Docs Settings

DATABASE_DOCS_BASE_URL = urlparse.urljoin(TS_URL, "/admin/doc/models/")
DATABASE_DOCS_OUTPUT_PATH = "source/auto_database_ref_docs/"
DATABASE_NAME = "iondb"

##Functions

#https://code.google.com/p/pandoc/downloads/list
def html2rst(html):
    p = subprocess.Popen(['pandoc', '--from=html', '--to=rst'],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return p.communicate(html)[0]

##API Auto-gen Documentation

#Get API schema for all objects
main_schema_request = requests.get(API_BASE_URL, params={"format": "json"}, auth=auth)
main_schema_request.raise_for_status()

#Track locations of API docs for listing page
resource_doc_paths = []

#Write out docs pages for each API resource
for resource_name, resource_values in main_schema_request.json().items():
    if resource_name not in EXCLUDE_RESOURCES:

        #Get schema for the current resource
        print "Using TS API to fetch %s schema..." % resource_name
        single_resource_schema_request = requests.get(
            urlparse.urljoin(API_BASE_URL, resource_values["schema"]),
            params={"format": "json"}, auth=auth)
        print single_resource_schema_request.url
        single_resource_schema_request.raise_for_status()

        #Make a request to get an example response
        single_resource_demo_request = requests.get(
            urlparse.urljoin(API_BASE_URL, resource_values["list_endpoint"]) + DEMO_URL_ARGS, auth=auth)
        single_resource_demo_request.raise_for_status()

        #Make a python demo
        python_demo = PYTHON_READ_EXAMPLE.format(
            request_url=urlparse.urljoin(DEMO_API_BASE_URL, resource_values["list_endpoint"]),
            resource_name=resource_name)
        python_demo = "\n".join(["\t" + python_line for python_line in python_demo.split("\n")])

        #Generate an rst for the resource
        resource_doc_path = os.path.join(API_DOCS_OUTPUT_PATH, resource_name + ".rst")

        with open(resource_doc_path, "w+") as output_file:
            json_formatted_demo = json.dumps(single_resource_demo_request.json(), indent=4)
            json_formatted_demo = "\n".join(["\t" + json_line for json_line in json_formatted_demo.split("\n")])

            json_formatted_schema = json.dumps(single_resource_schema_request.json()["fields"], indent=4)
            json_formatted_schema = "\n".join(["\t" + json_line for json_line in json_formatted_schema.split("\n")])

            allowed_http_methods = single_resource_schema_request.json()["allowed_detail_http_methods"]

            output_file.write(resource_name.title() + " Resource\n")
            output_file.write("==========================================================================" + "\n\n")
            output_file.write(
                "Resource URL: ``%s``\n\n\n" % urlparse.urljoin(DEMO_API_BASE_URL, resource_values["list_endpoint"]))
            output_file.write("Schema URL: ``%s``\n" % urlparse.urljoin(DEMO_API_BASE_URL, resource_values["schema"]))

            #Write out manual docs portion
            output_file.write("\n\n" + ".. include:: ../manual_api_ref_docs/" + resource_name + ".rst" + "\n\n")

            #Write out resource schema
            cols = ["help_text", "default", "nullable", "readonly", "blank", "unique", "type"]
            header_cols = ["help text", "default                                                        ", "nullable",
                "readonly", "blank", "unique", "type"]
            header_cols = ["help text", "default", "nullable", "readonly", "blank", "unique", "type"]
            output_file.write("Fields table\n")
            output_file.write("------------" + "\n\n")
            toprow = ["field"]
            toprow.extend(header_cols)
            table = []
            table.append(toprow)
            for field, values in single_resource_schema_request.json()["fields"].iteritems():
                row = ["**" + field + "**"]
                for col in cols:
                    if col == "default" and values[col] == "No default provided.":
                        values[col] = "n/a"
                    if col == "default" and values[col] == "No default provided.":
                        values[col] = "n/a"
                    if str(values[col]) == "False":
                        values[col] = "false"
                    if str(values[col]) == "True":
                        values[col] = "true"
                    row.append(str(values[col]))
                table.append(row)
            output_file.write(make_table(table))
            output_file.write("\n")

            #Write out resource request demo
            output_file.write("Example request\n")
            output_file.write("---------------" + "\n\n")
            output_file.write("Request URL: ``%s``\n\n\n" % (
                urlparse.urljoin(DEMO_API_BASE_URL, resource_values["list_endpoint"]) + DEMO_URL_ARGS))

            output_file.write("Python example\n")
            output_file.write("^^^^^^^^^^^^^^" + "\n\n")
            output_file.write(".. code-block:: python\n\n")
            output_file.write(python_demo + "\n")

            output_file.write("Torrent Server response\n")
            output_file.write("^^^^^^^^^^^^^^^^^^^^^^^" + "\n\n")
            output_file.write(".. code-block:: javascript\n\n")
            output_file.write(json_formatted_demo + "\n")

            #old schema
            """
            output_file.write("Available Fields\n")
            output_file.write("-------"+"\n\n")
            output_file.write(".. code-block:: javascript\n\n")
            output_file.write(json_formatted_schema+"\n")
            """

            #Write out http methods
            output_file.write("\nAllowed HTTP methods\n")
            output_file.write("--------------------" + "\n\n")
            for allowed_http_method in allowed_http_methods:
                output_file.write("- " + allowed_http_method + "\n")
            output_file.write("\n")

            """
            Filtering
            --------
                Enable all basic ORM filters but do not allow filtering across relationships.
                ALL = 1
                # Enable all ORM filters, including across relationships
                ALL_WITH_RELATIONS = 2

            "default_format": "application/json",
            "default_limit": 20,
            "filtering": {},
            "ordering": []
            """

        resource_doc_paths.append(os.path.relpath(resource_doc_path, "source").replace("\\", "/"))

#Wrtie out the API resource listing page
resource_doc_paths.sort()
with open("source/auto_api_ref_index.rst", "w+") as api_ref_listing_file:
    api_ref_listing_file.write(".. _api-ref:\n\n")
    api_ref_listing_file.write("Torrent Server REST API %s Resources\n" % API_VERSION)
    api_ref_listing_file.write("===========================================================================\n\n")
    api_ref_listing_file.write(".. toctree::\n")
    api_ref_listing_file.write("\t:maxdepth: 1\n\n")

    for resource_doc_path in resource_doc_paths:
        api_ref_listing_file.write("\t" + resource_doc_path + "\n")

##Database Auto-gen Documentation

database_doc_scraper = ModelDocScraper(DATABASE_DOCS_BASE_URL, auth)

#Track locations of API docs for listing page
database_doc_paths = []

for model_doc in database_doc_scraper.get_model_docs_html():

    table_name = model_doc["pg_table_name"]

    print "Using Django admin docs to fetch %s schema..." % table_name

    #Convert the django admin html table to and rst table
    model_doc_html = model_doc["model_docs_html"]
    model_doc_rst = html2rst(model_doc_html).replace("\r\n", "\n")

    #Generate an rst for the resource
    table_doc_path = os.path.join(DATABASE_DOCS_OUTPUT_PATH, table_name + ".rst")

    with open(table_doc_path, "w+") as output_file:
        output_file.write("Database Table " + table_name + "\n")
        output_file.write("============================================================================" + "\n\n")
        output_file.write("Postgres database: ``%s``\n\n\n" % DATABASE_NAME)
        output_file.write("Postgres table: ``%s``\n" % table_name)

        #Write out manual docs portion
        output_file.write("\n\n" + ".. include:: ../manual_database_ref_docs/" + table_name + ".rst" + "\n\n")

        #Write out table schema
        output_file.write("Schema\n")
        output_file.write("-------" + "\n\n")
        output_file.write(model_doc_rst)

    database_doc_paths.append(os.path.relpath(table_doc_path, "source").replace("\\", "/"))

#Wrtie out the database table listing page
database_doc_paths.sort()
with open("source/auto_database_ref_index.rst", "w+") as database_ref_listing_file:
    database_ref_listing_file.write(".. _database-ref:\n\n")
    database_ref_listing_file.write("Torrent Server Database Tables\n")
    database_ref_listing_file.write("==============================\n\n")
    database_ref_listing_file.write(".. toctree::\n")
    database_ref_listing_file.write("\t:maxdepth: 3\n\n")

    for table_doc_path in database_doc_paths:
        database_ref_listing_file.write("\t" + table_doc_path + "\n")

#Call the sphinx make script
if os.name == 'nt':
    #Windows
    os.system("make.bat html")
else:
    os.system("make html")
