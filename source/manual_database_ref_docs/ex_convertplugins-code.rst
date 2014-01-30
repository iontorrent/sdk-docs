Alignment.py
============

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
	
	class Alignment(IonPlugin):
		# Whatever 'version' is set to will show up as the plugin's version in your browser.
		version = '3.6.5602'
		
		# The dictionary that holds environment variables; use it to keep a consistent environment.
		envDict = dict(os.environ)
		
		# This method performs the same actions found in the 'launch.sh' file. You don't need to make separate methods, but it is easier to organize.
		def analyze(self):
			# (See below for an explanation of Popen.)
			alignRead = Popen(['%s/alignment.py'%self.envDict['DIRNAME'], 'startplugin.json', self.envDict['TSP_LIBRARY'], self.envDict['TSP_FILEPATH_UNMAPPED_BAM'], self.envDict['TSP_FILEPATH_BAM']], stdout=PIPE, env=self.envDict)
			
			# Write results to a file.
			alignOut = open('%s/Alignment_API_output.txt'%self.envDict['TSP_FILEPATH_PLUGIN_DIR'], 'w')
			# <Popen var>.communicate() returns a tuple of [stdout, stderr] for that command. [0] gets the standard output, [1] gets the error output.
			alignOut.write(alignRead.communicate()[0])
			alignOut.close()
			# Copy the files.
			Popen(['cp', '-r', '%s/Alignment_block.php'%self.envDict['DIRNAME'], self.envDict['TSP_FILEPATH_PLUGIN_DIR']], stdout=PIPE, env=self.envDict)
			Popen(['cp', '-r', '%s/library'%self.envDict['DIRNAME'], self.envDict['TSP_FILEPATH_PLUGIN_DIR']], stdout=PIPE, env=self.envDict)
		
		# Method to launch the plugin.
		def launch(self, data=None):
			# Get json data.
			json_dat = getattr(self, 'startpluginjson', None)
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
			
		# These methods are not necessary, but they are one way of reporting data.
		
		def report(self):
			pass
		
		def metric(self):
			pass
	
		# For debugging purposes.
		if __name__ == "__main__":
			PluginCLI(Alignment())
