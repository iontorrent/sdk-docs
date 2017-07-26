.. _plugin_getting_started:

Getting Started with Plugins
============================
The plugin framework is primarily an extension of the analysis pipeline and executes custom python modules (plugins) 
at different points in the pipeline process.  There are 3 reason for writing a plugin:

#. Data Management: the transfer or backup of data to a secondary file server or remote site.
#. Quality Assurance/Quality Control: These plugins check the quality of the data and give you access 
   to some of the larger and transient data used in signal processing, which are eventually deleted.
#. Application Analysis: This is broadest and most useful category which bridges the gap between general pipeline 
   workflow and application-specific analysis and reporting.

There is nothing strict about these categories. They have no technical bearing on the functioning of the plugins 
other than a conceptual framework for deciding whether to use a plugin or not.

Quick Start
-----------

Enter the following python code into a file called *MyPlugin.py* inside a new directory called *MyPlugin*.

.. code-block:: python

    import subprocess
    from ion.plugin import *


    class MyPlugin(IonPlugin):
        version = "1.0.0.0"

        def launch(self, data=None):
            output = subprocess.check_output(['ls', '-l'])
            with open("status_block.html", "w") as html_fp:
                html_fp.write("<html><body><pre>")
                html_fp.write(output)
                html_fp.write("</pre></body></html>")


    if __name__ == "__main__":
        PluginCLI()

Zip the *MyPlugin* directory. See :ref:`plugin_packaging` for help. Click *Install or Upgrade Plugin* to upload the archive 
on the TS plugins page. Navigate to an existing TS run report, click *Select Plugins to Run*, then select *MyPlugin*. 
The plugin code executes and the output displays in an iframe on the report


Pipeline Overview
-----------------

Plugins are fundamentally an ability to extend the functionality of the analysis pipeline.  At certain stages of the pipeline execution, each of these stages is represented as "Run Levels".

Configuration
^^^^^^^^^^^^^

Occasionaly, you need to configure plugins before their execution. 
To do this, the Plugin Framework offers three different caches for storing the configurations for the two different workflows for executing a plugin.

**Automated Pipeline Workflow**

* **1st Priority**: Plan Configuration
* **2nd Priority**: Global Configuration

**Manual Plugin Execution**

* **1st Priority**: Instance Configuration
* **2nd Priority**: Global Configuration

.. _getting_started_run_levels:

Run Levels
^^^^^^^^^^

One of the key attributes of any given plugin is the run level that directs the pipeline to execute the plugin
at each of these stages specified in the module.  It is important to remember that the same method is called in the 
plugin no matter what run level is currently being executed. So if you are going to use more than one run level, 
write the plugin code so it is conditionally based on the :ref:`reference_run_levels`.

When employing run levels, use one of the two following strategies. The conventional workflow covers almost all 
situations; therefore, it is the default approach.


**Block Levels**

When you use block-based run levels, we recommend that you use a combination of the three following run levels:

* PRE: This stage occurs before any significant processing happens, and is sufficient for preparation.
* BLOCK: Plugins are triggered once per block on the chip. This run level is never executed for runs that do not have block-level processing.
* POST: This stage occurs after the analysis pipeline is completely executed.  When executed, the plugin results output directory is a child directory of the normal plugin output directory named "post".

**Conventional Workflow**

This strategy is the default for non-block-level specific run levels and is used in a more conventional workflow.

* DEFAULT: Plugins are triggered at the end of pipeline processing after the four usual steps (see pipeline documentation for details).
* LAST: Plugins are executed after all other plugins that are not "LAST" have been executed. If there is more than one, all "LAST" run level plugins run concurrently.

**Internal Use Only**

* SEPARATOR: Do not use.


Dependencies
^^^^^^^^^^^^

The term "dependency" is not quite accurate. This attribute ensures that when a plugin with a "dependency" is set to run at a run level, it is scheduled to run after the declared dependency that also shares that run level. 
If the declared dependency is not scheduled to run at the same run level, then the plugin runs without any special scheduling.

OIA Integration
^^^^^^^^^^^^^^^

Currently, the "On Instrument Analysis" (OIA) is responsible for the first two portions of the pipeline execution.  
The OIA does not normally interfere with plugin execution. However, if you select the PRE run level, any OIA-based 
workflows are executed after the signal processing step. A pure TS implementation's PRE step is executed before the 
signal processing step.

Plugin Code
-----------

You must write the code for all plugins in python, so a basic understanding of both python and object oriented programming is required.

In order for the plugin to function, it must inherit from the base class IonPlugin contained in the module at ion.plugin. 
At a minimum, the version attribute and launch method need to be overridden.

Legacy Note
^^^^^^^^^^^

Legacy plugins that use a bash script called "launch.sh" are obsolete and should not be replicated.

Naming Your Plugin
^^^^^^^^^^^^^^^^^^

It is important to include the name of your plugin in the following:

* The directory containing the python plugin file
* The name of the python plugin file (not including the required .py file extension)
* The name of the class declared within the python plugin file that derives the IonPlugin base class
  
  NOTE: All are case-sensitive.

Plugin Version
^^^^^^^^^^^^^^
The version of the plugin must be a string that has the standard four-number formatting as follows:

*<Major>.<Minor>.<Revision>.<Build>*

Launch Method
^^^^^^^^^^^^^
The one required override method to implement in the plugin class is the launch method, which has only 
the self argument, and an unused "Data" argument with the "None" default.  
This method performs all the required actions to achieve the goal of the plugin as well as produce all the results files.

.. _plugin_packaging:

Packaging & Installation
------------------------

There are two supported methods for packaging and installing plugins into the system: the debian packaging system 
and a simple zip archive method.  This section describes only the zip archive method. The debian packaging system is described
elsewhere because it is more advanced.

When you create a zip package, the contents must use a file structure with a root folder that has the same name as the
plugin. All other contents are a child of this root folder:

Linux Bash Shell: 'zip -r --exclude=*.git* PluginName.zip PluginDirectory'

After you create the archive, go to http://TS_hostname/configure/plugins/ on the Torrent Suite Server, then 
click "Install or Upgrade Plugin" to submit your new archive.