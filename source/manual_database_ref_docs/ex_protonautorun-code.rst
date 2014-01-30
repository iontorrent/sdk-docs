Proton Autorun Plugin Example Code
==================================

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
		# The run levels are: (RunLevel.<level>)
		#	PRE:   run once all block jobs have been submitted.
		#	BLOCK: run after each individual block finishes. (So, up to 96 times.)
		#	POST:  run after everything is done.
		# The run types are: (RunType.<type>)
		#	FULLCHIP:  PGM full chip analysis.
		#	THUMB:     Thumbnail analysis.
		#	COMPOSITE: Proton analysis.
		runtypes = [ RunType.COMPOSITE ]
		runlevels = [ RunLevel.PRE, RunLevel.BLOCK, RunLevel.POST ]
		envDict = dict(os.environ)
		
		# The launch script will check what run level we are on and act appropriately.
		# NOTE: this plugin is designed to be run in automatic mode, and it assumes that the run is composite due to the runtypes filter.
		def launch(self, data=None):
			# Read json data.
			json_file = open('%s/startplugin.json'%self.envDict['TSP_FILEPATH_PLUGIN_DIR'], 'r')
			json_dat = json.loads(json_file.read())
			json_file.close()
			
			# Define the run level.
			runlevel = json_dat['runplugin']['runlevel']
			print '----------\nRUN LEVEL: %s\nPLUGIN DIR: %s\n-----------'%(runlevel, self.envDict['TSP_FILEPATH_PLUGIN_DIR'])
			
			# Open the html block file for appending and reading.
			htmlPath = '%s/plugin_out/protonAutoBlockProcessEx_out/protonAutoBlockProcessEx_block.html'%self.envDict['ANALYSIS_DIR']
			htmlOut = open(htmlPath, 'a+')
			if os.path.getsize(htmlPath) == 0:
				htmlOut.write('<html><body>')
			
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

	if __name__ == '__main__':
		PluginCLI(protonAutoBlockProcessEx())
