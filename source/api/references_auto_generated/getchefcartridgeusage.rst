.. _api_reference_getchefcartridgeusage:

Get Chef Cartridgeusage Resource
================================

| Resource URL ``http://mytorrentserver/rundb/api/v1/getchefcartridgeusage/``
| Schema URL ``http://mytorrentserver/rundb/api/v1/getchefcartridgeusage/schema/``
| 

.. include:: ../references_manual_extras/getchefcartridgeusage.rst

Resource Fields
---------------

============================== =================================================================================================================================================== ======= ======== ======== ===== ====== =========== 
field                          help text                                                                                                                                           default nullable readonly blank unique type        
============================== =================================================================================================================================================== ======= ======== ======== ===== ====== =========== 
**hoursSinceSolutionFirstUse** Integer number of hours between (oldest associated experiment using Solution) and (chefCurrentTime). Rounded down to the nearest hour is OK. Ex: 24 n/a     true     true     true  false  Integer     
------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ----------- 
**numberSolutionSerialUsage**  Integer number. No of Solution cartridge Usage Ex: 2                                                                                                n/a     true     true     true  false  Integer     
------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ----------- 
**errorCodes**                 A lists of data. Ex: ["E200"] or ["W100", "W200"]                                                                                                   n/a     true     true     true  false  List Object 
------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ----------- 
**allowRunToContinue**         Boolean string data. Ex: "true or false"                                                                                                            n/a     true     true     true  false  boolean     
------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ----------- 
**detailMessages**             A dictionary of data. Ex: {'E300': 'No. of reagent and solution usage do not match'}                                                                n/a     true     true     true  false  dict        
------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ----------- 
**numberReagentSerialUsage**   Integer number. No of Reagent cartridge Usage Ex: 2                                                                                                 n/a     true     true     true  false  Integer     
------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------- ------- -------- -------- ----- ------ ----------- 
**hoursSinceReagentFirstUse**  Integer number of hours between (oldest associated experiment using Reagent) and (chefCurrentTime). Rounded down to the nearest hour is OK. Ex: 48  n/a     true     true     true  false  Integer     
============================== =================================================================================================================================================== ======= ======== ======== ===== ====== =========== 

Example Response
^^^^^^^^^^^^^^^^

.. code-block:: javascript

	{
	    "hoursSinceSolutionFirstUse": "", 
	    "numberSolutionSerialUsage": 0, 
	    "errorCodes": [
	        "E305"
	    ], 
	    "allowRunToContinue": false, 
	    "detailMessages": {
	        "E305": "Missing chef inputs filter option ['chefReagentsSerialNum', 'chefSolutionsSerialNum', 'kitName']"
	    }, 
	    "numberReagentSerialUsage": 0, 
	    "hoursSinceReagentFirstUse": ""
	}

Allowed list HTTP methods
-------------------------

- GET


Allowed detail HTTP methods
---------------------------

None

