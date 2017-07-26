Plugin Reference
=============

.. class:: ion.plugin.IonPlugin(*args, **kwargs)

	.. method:: barcodetable_columns()

	.. method:: barcodetable_data(data, planconfig={}, globalconfig={})

	.. attribute:: depends=[]

	.. attribute:: features=[]

	.. method:: generate_output()

	.. method:: getUserInput()

	.. method:: get_restobj(resource, params={}, timeout=30, attempts=5)

	.. method:: launch(data=None)

	.. method:: launch_wrapper(data=None, dry_run=True)

	.. attribute:: log=<logging.Logger object at 0x7ff9186abb10>

	.. attribute:: major_block=False

	.. attribute:: name=None

	.. attribute:: output={}

	.. method:: post_block(block)

		Mark block as processed 

	.. method:: post_launch()

	.. method:: pre_block(block)

		Return value indicates if block will be called 

	.. method:: pre_launch(data=None)

		Code invoked prior to submission to queue.
		Return value determines if launch will be invoked.

	.. attribute:: requires=['BAM']

	.. attribute:: results={}

	.. attribute:: runlevels=[]

	.. attribute:: runtypes=[]

	.. attribute:: startplugin=<property object at 0x7ff9186a6a48>

	.. attribute:: version=None

.. class:: ion.plugin.RunLevel

	T.__new__(S, ...) -> a new object with type S, a subtype of T

	.. attribute:: BLOCK

	.. attribute:: DEFAULT

	.. attribute:: LAST

	.. attribute:: POST

	.. attribute:: PRE

	.. attribute:: SEPARATOR

.. class:: ion.plugin.RunType

	T.__new__(S, ...) -> a new object with type S, a subtype of T

	.. attribute:: COMPOSITE

	.. attribute:: FULLCHIP

	.. attribute:: THUMB

.. class:: ion.plugin.Feature

	T.__new__(S, ...) -> a new object with type S, a subtype of T

	.. attribute:: EXPORT

