Torrent Suite™ Software Introduction to Writing Plugins
=======================================================

Introduction
------------

Plugins are distributed and installed as ZIP archives containing the plugin definition (shell or python) any other applications
and resources needed to function.

Plugins can be defined using a simple shell script named 'launch.sh'. This shell script serves as the entry point for execution of the
plugin and can be used to launch other applications, scripts, or binaries included in the plugin archive. Any command that
can be executed on the command line can be run in a launch.sh plugin, using environment variables set by the plugin framework
to access input files, output folders, and other analysis settings.

Since Torrent Suite 3.0, plugins can alternately be defined using a python class. This plugin class definition is
instantiated by the plugin framework and has multiple entry points to hook into the plugin processing workflow.
The primary entry point for a python plugin is a 'launch' method on a class that inherits from the `IonPlugin` base class.
Using python to define the plugin provides access to a Torrent Suite specific helper runtime library of utility functions,
the power of the standard python library, and the vast array of third party python libraries.

Key Differences in shell vs python plugins
------------------------------------------
Plugins using a 'launch.sh' script are all submitted to the queue after the completion of the main analysis
pipeline.

Python plugins can register for several different RunLevels, which are invoked at various stages in the analysis pipeline.
They can also perform block level analysis, where portions of the plugin are invoked many times during analysis.

For a shell plugin, setting configuration requires separate 'pluginsettings.json',  and 'pluginconfig.json' files.
The settings possible in these files are incorporated into a python class definition as class attributes.

A plugin defined using a Python class can be instantiated and queried without executing the analysis
portion of the plugin.  A shell script can only be executed at plugin runtime, and must be carefully parsed for
``VERSION`` and ``AUTORUNDISABLED`` values. These must be defined as simple strings as these lines are not executed during parsing.
Python allows these methods to be defined as python variables or callables, allowing plugin framework parameters to be
computed dynamically based on system parameters or user selections.

A shell script has a single entry point (ie. the only option is to execute the script), but multiple methods can be
defined in a python class for various stages of analysis, allowing parts of the plugin to run at different points in the
Analysis pipeline.  All the configuration and plugin framework interaction can be driven by a single script.
This also provides plenty of opportunity for future expansion of plugin capabilities and inclusion of additional features.

Lastly, python has a rich set of existing libraries, and we can wrap common Ion Torrent specific functionality into our
own library, with an IonPlugin SDK of reusable components.

Writing a simple shell plugin
------------------------------
Shell scripts are simple and make it easy to wrap sequences of command line programs.

ExampleShellPlugin/launch.sh:

.. code-block:: bash

  #!/usr/bin/env ionPluginShell
  VERSION='1.0'
  echo "This is a launch.sh plugin"
  echo "Read from ${ANALYSIS_DIR}, write to ${OUTPUT_DIR} (or cwd)"
  echo "<pre>BAM FILE is ${TSP_FILEPATH_BAM}</pre>" > plugin_block.html

Shell scripts can access analysis data via environment variables (set for you).

For example, ``TSP_FILEPATH_BAM``, ``ANALYSIS_DIR``, ``BASECALLER_DIR``, ``TSP_CHIPTYPE``, ``TSP_NUM_FLOWS``, etc.
See Plugin API reference documentation for complete listing.
Use these values to launch any program of your choosing with appropriate arguments.

Output written to an html file ending in "_block.html" will be shown inline in an iframe in the plugin section.
Other html files will be linked to from the report.

Writing a simple python plugin
------------------------------
Python scripts have a few additional features for Proton analysis and running selectively.

ExampleIonPlugin/ExampleIonPlugin.py:

.. code-block:: python

  #!/usr/bin/env python
  from ion.plugin import *
  class ExampleIonPlugin(IonPlugin):
      version='1.0.0'
      def launch(self):
          print "This is a python based plugin"

While python can access the same environment variables, the preferred approach is to parse the startplugin.json file in python and access the values directly.

Python specific attributes::

  Features = EXPORT
  RunLevel = PRE/BLOCK/POST, DEFAULT, SEPARATOR, LAST
  RunType = FULLCHIP, THUMB, COMPOSITE

.. code-block:: python

    #!/usr/bin/env python
    from ion.plugin import *
    import os
    import json
    import requests

    class HelloWorld(IonPlugin):
        """  Demo Plugin to show the new plugin definition and features """
        version = "1.0.1"
        features = [ Feature.EXPORT, ]
        runtypes = [ RunType.THUMB, RunType.FULLCHIP, RunType.COMPOSITE ]
        runlevel = [ RunLevel.BLOCK, RunLevel.DEFAULT ]


Writing Ion Plugins in Python
-----------------------------

Let's get started with IonPlugin classes.
To write a plugin using the Ion Torrent Suite Plugin Framework you must:

#. Name your plugin. The name must match between the folder and implementation file and class.
    We'll call our example plugin "HelloIonWorld"
    Names must be a valid python identifier.
#. Create the plugin folder and python script.
    .. code-block:: bash

      $ mkdir HelloIonWorld; touch HelloIonWorld/HelloIonWorld.py
#. Edit the python file you just created.
    Import the IonPlugin libraries and create a class for your plugin which inherits from IonPlugin.

    .. code-block:: python

      from ion.plugin import *
      class HelloIonWorld(IonPlugin):
          pass

You now have a valid Ion Plugin, which will install and run on the Torrent Server. But it doesn't do anything interesting yet. Let's continue.
Replace the empty implementation ``pass`` with code implementing your plugin. Add a version number to indicate this has changed.

.. code-block:: python

    from ion.plugin import *
    class HelloIonWorld(IonPlugin):
      """ A plugin for saying hello. """
      # Plugin Configuration
      version = "1.0"
      # launch - Runs at the default runlevel
      def launch(self, data=None):
        print "Hello Ion World!"


Suggestion:  To quickly convert a launch.sh plugin, rename launch.sh to another name, and use the
runtime 'call' method to invoke it under launch.

.. note:: The ``VERSION`` and ``AUTORUNDISABLE`` flags will not be read from the renamed shell script, so they must be
   set in the python class.


.. code-block:: python

    #!/usr/bin/env python
    from ion.plugin import *
    class HelloIonWorld(IonPlugin):
      """ Demo Plugin to show the new plugin definition and features. """
      # Plugin Configuration
      version = "1.1"
      allow_autorun = True

      # launch - Runs at the default runlevel
      def launch(self):
        print "Hello Ion World!"
        ## sayhello.sh is the former launch.sh
        # self.call is aliased to python subprocess.call
        self.call("sayhello.sh","-j","startplugin.json")

    if __name__ == "__main__": PluginCLI()

This will run your shell script in a equivalent fashion to one named 'launch.sh'.
We've also added a python header, and a main method, which allows you to run the plugin directly on the command line,
for development and testing use. It is not required for running within the Torrent Server.

But please, don't stop there. Calling a shell script is a poor use of the new plugin classes. Now that you are running
in a full python environment, consider implementing the behavior of your plugin in python itself.

