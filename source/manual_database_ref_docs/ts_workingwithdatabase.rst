Work with the Database
======================

Most REST operations involve reading data from the database or updating the database with data from your own applications. The following example applications use more advanced programming procedures than those already presented:
	
.. toctree::
    :maxdepth: 1

    ./ts_metadataandmetrics.rst
    ./ts_updatingexperimentnotes.rst
    ./ts_addingarig.rst
    ./ts_pgmstatus.rst

These examples show more complex and involved database query sequences than the basic operations used to introduce REST API programming. They get run metadata then use linked fields to navigate to analysis and quality metrics associated with a run.

Some examples demonstrate how to use the PUT and POST methods to update data resource fields and to create new resource elements.

Although simple resources are shown, having a limited number of fields, the procedures demonstrated in this section apply for any of the resources exposed by the REST API.
