Torrent SDK Getting Started with PostgreSQL (psql)
==================================================

The ``psql`` program is a command line client that accesses the PostgreSQL database both programmatically and interactively.

.. _refs:

References
----------

* `Practical PostgreSQL <http://www.commandprompt.com/ppbook/book1>`_
* `PostgreSQL 8.4.7 Documentation <http://www.postgresql.org/docs/8.4/static/index.html>`_ - `Chapter 19. Client Authentication 19.1 <http://www.postgresql.org/docs/8.4/static/client-authentication.html>`_ - `The pg_hba.conf file <http://www.postgresql.org/docs/8.4/static/auth-pg-hba-conf.html>`_. 
* On your PostgreSQL server, view the ``psql manpage`` with the following command: ``man psql``

.. _conndblocal:

Connect to the database locally
----------------------------------

If you are logged into the Torrent Server, you can interactively run ``psql`` and connect to the database using the following command::

	ionadmin@myserver:~$ psql -U ion -d iondb
	psql (8.4.7)
	Type "help" for help.
	
	iondb=>

After connecting, you can continue to interactively access the database using PostgreSQL queries. `iondb=>` is the command prompt.

.. _conndbremote:

Connect to the database remotely
-----------------------------------

To remotely connect to the database, you may need to do one or more of the following actions:

* Change security settings
* Install a PostgreSQL client
* Connect programmatically or using the ``psql`` command line client

.. _conndbverify:

Change remote access security settings
----------------------------------------

By default, the postgres database in the Torrent Server is configured to restrict remote access to the database according to the IP address of the local subnet. To change this security restriction, the PostgreSQL ``pg-hba.conf`` configuration file must be modified (see the :ref:`refs` section for links to PostgreSQL documentation).

Install the PostgreSQL client
-----------------------------

If you are on another Linux computer on the network, you can access the database remotely if a PostgreSQL client is installed. Install the client on Ubuntu using the following commands::

	sudo apt-get install postgresql-client-common
	sudo apt-get install postgresql-client-8.4

Connect to the database
-----------------------

When the client is installed, access the database using ``psql`` and provide your login username::

	thisuser@mydesktop:~$ psql -h myserver -d iondb -U ion
	psql (8.4.7)
	SSL connection (cipher: DHE-RSA-AES256-SHA, bits: 256)
	Type "help" for help.
	
	iondb=>

Verify your database connection
-------------------------------

Verify that you are connected to the Torrent Server database by checking the PostgreSQL version, using ``psql``::

	iondb=> select version();
	
	--------------------------
	
	PostgreSQL 8.4.7  ... elided ...

The installed PostgreSQL version is displayed with other information about the database.

After you verify that your system can access the database, you can run SQL queries on the database using ``psql`` or your programming language PostgreSQL API. Continue reading `Database Access Examples <./database_access_examples.html>`_ for specific methods for working with the Ion Torrent database.

