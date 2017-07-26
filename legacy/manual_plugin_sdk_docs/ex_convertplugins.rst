Converting a Shell Plugin to a Python Plugin
============================================

The goal of this document is to walk through converting a plugin's 'launch.sh' file to a '<plugin_name>.py' file that
follows the new guidelines for python plugins.

Please note that plugins utilizing a launch.sh file will continue to function normally, so it is not necessary to
perform this conversion. However, the new system supports a robust set of new features, many of which are not available to plugins running via launch.sh.

|  :ref:`Alignment_launch`
|  :ref:`Converted_alignment`

In general, the idea is to mimic the commands run by the launch.sh file.
	* Changes to the environment can be tracked in a couple of ways using the os module. Either a dictionary can be made to hold a copy of the variable which is updated as needed, or the os.[get|put]env methods.
		* Using a separate dictionary is recommended, as it allows the updated environment to be passed into subprocess calls. This is particularly useful when calling external shell scripts.
	* Python's subprocess module can be used to launch shell commands and/or functions.

The Alignment plugin provides a simple, real-world example. In its case, the whole script could probably be replaced by the 'alignment.py' file which is called in the original launch.sh. But it provides a good example of how to deal with shell commands and environment variables in the new 3.x plugin system.

.. _Alignment_launch:

Alignment's 'launch.sh'
-----------------------

.. code-block:: console

	#!/bin/bash
	# Copyright (C) 2011 Ion Torrent Systems, Inc. All Rights Reserved
	#AUTORUNDISABLE
	#normal plugin script
	
	VERSION="3.6.56201"
	
	$DIRNAME/alignment.py startplugin.json ${TSP_LIBRARY} $	{TSP_FILEPATH_UNMAPPED_BAM} ${TSP_FILEPATH_BAM} >> $TSP_FILEPATH_PLUGIN_DIR/launch_sh_output.txt
	cp -r $DIRNAME/Alignment_block.php $TSP_FILEPATH_PLUGIN_DIR/
	cp -r $DIRNAME/library $TSP_FILEPATH_PLUGIN_DIR/

The commands performed are pretty simple. A shebang tells anything running it to use bash, autorun is disabled by the AUTORUNDISABLE comment at the top, and the VERSION variable is set to 3.6.56201.

The actual plugin simply calls 'alignment.py' with 'startplugin.json' and a few environment variables as arguments, then pipes the output to launch_sh_output.txt. Finally, it copies some files from the directory it resides in to the plugin output directory.

.. _Converted_alignment:

Converted Alignment Plugin
--------------------------

The converted python file will be walked through in parts, the whole code can be viewed `here. <ex_convertplugins-code.html>`_

**Pre-class Definitions**

.. code-block:: python

	#!/usr/bin/python
	# Copyright (C) 2013 Ion Torrent Systems, Inc. All Rights Reserved
	
	import markdown
	import operator
	import os
	import sys
	import simplejson as json
	from subprocess import *
	from ion.plugin import *
	from django.utils.datastructures import SortedDict

This is fairly self-explanatory, just import the python modules necessary for running the plugin. The markdown, operator, and json modules are used to parse the startplugin.json file, os and sys are used to access certain system functions and commands, subprocess is used to execute shell commands, and ion.plugin contains the information necessary to make this a plugin rather than an ordinary .py file. The django import is just a convenient data structure.

**Class Declaration**

.. code-block:: python

	class Alignment(IonPlugin):
		# Whatever 'version' is set to will show up as the plugin's version in your browser.
		version = '3.6.5602'
		runtypes = []
		
		# The dictionary that holds environment variables; use it to keep a consistent environment.
		envDict = dict(os.environ)

The class' name should be the same as both the filename and the plugin directory name. In this case, the class is Alignment, the file is Alignment.py, and the directory is (you guessed it) /results/plugins/Alignment/. Further, the class should take 'IonPlugin' as an argument.

Note that the 'version' variable is lower case; in the launch.sh files it was in all caps. The runtypes array states which types of run this plugin can be run automatically on. In this case it is empty, mimicking the AUTORUNDISABLE flag.

The 'envDict' variable is very important and useful. It holds a dictionary with a copy of the 'os.environ' variable. Since python uses its own little environment, changes made to os.environ *will not* be reflected outside of the script. For this reason, it is important to keep a copy of python's environment updated and ready to pass to any relevant shell scripts.

So, the equivalent of ${<var>} is [self.]envDict['<var>'].

**'analyze' Method**

NOTE: This method is not called directly when the plugin is run. It is called from the launch method, which runs first and is defined below.

.. code-block:: python

		# This method performs the same actions found in the 'launch.sh' file.
		# You don't need to make separate methods, but it is easier to organize.
		def analyze(self):
			# (See below for an explanation of Popen.)
			alignRead = Popen(['%s/alignment.py'%self.envDict['DIRNAME'], 'startplugin.json', \
				self.envDict['TSP_LIBRARY'], self.envDict['TSP_FILEPATH_UNMAPPED_BAM'], \
				self.envDict['TSP_FILEPATH_BAM']], stdout=PIPE, env=self.envDict)
			
			# Write results to a file.
			alignOut = open('%s/Alignment_API_output.txt'%self.envDict['TSP_FILEPATH_PLUGIN_DIR'], 'w')
			# <Popen var>.communicate() returns a tuple of [stdout, stderr]
			# for that command. [0] gets the standard output, [1] gets the error output.
			alignOut.write(alignRead.communicate()[0])
			alignOut.close()
			# Copy the files.
			Popen(['cp', '-r', '%s/Alignment_block.php'%self.envDict['DIRNAME'], \
				self.envDict['TSP_FILEPATH_PLUGIN_DIR']], stdout=PIPE, env=self.envDict)
			Popen(['cp', '-r', '%s/library'%self.envDict['DIRNAME'], \
				self.envDict['TSP_FILEPATH_PLUGIN_DIR']], stdout=PIPE, env=self.envDict)


The first Popen command imitates the first line of the corresponding launch.sh file. The file to write to is then opened, and written to. Note that while the results of the communicate method are not assigned to any particular variable here because it is only used once, it is a good idea to use the following general syntax if a command's stderr or stdout output is accessed multiple times:

.. code-block:: python

	cmdRead = Popen([cmd, args], stdout=PIPE, env=self.envDict)
	(cmdOut, cmdErr) = cmdRead.communicate()

**'launch' Method**

.. code-block:: python

		# Method to launch the plugin.
		def launch(self, data=None):
			# Get json data.
			json_dat = getattr(self, 'startplugin.json', None)
			if not json_dat:
				try:
					with open('startplugin.json', 'r') as fh:
						json_dat = json.load(fh)
				except:
					sys.stderr.write('ERROR: could not read plugin json.')
			
			# Next, interpret the json. Store it in a sorted dictionary, and use markDOWN to format the markUP! (html)
			pluginjson = SortedDict()
			md = markdown.Markdown(extensions=['codehilite'], safe_mode='escape')
			for (k,v) in sorted(json_dat.iteritems()):
				text = json.dumps(v, indent=2).split('\n')
				text = '\n\t'.join(text)
				html = md.convert(text)
				pluginjson.insert(-1, k, html)
			
			# Update the context to hold the json data.
			context = { 'pluginjson' : pluginjson }
			self.context.update(context)
			
			# Do the analysis.
			self.analyze()
			
			# Exit gracefully.
			return True

Each plugin must have a launch method, which is run when the plugin is launched. It takes a json 'data' argument in addition to the usual 'self' one, but here the relevant json data is in the startplugin.json file. It isn't actually necessary to parse the json file here, since the python file called in the 'analyze' method does so anyways, but it is worth demonstrating as an example.

First, getattr is attempted to quickly read the json file. Failing that, the file is opened and read normally. The result is given to a SortedDict, after being parsed by the markdown module. Finally, the context is updated to hold the json data.

After startplugin.json is parsed, the analyze method is called, after which the plugin returns True.

**Other output methods**

For completeness' sake, there are some methods which can be used to output json data in different ways. *Some more explanation could be used here.*

.. code-block:: python

		# These methods are not necessary, but they are one way of reporting data.
		def report(self):
			pass
		
		def metric(self):
			pass
