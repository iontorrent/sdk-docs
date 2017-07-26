Torrent Suite Plugins Developer Guide
=====================================

.. contents::

Plugin Procedures Checklist
---------------------------

Creating and running plugins required developers to follow certain conventions defined by the plugin framework.

* Write your plugin code.

* Install the plugin in the /results/plugin/<yourPlugin> directory.

If the plugin requires runtime variables and parameters provided through a user interface,

* Write the config.html code for setting global variables.

* Write the instance.html code for setting instance parameters.

* Write the pluginconfig.json code for setting instance variables.

If the plugin has customized output, write code to generate html files,

* Write the <pluginName>_block.html code for displaying plugin output in the Default Analysis report Plugin Summary panel.

* Write <pluginName>.html or pluginName>.php code for Web page to display your results. A link to your page is created in the Plugin Summary panel.

After analysis pipeline processing completes,

* Plugins selected during run planning are run automatically.

* Go to the Analysis Report Plugin section to run manual mode plugins.

Structure and Content of Shell ("launch.sh") Torrent Suite Plugins
------------------------------------------------------------------

In your plugin folder, these file names and types have special purpose.

* launch.sh - Main run Script
  * VERSION
  * AUTORUNDISABLE
  * source /results/plugin_functions
* pluginsettings.json  - Initial/default values for plugin global settings, read at plugin install time.
* config.html - HTML page for user editable plugin global settings.
* pluginconfig.json - Plugin Control Parameters: runmode, runtype, features. Informs pipeline where and how plugin should run.
* instance.html - User input to set run specific settings for the plugin. Shown on report page when user selects plugin to be run manually.

Structure and Content of Python Torrent Suite Plugins
-----------------------------------------------------

In your plugin folder, these file names and types have special purpose.

* <PluginName>.py
  * ``class <PluginName>(IonPlugin)``
  * All plugin runtime, runtype, feature settings are set as class attributes.
* pluginsettings.json  - Initial/default values for plugin global settings, read at plugin install time.
* config.html - HTML page for user editable plugin global settings.
* instance.html - User input to set run specific settings for the plugin. Shown on report page when user selects plugin to be run manually.

Plugin SDK Python
=================

A python extending the base class IonPlugin can implement the following methods that serve as entry points for plugin execution:

``def launch(self): pass``
    This method should perform the main work of analysis.

``def result(self): pass``
    This function should return a python dictionary to be written to 'results.json', which is uploaded to the Torrent Server database and accessible through the REST API. Useful for data which should be made available to external systems. See Documentation for 'results.json'

``def output(self): pass``
    This function should return  a python dictionary to be written to 'output.json' and used to drive the Ion Plugin Template SDK – to simplify writing plugin report html files. See Documentation for the 'Ion Plugin Template SDK'.

The following class attributes are significant to the IonPlugin Runtime. All fields are optional, but setting a version is strongly recommended.

* ``version`` – string
    Specifies plugin version. Default "0.0"
* ``allow_autorun`` – boolean
    Allow a user to mark this plugin to automatically run after analysis based on plan data. (Must run with no additional user input.). Default: True
* ``features`` – list or tuple of Features – Extra Ion Plugin features this plugin support.
    Default: None.

    Valid values:

        ``Features.EXPORT`` – Causes plugin to appear in Export tab of Plan, separate from Analysis plugins.

* ``runtypes`` – list or tuple of RunTypes – Run only for a selected type of Run.
    Default: ``[ RunType.FULLCHIP, RunType.THUMBNAIL ]``.

    Valid values:

        ``RunType.FULLCHIP`` - Plugin Runs for PGM runs

        ``RunType.THUMBNAIL`` - Plugin Runs for Proton Thumbnail runs (a preliminary analysis of a small portion of the chip for QC purposes)

        ``RunType.COMPOSITE`` - Plugin Runs for Full Proton Runs (typically using BLOCK level analysis, these are large data sets)

.. note:: Advanced usage: All class attributes are marked as properties, and can be set to any python "callable".
    For example, all of the following are equivalent for version, and result in a version of "1.0.1"::
    version = "1.0.1"
    version = "%(major)d.%(minor)d.%(patch)d" % {'major': 1, 'minor': 0, 'patch': 1}
    version = '1.0.' + filter(str.isdigit, '$Revision:  1 $')
    def version(cls): return "1.0.1"

If you do use a 'callable', please note that these are class methods and will not have a full instance of the
plugin class. You can call other functions and class methods, but not instance methods (self).
Please keep them lightweight as they are invoked when your plugin is queried by the Torrent Browser UI.


It is recommended that you provide a docstring for your class. This is done in the usual python way
immediately under the class statement, as shown in the HelloWorld example above.

Providing the python shebang (#!) header, and the PluginCLI() call at the end will allow you to run your plugin on the command line for testing use:

::

    $python HelloWorld.py --help
    usage: HelloWorld.py [-h] [--version] [-v] [--dry-run] [--inspect]
                         [--runmode RUNMODE] [--block BLOCK]

    Ion Plugin Command Line Interface Ion Torrent Plugin - 'HelloWorld' v1.1.0
    Demo Plugin to show the new plugin definition and features

    optional arguments:
      -h, --help         show this help message and exit
      --version
      -v, --verbose
      --dry-run
      --inspect, --info

.. note::  Additional runmode and block flags are present for future use in analyzing Proton runs, but are currently unsupported.

Plugin Flags
------------

Plugin flags (new in 4.2):
* Features = EXPORT
* RunLevel = PRE/BLOCK/POST, DEFAULT, SEPARATOR, LAST
* RunType = COMPOSITE, THUMB, FULLCHIP

Plugin flags are specified in python as class attributes, and enums representing valid values are imported with ``from ion.plugin import *``.
For shell plugins, flags are specified in the file ``pluginconfig.json``
