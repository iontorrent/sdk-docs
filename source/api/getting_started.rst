.. _api_started:

Getting Started with the API
============================

API Overview
------------

Our API is RESTful and HTTP based. All resources use HTTP standard verbs return JSON data.

The main API endpoint for Torrent Suite is ``/rundb/api/v1/``. This endpoint returns a JSON object containing information
for each resource available from the API. To see each resource's list endpoint, go to ``/rundb/api/v1/resource-name/`` .
To see each resource's schema, go to ``/rundb/api/v1/resource-name/schema/``.

.. _api_authentication:

Authentication
--------------

To use the API you need to authenticate as an existing TS user. To see API keys for each TS user, go to ``/admin/tastypie/apikey/`` .
You must include an API key with every API request. There are two methods:

As a header. Format is ``Authorization: ApiKey <username>:<api_key>``
``Authorization: ApiKey daniel:204db7bcfafb2deb7506b89eb3b9b715b09905c8``

As GET params
``http://127.0.0.1:8000/api/v1/entries/?username=daniel&api_key=204db7bcfafb2deb7506b89eb3b9b715b09905c8``

Pagination
----------

The meta section of the list endpoint's response contains pagination details. Use the following GET params to
control pagination.

| ``limit`` The maximum number of resources the objects list will contain.
| ``next`` A URL pointing to the next page of results.
| ``offset`` The object number the current list of objects starts at.
| ``previous`` A URL pointing to the previous page of results.
| ``total_count`` The total number of objects remaining after filtering.
|

Modify ``limit`` and ``offset`` with URL parameters.

Sorting
-------

Use the ``order_by`` GET param to specify a field to sort returned objects. Add a ``-`` character in front of the field name
to switch the sort direction from ascending order (the default) to descending order. You can use most fields of an object to sort.

Filtering
---------

Perform basic filtering by using a GET param with the same name as an object field. Using ``name=alexander`` 
only returns objects with a name field of "alexander".

Use more advanced filters by appending the correct suffix to the GET param. The suffix consists of ``__`` plus one of the filters that follow.
Using ``name__startswith=alex`` only returns objects with a name field starting with "alex".

=========== ===========
Filter      Description
=========== ===========
exact       Exact match.
iexact      Case-insensitive exact match.
contains    Case-sensitive containment test.
icontains   Case-insensitive containment test.
in          In a given list. Comma delimited.
gt          Greater than.
gte         Greater than or equal to.
lt          Less than.
lte         Less than or equal to.
startswith  Case-sensitive starts-with.
istartswith Case-insensitive starts-with.
endswith    Case-sensitive ends-with.
iendswith   Case-insensitive ends-with.
range       Range test (inclusive).
year        Exact year match (date fields).
month       Exact month number match (date fields).
day         Exact day number match (date fields).
week_day    Exact week day number match. 1-7. Sunday=1 (date fields).
hour        Exact hour match. 0-23. (date fields).
minute      Exact minute match. 0-59. (date fields).
second      Exact second match. 0-59. (date fields).
isnull      Null check. True or False.
regex       Case-sensitive regular expression match.
iregex      Case-insensitive regular expression match.
=========== ===========

