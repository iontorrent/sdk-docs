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

The API specifies endpoints with callable methods for each resource and managed entity, such as a plugin or file. To perform an action using the API, you send a request to the endpoint, using a REST method and specifying parameters, data and the format. The parameters, requests, responses, and error codes for each method are listed in the API reference tables.

See the API reference tables for a listing of all API resources:

.. toctree::
    :maxdepth: 1

    auto_api_ref_index.rst
    manual_api_cookbook/about_examples.rst
    manual_api_cookbook/before_reading.rst
    manual_api_cookbook/connect_with_server.rst
    manual_api_cookbook/first_request.rst

	
Other SDK documents and guides
------------------------------

.. toctree::
    :maxdepth: 1

    manual_api_ug.rst
    manual_api_FAQ.rst
    manual_api_acro.rst	

Torrent Suite Plugin Development
--------------------------------

.. toctree::
    :maxdepth: 1

    auto_plugin_reference.rst
    manual_plugin_sdk_index.rst
    manual_plugin_sdk_docs/getting_started_with_plugins.rst
    manual_plugin_sdk_docs/plugin_developer_guide.rst
    manual_plugin_sdk_docs/plugin_environment.rst
    manual_plugin_sdk_docs/plugin_authentication.rst
    manual_plugin_sdk_docs/plugins_running.rst

`Example: Fastq creator plugin <manual_plugin_sdk_docs/ex_fastqcreator.html>`_

`Example: Proton runlevel demonstration <manual_plugin_sdk_docs/ex_protonautorun.html>`_

`Example: Convert shell plugin to python plugin <manual_plugin_sdk_docs/ex_convertplugins.html>`_

About these documents
---------------------

See this page for descriptions of the left panel table of contents, the breadcrumbs at the top of each page, and the previous and next navigation links:

.. toctree::
    :maxdepth: 2

    about_these_docs.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


