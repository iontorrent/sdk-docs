Write a Web Service Client
==========================

You can use the REST API to write a web service client.

Topics on this page:

* :ref:`Getting_a_list_of_experiments`
* :ref:`Displaying_results_data`
* :ref:`CSS_used_in_these_examples`

Some application environments have timing complexities that make a simple request-response communication paradigm undesirable. A non-deterministic, blocking protocol, like HTTP, may take a long time to complete, causing connections to time out or degraded application performance. Using AJAX, you can achieve the asynchronous behavior needed for such applications.

These examples uses the jQuery library to show how to set up and make a REST API call and handle the pending response. The first example simply lists all experiments on the server, sorted by date. The second example uses the experiment resource link to the results data for the experiment to also display all analysis results for the experiment. (The CSS code is only provided to show the UI presentation mechanism used in the examples.)

Because JavaScript prevents data requests to servers in a different domain, the JSONP data format is used handle this limitation.

Building on the fundamental procedures shown in these examples, you might easily modify the application to also monitor the status of a run and report when analysis processing has completed. Such an application could be implemented on a mobile device to allow remote monitoring and real-time notification.

	(!) The sample JavaScript code has been tested with the Chrome 11 and Firefox 3.6 browsers.

.. _Getting_a_list_of_experiments:

Get a list of experiments
-------------------------

The first example is to display the list of experiments, including the run date and the PGM™ or Proton™ Sequencer name.

.. image:: ../images/ts_writingawebserviceclient_webapp00.png

The HTML is simply a <div> tag encapsulating the display. The JavaScript functions write data to the element whose id is mainPage.

.. code-block:: html

	<div id="mainPage"></div>

The JavaScript uses the jQuery library.

.. code-block:: javascript

	<script type="text/javascript" src="http://code.jquery.com/jquery-1.6.min.js"></script>

On loading the HTML page, a jQuery AJAX function sets up the request for experiment data:

* The URL is set to the URI for the ﻿experiment resource.
* The data type is set to jsonp to handle JavaScript cross-domain restrictions.
* A function is defined to handle the response from the server.

.. code-block:: javascript

	$(function(){
		$.ajax({
			url: "http://myusername:mypassword@myhost/rundb/api/v1/experiment \
				 ?format=jsonp&order_by=date",
			dataType: 'jsonp',
			success: function(json_results){
				$('#mainPage').append('<table class="expTable">
									   <tr><th>Experiment</th>
										<th>Date</th>
										<th>PGM</th></table>');
				listItems = $('#mainPage').find('table');
				$.each(json_results.objects, function(key) {
					html =  '<td>' + json_results.objects[key].expName + '</td>';
					html += '<td class="expTableCol">' + \
							json_results.objects[key].date + '</td>' ;
					html += '<td class="expTableCol">' + \
							json_results.objects[key].pgmName + '</td>' ;
					listItems.append('<tr class="expTableRow">'+html+'</tr>');
				});
			}
		});
	});

Within the ``id=mainPage`` element, the response handling function constructs an HTML table and populates the cells with the following experiment resource fields, for each element returned in the response:

* ``expName``, the experiment name.
* ``date``, the date of the experiment.
* ``pgmName``, the name of the PGM sequencer where the experiment was run.

.. _Displaying_results_data:

Display results data
-----------------------

The previous example is now extended to include the location of results data associated with the experiment. This might be useful for monitoring run status.

.. image:: ../images/ts_writingawebserviceclient_webapp01.png

Further, by clicking on the results link in the table, results metadata are displayed:

.. image:: ../images/ts_writingawebserviceclient_webapp02.png

The JavaScript code snippet is the same as the previous example with the addition of a loop to get all of the results for an experiment and display them in the *results* column.

Notice that the results table entry includes an onClick event handler, which call the showResult function to display results metadata, passing the results location from the results field as a parameter.

.. code-block:: javascript

	$(function(){
		$.ajax({
			url: "http://myusername:mypassword@myhost/rundb/api/v1/experiment \
				  ?format=jsonp&order_by=date",
			dataType: 'jsonp',
			success: function(json_results){
				$('#mainPage').append('<table class="expTable">
									   <tr><th>Experiment</th>
										   <th>Date</th><th>PGM</th>
										   <th>Results</th></table>');
				listItems = $('#mainPage').find('table');
				$.each(json_results.objects, function(key) {
					html =  '<td>' + json_results.objects[key].expName + '</td>';
					html += '<td class="expTableCol">' + \
							json_results.objects[key].date + '</td>' ;
					html += '<td class="expTableCol">' + \
							json_results.objects[key].pgmName + '</td>' ;
					html += '<td class="expTableCol">' ;
			for (var result in json_results.objects[key].results)
			{
				resultPath = json_results.objects[key].results[result];
				resultId = resultPath.split('/');
				html += '<a href="#" onClick= \
									 "showResult(' + resultId[5] + '); \
									 return false;">' + resultPath + '</a><br>';
			}
					html += '</td>' ;
					listItems.append('<tr class="expTableRow">'+html+'</tr>');
				});
			}
		});
	});

The call to ``showResult`` constructs an AJAX GET request, including the ``results`` field parameter in the URI and, again, specifying a jsonp data type.

.. code-block:: javascript

	function showResult(resultLocation) {
	/\*	alert("resultLocation: " + resultLocation)  \*/
	
		$.ajax({
			url: "http://myusername:mypassword@myhost/rundb/api/v1/results/" + \
				  resultLocation + "?format=jsonp",
			dataType: 'jsonp',

When a successful response is received from the server, the response handler constructs a table of metadata in the mainPage element.

The following results resource fields are appended to the table:

* ``resultsName``, the name assigned to the analysis.
* ``timeStamp``, the time of the analysis.
* ``framesProcessed``, the number of frames processed.
* ``processedCycles``, the number of cycles processed.
* ``status``, the analysis status.
* ``timeToComplete``, the time remaining to complete the analysis.

.. code-block:: javascript

	success: function(json_results){
			$('#mainPage').replaceWith('<div id="mainPage"> \
								  <table class="expTable"></table></div>');
			listItems = $('#mainPage').find('table');
			listItems.append('<tr class="expTableRow"> \
									  <td>Results Name</td><td>' + \
									  json_results.resultsName + '</td></tr>');
			listItems.append('<tr class="expTableRow"> \
									  <td>Date</td> \
									  <td>' + json_results.timeStamp + '</td> \
									  </tr>');
			listItems.append('<tr class="expTableRow"> \
									  <td>Frames Processed</td><td>' + \
									  json_results.framesProcessed + '</td> \
									  </tr>');
			listItems.append('<tr class="expTableRow"> \
									  <td>Cycles Processed</td><td>' + \
									  json_results.processedCycles + '</td> \
									  </tr>');
			listItems.append('<tr class="expTableRow"><td>Status</td> \
									  <td>' + json_results.status + '</td></tr>');
			listItems.append('<tr class="expTableRow"> \
									  <td>Time to Complete</td><td>' + \
									  json_results.timeToComplete + '</td></tr>');
			}
		});
	
	}

.. _CSS_used_in_these_examples:

CSS used in these examples
--------------------------

.. code-block:: css

	#mainPage
	{
		background-color: #f9f1cd;
		font-family: Verdana, Geneva, Arial, Helvetica, sans-serif;
	}
	
	ul
	{
		list-style-type: none;
	}
	
	table.expTable
	{
		border:none;
		border-spacing:0px;
		margin-left:25px;
		vertical-align:top;
		padding:0px;
	}
	
	table.expTable th
	{
		border-color: #dddddd;
		border-width: 1px 1px 1px 1px;
		border-style: solid;
		background-color: #333333;
		font-family: Verdana, Geneva, Arial, Helvetica, sans-serif;
		color:#f9f1cd;
		font-size:8pt;
		margin-left:25px;
		padding-right:10px;
		vertical-align:top;
	}
	
	table.expTable td
	{
		border-color: #dddddd;
		border-width: 1px 1px 1px 1px;
		border-style: solid;
		font-family: Verdana, Geneva, Arial, Helvetica, sans-serif;
		color:#666666;
		font-size:8pt;
		margin-left:25px;
		padding-right:10px;
		vertical-align:top;
	}
