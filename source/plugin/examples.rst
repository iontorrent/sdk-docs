.. _plugin_examples:

Plugin Examples
===============

This section has a very basic example plugin and its code.

Basic Plugin
------------

This plugin goes through the explog and presents a few entries in the plugin output.  
It produces an HTML output but does not take any parameters.

::

    #!/usr/bin/python
    # Copyright (C) 2013 Ion Torrent Systems, Inc. All Rights Reserved

    #
    # Samples: LogParser
    # plugin demonstrating simple log parsing ability
    #

    import json
    import os
    from django.utils.functional import cached_property
    from ion.plugin import *


    class LogParser(IonPlugin):
        # The version number for this plugin
        version = "5.4.0.0"

        # this plugin can run on fullchip runs, thumbnail runs, and composite (merged via project page) runs
        # when this plugin is manually launched, only the 'launch' method is called
        runtypes = [RunType.FULLCHIP, RunType.THUMB, RunType.COMPOSITE]

        # specify when the plugin is called.  For log parsing, stay simple and just get called when the run completes.
        # the plugin can also be called before the run starts, at the block level, or after all other default plugins run
        runlevels = [RunLevel.DEFAULT]

        # a simple cached version of the start plugin property
        @cached_property
        def startplugin_json(self):
            return self.startplugin

        def read_explog(self):
            """This method reads and outputs an array of colon-delimited key/value pairs from the explog_final.txt"""

            path = os.path.join(self.startplugin_json['runinfo']['raw_data_dir'], "explog_final.txt")
            if not os.path.exists(path):
                raise Exception("explog_final.txt missing")

            # parse the log file for all of the values in a colon-delimited parameter
            data = dict()
            for line in open(path):
                # accommodates formatting issues in explog
                datum = line.split(":", 1)
                if len(datum) == 2:
                    key, value = datum
                    data[key.strip()] = value.strip()

            return data

        def launch(self, data=None):
            """This is the primary launch method for the plugin."""

            na = '<strong>NA</strong>'
            # creates a results object that is written out later.  This holds data that can be scrapped by a LIMS system, 
			and will be part of the |TS| database
            exp_log_data = self.read_explog()
            results_json = {
                'Project': exp_log_data.get('Project', None) or na,
                'Sample': exp_log_data.get('Sample', None) or na,
                'Library': exp_log_data.get('Library', None) or na,
            }

            # open up an HTML file to dump interesting log file findings to
            with open(self.startplugin_json['runinfo']['results_dir'] + '/LogParser_block.html', 'w') as html_handle:
                html_handle.write('<html><body>')
                html_handle.write("Project is: %s<br \>" % results_json['Project'])
                html_handle.write("Sample is: %s<br \>" % results_json['Sample'])
                html_handle.write("Library is: %s<br \>" % results_json['Library'])
                html_handle.write('</body></hmtl>')

            # write out our results json object
            with open(self.startplugin_json['runinfo']['results_dir'] + '/results.json', 'w') as results_handle:
                json.dump(results_json, results_handle, indent=4)

            return True

    # Devel use - running directly
    if __name__ == "__main__":
        PluginCLI()

Plugin which uses a subprocess
______________________________

::

    #!/usr/bin/python
    # Copyright (C) 2013 Ion Torrent Systems, Inc. All Rights Reserved

    #
    # Samples: LogParser
    # plugin demonstrating simple log parsing ability
    #

    import json
    import os
    from django.utils.functional import cached_property
    from ion.plugin import *
    from subprocess import check_output


    class CallSubprocessExample(IonPlugin):
        # The version number for this plugin
        version = "5.4.0.0"

        # this plugin can run on fullchip runs, thumbnail runs, and composite (merged via project page) runs
        # note that when the plugin is manually launched, only the 'launch' method will be called
        runtypes = [RunType.FULLCHIP, RunType.THUMB, RunType.COMPOSITE]

        # specify when the plugin is called.  For log parsing, stay simple and just get called when the run completes.
        # but can also be called before the run starts, at the block level, or after all other default plugins run
        runlevels = [RunLevel.DEFAULT]

        # a simple cached version of the start plugin property
        @cached_property
        def startplugin_json(self):
            return self.startplugin

        def launch(self, data=None):
            """This is the primary launch method for the plugin."""

            path_to_executable = "MyExecutable"
            arg1 = 'First Argument'
            arg2 = 'Second Argument'
            results = check_output([path_to_executable, arg1, arg2], cwd=self.startplugin_json['runinfo']['plugin']['path'])

            return True

    # Devel use - running directly
    if __name__ == "__main__":
        PluginCLI()

Accessing Barcode Data
----------------------

::

    #!/usr/bin/python
    # Copyright (C) 2013 Ion Torrent Systems, Inc. All Rights Reserved

    #
    # Samples: LogParser
    # plugin demonstrating simple log parsing ability
    #

    import json
    import os
    from django.utils.functional import cached_property
    from ion.plugin import *
    from subprocess import check_output


    class BarcodesExample(IonPlugin):
        # The version number for this plugin
        version = "5.4.0.0"

        # this plugin can run on fullchip runs, thumbnail runs, and composite (merged via project page) runs
        # note that when the plugin is manually launched, only the 'launch' method will be called
        runtypes = [RunType.FULLCHIP, RunType.THUMB, RunType.COMPOSITE]

        # specify when the plugin is called.  For log parsing, stay simple and just get called when the run completes.
        # but can also be called before the run starts, at the block level, or after all other default plugins run
        runlevels = [RunLevel.DEFAULT]

        # a simple cached version of the start plugin property
        @cached_property
        def startplugin_json(self):
            return self.startplugin

        @cached_property
        def barcodes_json:
            with open('barcodes.json', 'r') as barcodes_handle:
                return json.load(barcodes_handle)

        def launch(self, data=None):
            """This is the primary launch method for the plugin."""

            for barcode_name, barcode_values in self.barcodes_json.iteritems():
                # do you work per barcode here!
                print("Barcode Name: " + barcode_name)
                print("Bam File: " + barcode_values['bam_file']

            return True

    # Devel use - running directly
    if __name__ == "__main__":
        PluginCLI()


Using the REST API
------------------
::

    import json
    import requests
    api_response = requests.get('http://HOSTNAME/APPNAME/api/v1/APIENDPOINT/?ARG1=VAL1&api_key=' + self.startplugin['runinfo']['api_key'])
    api_response.raise_for_status()
    api_json_response = json.loads(api_response.content)


Displaying Progress
-------------------

When displaying progress, this needs to be manually updated by re-writing the \*_block.html file intermittently during the process.  
Here is a simple example of how to construct a method to do this.

::

    ...
    def update_progress(self, current_progress, max_progress)
        with open(self.startplugin['runinfo']['results_dir'] + '/progress_block.html', 'w') as html_handle:
                html_handle.write('<html><body>')
                html_handle.write("The current progress is %d of %d" %(current_progress, max_progress))
                html_handle.write('</body></hmtl>')
    ...


.. _plugin_templating:

Rendering Templates
-------------------

When outputting HTML files, using templates can be cleaner than assembling long stings. Below is an example of using `Django templates <https://docs.djangoproject.com/en/1.7/topics/templates/>`_.
This example uses an HTML template named *progress_block_template.html* inside a *templates* directory inside the plugins root directory.

::

    from django.conf import settings
    from django.template.loader import render_to_string

    settings.configure(TEMPLATE_DIR=self.startplugin["runinfo"]["plugin"]["path"] + '/templates')

    with open(self.startplugin['runinfo']['results_dir'] + '/progress_block.html', 'w') as html_handle:
        html_handle.write(render_to_string("progress_block_template.html", {"current_progress": 54}))

