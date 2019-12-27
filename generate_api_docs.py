#!/usr/bin/env python
import requests
import json
import os

try:
    from urllib import parse as urlparse
except ImportError:
    import urlparse


from settings import TS_URL, TS_USERNAME, TS_PASSWORD


# modified from http://stackoverflow.com/a/12539081/56069
def make_table(grid):
    max_cols = [
        max(out)
        for out in map(list, zip(*[[len(item) for item in row] for row in grid]))
    ]
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


def lower_case_to_title_case(string):
    """
    This function takes text like 'bigredtruck' and turns it into 'big red truck' by magic.
    """
    string = string.replace("_", "").lower()
    dictionary = sorted(
        [
            "active",
            "adapter",
            "analysis",
            "analysis",
            "annotation",
            "appl",
            "application",
            "args",
            "attribute",
            "available",
            "basic",
            "chef",
            "cluster",
            "common",
            "composite",
            "content",
            "cv",
            "data",
            "db",
            "dna",
            "email",
            "event",
            "experiment",
            "file",
            "flow",
            "genome",
            "global",
            "group",
            "history",
            "info",
            "ion",
            "item",
            "job",
            "kit",
            "lib",
            "library",
            "location",
            "log",
            "management",
            "metrics",
            "mesh",
            "monitor",
            "node",
            "onetouch",
            "pgm",
            "plan",
            "planned",
            "plugin",
            "prep",
            "prime",
            "product",
            "project",
            "proton",
            "qc",
            "quality",
            "reference",
            "result",
            "results",
            "run",
            "sample",
            "sequencing",
            "server",
            "set",
            "settings",
            "suite",
            "summary",
            "support",
            "support",
            "template",
            "tf",
            "three",
            "torrent",
            "type",
            "upload",
            "get",
            "script",
            "info",
        ],
        key=len,
        reverse=True,
    )
    found_words = []
    for _ in range(0, 10):
        for word in dictionary:
            if string.startswith(word):
                found_words.append(word)
                string = string[len(word) :]
                break
    found_words.append(string)
    return " ".join(found_words)


# Auth
auth = (TS_USERNAME, TS_PASSWORD)

# API Docs Settings

API_BASE_URL = urlparse.urljoin(TS_URL, "/rundb/api/v1/")

API_DOCS_OUTPUT_PATH = os.path.join("source", "api", "references_auto_generated")
MANUAL_API_DOCS_OUTPUT_PATH = os.path.join("source", "api", "references_manual_extras")
EXCLUDE_RESOURCES = [
    "ionreporter",  # 500
    "account",  # 401
    "prepopulatedplanningsession",  # 500
    "obsoletereferencegenome",  # Obsolete
    "getsoftwareinfo",
]
API_VERSION = "v1"
DEMO_API_BASE_URL = "http://mytorrentserver/rundb/api/v1/"
DEMO_URL_ARGS = "?format=json&limit=1"

# Functions

# API Auto-gen Documentation

# Get API schema for all objects
main_schema_request = requests.get(API_BASE_URL, params={"format": "json"}, auth=auth)
main_schema_request.raise_for_status()

# Track locations of API docs for listing page
resource_doc_paths = []

# Write out docs pages for each API resource
for resource_name, resource_values in list(main_schema_request.json().items()):
    if resource_name not in EXCLUDE_RESOURCES:

        # Get schema for the current resource
        print("Using TS API to fetch %s schema..." % resource_name)
        single_resource_schema_request = requests.get(
            urlparse.urljoin(API_BASE_URL, resource_values["schema"]),
            params={"format": "json"},
            auth=auth,
        )
        print(single_resource_schema_request.url)
        single_resource_schema_request.raise_for_status()

        # Make a request to get an example response
        single_resource_demo_request = requests.get(
            urlparse.urljoin(API_BASE_URL, resource_values["list_endpoint"])
            + DEMO_URL_ARGS,
            auth=auth,
        )
        single_resource_demo_request.raise_for_status()

        # We get warnings if the manual files do not exist. Try to create them now if they do not exist
        manual_resource_doc_path = os.path.join(
            MANUAL_API_DOCS_OUTPUT_PATH, resource_name.lower() + ".rst"
        )
        if not os.path.exists(manual_resource_doc_path):
            print(
                "Missing manual rst file for %s resource. Creating one now."
                % resource_name
            )
            with open(manual_resource_doc_path, "w+") as output_file:
                output_file.write("")

        # Generate an rst for the resource
        resource_doc_path = os.path.join(
            API_DOCS_OUTPUT_PATH, resource_name.lower() + ".rst"
        )

        with open(resource_doc_path, "w+") as output_file:
            json_formatted_demo = json.dumps(
                single_resource_demo_request.json(), indent=4
            )
            json_formatted_demo = "\n".join(
                ["\t" + json_line for json_line in json_formatted_demo.split("\n")]
            )

            json_formatted_schema = json.dumps(
                single_resource_schema_request.json()["fields"], indent=4
            )
            json_formatted_schema = "\n".join(
                ["\t" + json_line for json_line in json_formatted_schema.split("\n")]
            )

            allowed_detail_http_methods = single_resource_schema_request.json()[
                "allowed_detail_http_methods"
            ]
            allowed_list_http_methods = single_resource_schema_request.json()[
                "allowed_list_http_methods"
            ]

            title = lower_case_to_title_case(resource_name).title() + " Resource\n"

            output_file.write(".. _api_reference_%s:\n\n" % resource_name.lower())
            output_file.write(title)
            output_file.write("=" * (len(title) - 1) + "\n\n")
            output_file.write(
                "| Resource URL ``%s``\n"
                % urlparse.urljoin(DEMO_API_BASE_URL, resource_values["list_endpoint"])
            )
            output_file.write(
                "| Schema URL ``%s``\n"
                % urlparse.urljoin(DEMO_API_BASE_URL, resource_values["schema"])
            )
            output_file.write("| ")

            # Write out manual docs portion
            output_file.write(
                "\n\n"
                + ".. include:: ../references_manual_extras/"
                + resource_name.lower()
                + ".rst"
                + "\n\n"
            )

            # Write out resource schema
            cols = [
                "help_text",
                "default",
                "nullable",
                "readonly",
                "blank",
                "unique",
                "type",
            ]
            header_cols = [
                "help text",
                "default                                                        ",
                "nullable",
                "readonly",
                "blank",
                "unique",
                "type",
            ]
            header_cols = [
                "help text",
                "default",
                "nullable",
                "readonly",
                "blank",
                "unique",
                "type",
            ]
            output_file.write("Resource Fields\n")
            output_file.write("---------------" + "\n\n")
            toprow = ["field"]
            toprow.extend(header_cols)
            table = [toprow]
            for field, values in single_resource_schema_request.json()[
                "fields"
            ].items():
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

            output_file.write("Example Response\n")
            output_file.write("^^^^^^^^^^^^^^^^" + "\n\n")
            output_file.write(".. code-block:: javascript\n\n")
            output_file.write(json_formatted_demo + "\n")

            # Write out http methods
            output_file.write("\nAllowed list HTTP methods\n")
            output_file.write("-------------------------" + "\n\n")
            if not allowed_list_http_methods:
                output_file.write("None\n")
            else:
                for allowed_http_method in allowed_list_http_methods:
                    output_file.write("- " + allowed_http_method.upper() + "\n")
            output_file.write("\n")

            output_file.write("\nAllowed detail HTTP methods\n")
            output_file.write("---------------------------" + "\n\n")
            if not allowed_detail_http_methods:
                output_file.write("None\n")
            else:
                for allowed_http_method in allowed_detail_http_methods:
                    output_file.write("- " + allowed_http_method.upper() + "\n")
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

        resource_doc_paths.append(
            os.path.relpath(resource_doc_path, "source").replace("\\", "/")
        )
