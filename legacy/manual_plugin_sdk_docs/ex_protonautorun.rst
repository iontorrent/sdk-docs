Performing Customized Analysis on Proton Runs
=============================================

The purpose of this document is to familiarize you with the enhanced level of customization offered by the new 3.x plugin system by walking through the creation of a plugin designed to analyze proton runs. When run automatically, this example plugin will perform simple tasks at specified points during analysis; before any blocks have finished, after each individual block, and once the analysis has been completed.

This document assumes that you have a basic familiarity with the 3.x plugin structure. The `FastqCreator example <ex_fastqcreator.html>`_ should help, and the HelloWorld plugin is a good example that is worth looking at.

This plugin should demonstrate some of the new 3.x features, and serve as a useful template. The full source code of this example can be found `here. <ex_protonautorun-code.html>`_

|  :ref:`Class_declaration`
|  :ref:`Launch_p1`
|  :ref:`Launch_p2`

.. _Class_declaration:

Class Declaration
-----------------

.. code-block:: python

	#!/usr/bin/python
	# Copyright (C) 2013 Ion Torrent Systems, Inc. All Rights Reserved

	import datetime
	import os
	import sys
	import simplejson as json
	from subprocess import *
	from ion.plugin import *
	from django.utils.datastructures import SortedDict

	class protonAutoBlockProcessEx(IonPlugin):
		version = '0.5'
		# Define when this plugin will automatically run.
		# In this case, we only want it to run on composite (proton) runs.
		runtypes = [ RunType.COMPOSITE ]
		runlevels = [ RunLevel.PRE, RunLevel.BLOCK, RunLevel.POST ]
		envDict = dict(os.environ)

The lines worth noting here are the definitions of 'runtypes' and 'runlevels'. These arrays contain the run types and levels that this plugin will automatically run on (when it is set to autorun). Note that these variables cannot be used to restrict when a plugin can be run manually.

Run types refer to the type of report being generated. The three options are defined below. In this case, we only want this plugin to run on proton data sets, so we set RunType.COMPOSITE.

+---------------+----------------------------+
| Run Type      | Definition                 |
+===============+============================+
| FULLCHIP      | Whole chip analysis (PGM). |
+---------------+----------------------------+
| THUMB         | Thumbnail analysis.        |
+---------------+----------------------------+
| COMPOSITE     | Proton analysis.           |
+---------------+----------------------------+

Run levels refer to when the plugin should run within an analysis. Not every level is relevant to non-proton runs. The run levels that can be used are:

+---------------+--------------------------------------------------+
| Run Level     | Definition                                       |
+===============+==================================================+
| PRE           | Runs after all analysis jobs are submitted, but  |
|               | before any are completed.                        |
+---------------+--------------------------------------------------+
| BLOCK         | Runs once every time a block analysis finishes.  |
|               | So, up to 96 times in total. The plugin_out dir  |
|               | for a plugin with this run level is within the   |
|               | block's individual directory.                    |
+---------------+--------------------------------------------------+
| POST          | Runs after all block analysis jobs are finished. |
+---------------+--------------------------------------------------+
| LAST          | Runs after all plugins in POST have run. If more |
|               | than one plugin has this run level, they will    |
|               | run at the same time.                            |
+---------------+--------------------------------------------------+
| DEFAULT       | Default run level, used in whole chip runs, etc. |
+---------------+--------------------------------------------------+

For this example, the plugin will run at the PRE, BLOCK, and POST run levels in order to demonstrate when each one occurs.

.. _Launch_p1:

Launch Method (Part 1)
----------------------

.. code-block:: python

	# The launch script will check what run level we are on and act appropriately.
	# NOTE: this plugin is designed to be run in automatic mode,
	# and it assumes that the run is composite due to the runtypes filter.
	def launch(self, data=None):
		# Read json data.
		json_file = open('%s/startplugin.json'%self.envDict['TSP_FILEPATH_PLUGIN_DIR'], 'r')
		json_dat = json.loads(json_file.read())
		json_file.close()

		# Define the run level.
		runlevel = json_dat['runplugin']['runlevel']
		print '----------\nRUN LEVEL: %s\nPLUGIN DIR: \
			%s\n-----------'%(runlevel, self.envDict['TSP_FILEPATH_PLUGIN_DIR'])

		# Open the html block file for appending and reading.
		htmlPath = '%s/plugin_out/protonAutoBlockProcessEx_out/\
			protonAutoBlockProcessEx_block.html'%self.envDict['ANALYSIS_DIR']
		htmlOut = open(htmlPath, 'a+')
		if os.path.getsize(htmlPath) == 0:
			htmlOut.write('<html><body>')

The first part of the launch method quickly loads the json data from 'startplugin.json' and uses it to determine the current run level. It then opens a common 'block' html file for appending and writes a small header if it is empty.

A little more on run levels: a plugin is not run once and put on hold until the analysis reaches an appropriate run level. Instead, it is run separately at each run level. For this reason, it is important to check the level and ensure that the plugin acts appropriately with regards to the fact that it may be run multiple times.

For example, instead of opening a file with the 'w' (write) argument, which will replace any file with the same name rather than adding to it, consider opening it with the 'a+' (appending/reading) argument, which will not overwrite the file's contents.

Further, be aware that the directory in which the plugin is running can change between levels. PRE and POST levels will be run from the normal plugin_out directory, but each BLOCK level will take place in a plugin_out directory within the block's individual path. Here, the 'ANALYSIS_DIR' environment variable is used to access the html file because unlike the 'TSP_FILEPATH_PLUGIN_DIR' variable, it remains consistent across the various levels.

These distinctions can also be useful, for example if you wanted to output a different analysis file for each block. It takes a bit more careful planning, but there are also more features available.

.. _Launch_p2:

Launch Method (Part 2)
----------------------

.. code-block:: python

	# Take action based on run level.
	if runlevel == 'pre':
		print '    PRE-run launch @%s'%datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		htmlOut.write('<br/><b>PRE-run</b> "analysis" launch. Time=%s'%datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	elif runlevel == 'block':
		# Determine the block's X & Y coord's from its filepath.
		bDir = self.envDict['TSP_FILEPATH_PLUGIN_DIR']
		bX = bDir[bDir.find('_X')+2:bDir.find('_Y')]
		bY = bDir[bDir.find('_Y')+2:bDir.find('/', bDir.find('_Y'))]
		print '    BLOCK X%s_Y%s launch @%s'%(bX, bY, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		htmlOut.write('<br/><b>BLOCK X%s_Y%s</b> "analysis" launch. Time=%s'%(bX, bY, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
	elif runlevel == 'post':
		print '    POST-run launch @%s'%datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		htmlOut.write('<br/><b>POST-run</b> "analysis" launch. Time=%s'%datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		htmlOut.write('</body></html>')
	elif runlevel == 'default':
		print '    DEFAULT launch @%s'%datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		htmlOut.write('<br/><b>DEFAULT</b> "analysis" launch. Time=%s'%datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		htmlOut.write('</body></html>')
	else:
		print '    \**Unrecognized run level.'

	# Exit gracefully.
	htmlOut.close()
	return True

Here, specific action is taken depending on which level the plugin was run at. If your plugin allows for more than one run type, you should also check that. Since this will only run on proton runs though, we already know the run type and the run levels are all that will be checked. Note that (for example) the RunType.POST level has a json value of 'post'. Be sure to check the literal value that represents your desired run level instead of using the RunType value. Further, while the default run level is supported, the PRE, BLOCK, and POST levels are all that this plugin should see in a proton run.

This plugin's "analysis" consists of printing a single line at each level to stdout and the html file defined above. Each line consists of the run level, the block's coordinates if applicable, and a timestamp formatted to 'year-month-day hour:minute:second'. This output can be replaced with analysis of any complexity though, so it's a good template for a proton autorun plugin.

And finally, the plugin closes the html file and returns True. There is also the usual debugging launch method at the very bottom of the file:

.. code-block:: python

	if __name__ == '__main__':
		PluginCLI(protonAutoBlockProcessEx())
