.. Torrent SDK documentation master file, created by
   sphinx-quickstart on Fri Jun  7 16:17:38 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Ion Torrent™ SDK documentation
=======================================

The Torrent Suite™ Software Development Kit (SDK) provides a convenient and powerful web services Application Programming Interface (API) for accessing the Torrent Server database and working with analysis results files and plugins. The API implements a well-defined interface based on Representational State Transfer (REST) principles for remote access to resources with programming language independence.

Examples
--------------------------------------

Below are some Python examples to get you started with the Torrent SDK.

.. toctree::
    :maxdepth: 2

    manual_code_examples_index.rst

REST API
--------------------------------------

The API specifies endpoints with callable methods for each resource and managed entity, such as a plugin or file. To perform an action using the API, you send a request to the endpoint, using a REST method and specifying parameters, data and the data format. The parameters, requests, responses, and error codes for each method are listed in the API reference tables.

See the API reference tables for a listing of all API resources:

.. toctree::
    :maxdepth: 1

    auto_api_ref_index.rst

See the API Cookbook for a tutorial on how to programatically access the API:

.. toctree::
    :maxdepth: 1

    manual_database_ref_docs/ts_cookbook.rst
	
The API Quick Reference provides a summary listing of select APIs:

.. toctree::
    :maxdepth: 1

    manual_database_ref_docs/ts_apiquickreference.rst

Database
--------------------------------------

Analysis, report and configuration data are stored in a PostgreSQL database. Database items include:

* Values computed during analysis pipeline processing.
* Configuration parameters accessible using the Torrent Browser UI.

See the schema tables for a listing of all Torrent Suite™ Software database tables:

.. toctree::
    :maxdepth: 1

    auto_database_ref_index.rst

PostgreSQL is an open-source object-relational Database Management System (DBMS) that supports almost all SQL constructs. PostgreSQL APIs are available for the most popular programming languages to build applications using the database for backend data store. The main user interface to PostgreSQL is the ``psql`` command line program. The ``psql`` program permits you to enter database queries directly from a terminal or to execute a query sequence from a file. Database queries demonstrated in this guide use ``psql``.

API and schema tables
---------------------

.. toctree::
    :maxdepth: 1

    auto_api_ref_index.rst
    auto_database_ref_index.rst
	
Other SDK documents and guides
------------------------------

.. toctree::
    :maxdepth: 1

    manual_database_ug_index.rst
    manual_database_ref_docs/ts_cookbook.rst
    manual_api_ug.rst
    manual_api_FAQ.rst
    manual_api_acro.rst	

Plugins:

`Example: Fastq creator plugin (3.x) <manual_database_ref_docs/ex_fastqcreator.html>`_

`Example: Proton runlevel demonstration (3.x) <manual_database_ref_docs/ex_protonautorun.html>`_

`Example: Convert 2.x plugin to 3.x plugin <manual_database_ref_docs/ex_convertplugins.html>`_

	
About these documents
---------------------

See this page for descriptions of the left panel table of contents, the breadcrumbs at the top of each page, and the previous and next navigation links:

.. toctree::
    :maxdepth: 2

    about_these_docs.rst


