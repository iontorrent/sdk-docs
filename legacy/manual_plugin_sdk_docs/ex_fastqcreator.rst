Plugin Example: Fastq Creator
=============================

|  :ref:`The_program`

The Fastq Creator is a pretty simple plugin written in python, to the new 3.x plugin specifications. It is a good example of what one of these plugins should look like.

The full code can be found `here <ex_fastqcreator-code.html>`_. It may be helpful to have it open while going through the code bit by bit.

.. _The_program:

The Program
-----------

**Pre-class Declaration**

.. code-block:: python

	#!/usr/bin/python
	# Copyright (C) 2012 Ion Torrent Systems, Inc. All Rights Reserved
	# FastqCreator plugin
	import os
	import glob
	import json
	import traceback
	import pysam
	import subprocess
	from ion.utils import blockprocessing
	from ion.plugin import *

	# DNA base complements
	COMPLEMENT = {'A': 'T',
		'T': 'A',
		'C': 'G',
		'G': 'C',
		'N': 'N'}

	def reverse_complement(sequence):
		return ''.join(COMPLEMENT[b] for b in sequence[::-1])

The shebang (#!...) simply tells anything trying to execute the script to use python. It means that you can run 'FastqCreator.py' instead of 'python FastqCreator.py'.

The import statements are pretty self-explanatory, they import the libraries necessary to run the plugin.

The COMPLEMENT variable defines base complements for use in the reverse_complements method.

Before the class declaration is a good place to put helper methods that you plan on using in the plugin. Here the reverse_complement method is a good example. It takes in a sequence and returns its complement. ''.join joins an array into a string, using '' to concatenate each element. In this case, the array to be joined contains the complement of each element in the given sequence, and nothing will be placed between each element.

**Class Declaration**

.. code-block:: python

	class FastqCreator(IonPlugin):
		version = "3.6.0-r%s" % filter(str.isdigit,"$Revision: 57238 $")
		runtypes = [ RunType.COMPOSITE, RunType.THUMB, RunType.FULLCHIP ]

The class has the same name as the file, and takes 'IonPlugin' as an argument.

Instead of the 2.x plugins' 'VERSION' string, 'version' is used to define the version string as it will appear next to the plugin's name. The change to lower caps is minor but important; using 'VERSION' will not work in a python plugin.

The 'runtypes' array states on which type of run the plugin should run. It only applies when the plugin is run automatically, if it's run manually through a report page's 'select plugins' dialog, it will do nothing. This is a new feature in the 3.x plugins and has no analogue in the old launch.sh plugins, which will run on all runtypes. Valid runtypes are:

	* RunType.FULLCHIP: whole chip (PGM) run.
	* RunType.THUMB: thumbnail run.
	* RunType.COMPOSITE: proton run.

**Launch method (part 1)**

*NOTE:* the launch method is near the bottom of the file, but it the first class method called. It's also a bit long, so it will be broken into parts.

.. code-block:: python

	def launch(self, data=None):
		
		with open('startplugin.json', 'r') as fh:
			spj = json.load(fh)
			net_location = spj['runinfo']['net_location']
			basecaller_dir = spj['runinfo']['basecaller_dir']
			alignment_dir = spj['runinfo']['alignment_dir']
			barcodeId = spj['runinfo']['barcodeId']
			runtype = spj['runplugin']['run_type']
		
		url_path = os.getenv('TSP_URLPATH_PLUGIN_DIR','./')
		print url_path
		output_stem = os.getenv('TSP_FILEPATH_OUTPUT_STEM','unknown')
		print "TSP_FILEPATH_OUTPUT_STEM: %s" % output_stem
		
		reference_path = os.getenv('TSP_FILEPATH_GENOME_FASTA','')
		
		with open(os.path.join(basecaller_dir, "datasets_basecaller.json"),'r') as f:
			datasets_basecaller = json.load(f);

Each method within the class takes 'self' as an argument, and launch takes 'data' as well.

'startplugin.json' holds the relevant json data that the plugin may need to access. The indented block here opens the json file, uses python's json library to parse it, and then defines some variables based on its contents.

'os.getenv(var, val)' tries to retrieve 'var' from the environment, and defaults to 'val' if it is not found. So a few variables are set from the environment after parsing the json.

The plugin then loads some more json data from a separate file.

**Launch method (part 2)**

.. code-block:: python

	for dataset in datasets_basecaller['datasets']:
		print dataset

		# input
		bam_list = []
		if reference_path != '':
			# don't use aligned bam files (TS-6279) or reverse-complemented it
			bam = os.path.join(alignment_dir, dataset['file_prefix']+'.bam')
		else:
			bam = os.path.join(basecaller_dir, dataset['file_prefix']+'.basecaller.bam')
		print bam
		if os.path.exists(bam):
			bam_list.append(bam)

		# output
		if barcodeId:
			dataset['fastq'] = dataset['file_prefix'].rstrip('_rawlib')+'_'+output_stem+'.fastq'
		else:
			dataset['fastq'] = output_stem+'.fastq'

		if len(bam_list) == 0:
			print 'WARNING: missing input file(s) for %s' % dataset['fastq']
			continue

		try:
			#use pysam only for unmapped bam files
			#self.bam2fastq_pysam(bam_list,dataset['fastq'])
			self.bam2fastq_picard(bam_list,dataset['fastq'])
		except:
			traceback.print_exc()

'datasets_basecaller' was loaded in part 1 of the launch method. This loop iterates through each elements of the 'datasets' block within that object.

Each iteration runs the 'bam2fastq_picard' method, defined below, but first a couple of defeinitions are made.

'bam_list' is appended with the appropriate bam file location, and the 'fastq' entry of the current dataset is defined based on whether or not the plugin is running on a barcoded run.

**bam2fastq_picard**

.. code-block:: python

	def bam2fastq_picard(self, bam_filename_list, fastq_filename):
		try:
			com = blockprocessing.bam2fastq_command(bam_filename_list[0],fastq_filename)
			ret = subprocess.call(com,shell=True)
		except:
			traceback.print_exc()

A list of bam filenames, and a fastq filename are taken as arguments.

Subprocess is a python module that allows execution of system commands. Here, 'com' is set to the return value of blockprocessing's bam2fastq_command method, and then that command is executed through subprocess' call method.

**Launch method (part 3)**

.. code-block:: python

	with open('FastqCreator_block.html','w') as f:
		f.write('<html><body>To download: "Right Click" -> "Save Link As..."<br>\n')
		
		for fastq_file in glob.glob('* .fastq'):
			size = os.path.getsize(fastq_file)/1000
			f.write('<a href="%s">%s</a> %sK<br>\n'
				%(os.path.join(net_location, url_path, fastq_file), fastq_file, size))
		f.write('</body></html>\n')
	
	return True

Here, the 'block' html file is written to. While <plugin_name>.html is used as the main output page, and instance.html is used to display an options page when the plugin is first run, <plugin_name>_block.html is treated as a sort of preview. It will show up in the plugin's status block at the bottom of the report (3.x python plugins only), as well as in the report itself.

Returning True allows the plugin to exit gracefully. It is also possible to use sys.exit(0), but keep in mind that this does not always work well when a plugin is running at the block level on proton runs, so 'return True' is preferable.

**bam2fastq**

The bam2fastq method is not called within the plugin itself, but an explanation of the method can be found `here. <ex_fastqcreator-3.html>`_ *(I'm not entirely clear what the method is doing there, but don't want to delete or omit it...)*

**Report & Metrics methods**

.. code-block:: python

	def report(self):
		output = {
			'sections': {
				'title': 'FastqCreator',
				'type': 'html',
				'content': '<p>FastqCreator util</p>',
			},
		}
		return output

	def metrics(self):
		""" Write result.json metrics """
		return { 'blocks': 96 }

The 'report' method outputs report data in json form, while the 'metrics' method outputs extra json metrics data.

**Debugging launch method**

.. code-block:: python

	# dev use only - makes testing easier
	if __name__ == "__main__": PluginCLI(FastqCreator())

This method just makes sure that the plugin runs; it makes quickly testing them easier.

*(Why is it marked dev use only? Does it make the plugins runnable from the filesystem or something?)*
