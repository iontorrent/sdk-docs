.. _api-ug:

Torrent Suite™ Software API User Guide
======================================

The Torrent Suite™ Software API User Guide describes the technology behind API and how to leverage the technology using the REST interface. 

.. toctree::
    :maxdepth: 2

    manual_api_ug/apiug_intro_purpose.rst
    manual_api_ug/apiug_intro_arch.rst
    manual_api_ug/apiug_intro_tech.rst
    manual_api_ug/apiug_intro_refs.rst
    manual_api_ug/apiug_intro_start.rst

Topics in this list provide background and conceptual information on parameters, requests, responses, and endpoints:

.. toctree::
    :maxdepth: 2

    manual_api_ref_docs/manapiref_params.rst
    manual_api_ref_docs/manapiref_reqhdrs.rst
    manual_api_ref_docs/manapiref_httpresp.rst
    manual_api_ref_docs/manapiref_endpoints.rst

The following topics provide more detail about implementing and maintaining REST applications:

.. toctree::
    :maxdepth: 2

    manual_api_ug/apiug_impl.rst
    manual_api_ug/apiug_workdjango.rst
    manual_api_ug/apiug_debug.rst
    manual_api_ug/apiug_tools.rst


The API is built on the Django Framework, which implements a Model View Controller (MVC) architecture and supports the REST communication model. Using the Torrent Suite™ Software REST API, client applications operate on resources modelled in the back-end PostgreSQL database. Database, file, and system resources are addressable using a Universal Resource Identifier (URI), and can be created, read, modified, searched, and sorted using parameterized REST methods.

This document provides a semantic description of the API, which complements the API syntax presented in the :ref:`api-ref`.
