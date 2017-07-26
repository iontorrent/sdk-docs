Running a Plugin
================

.. contents::

Execution Modes
---------------

Plugins have the following execution modes:

=========== =============
Mode        Description
=========== =============
Automatic	The plugin executes at the completion of every analysis pipeline processing run. Disabling auto-run in Torrent Browser changes the plugin setting to manual mode.
Manual      To manually run a plugin, navigate to the Torrent Browser Default Report page for the desired analysis. Select the plugin using the Plugin Summary panel. (See  Running the Installed Plugins.)
Disabled	( Default ) The plugin is registered but cannot be invoked either automatically or manually.
=========== =============

.. note:: To automatically set your plugin to manual mode, add the ``#AUTORUNDISABLE`` special comment to the launch.sh script.
    or the class attribute `autorun = False`` in the python wrapper script.
    Setting this variable, prevents the framework from including the plugin in the default set of plugins in the plan template.


Configuration
-------------

Plugins can have one of the following start-up behaviors:

Run without user input.
    Plugins without a user interface display a confirmation message that the plugin has been submitted to the scheduler.

Run with a user interface, for setting runtime parameters. (instance.html)
    Plugins requiring input parameters display the user interface you provided in the instance.html/php file, which is displayed when you click Submit. User interface plugins must be sure to include a line of JavaScript code that closes the iframe after the plugin is submitted to the scheduler.

Pugins can have the following configuration setting requirements:
* No configuration required.
* Require settings applicable for all instances of plugin execution.  (config.html, pluginsettings.json)
* Require settings applicable to individual instances of plugin execution (instance.html)

Configuration options depend on whether or not the following files exist in the plugin source directory:
Filename	Description
pluginconfig.json If the file exists, plugin instance configuration information is automatically registered in the database.
config.html If the file exists, displays a configuration iframe for entering global configuration settings, setting plugin values using the REST API. A link to this file is displayed in the Torrent Browser Config tab, if it exists.
instance.html If this user interface file exists, the file is loaded into an iframe and the plugin is launched manually. This file only applies to the current plugin instance.
The file implementation typically includes a form for specifying data to be passed to the plugin, and JavaScript code that submits the plugin to the SGE scheduler.
note.png	This file outputs a JSON structure, whose contents are converted to shell variables as described in the Plugin Framework section of this document.

See Example Plugin with User Interface for an example implementation of this type of plugin.
If this file is not present, the framework automatically makes a REST API call to run the plugin.
Default Configuration

The default configuration is settings that are applicable to all instances of the plugin running. One example of global configuration data is an ftp upload plugin where the ftp server, username and password settings and upload files are the same for all plugin instances.

Settings are stored in the Torrent Server database, and are passed to the launch.sh script and converted to bash shell variables.
 Instance Configuration

Instance configuration settings are applicable to only the current plugin instance.

Settings are defined in the pluginconfig.json JSON file, and are converted to shell variables and passed to the launch.sh script.
 Starting the Plugin Daemon

Before your plugin can run, you need to start the plugin daemon that submits your plugin job to the SGE scheduler.

Use the following procedure to start the daemon:
Login to Torrent Server, using ssh, and go to the executables directory where the daemon program is located:
ssh ionadmin@myhost

cd /opt/ion/iondb/bin
Start the daemon program:
python ionPluginDaemon.py
Selecting Plugins to Run

You select plugins to run from the Default Analysis report, following completion of analysis pipeline processing.

Refer to the Torrent Browser Analysis Report Guide,Select Plugins To Runsection,  for a description of the user interface for running plugins.
 Running a Plugin Using the API

To learn how to programmatically run a plugin using the REST API, refer to the Running a Plugin  example.
 Debugging Plugins

See theDebuggingsection of the Torrent Suite API User Guide for useful tips on debugging plugins.