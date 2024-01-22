Usage
=====

.. _installation:

Installation
------------

To use read_csv_excel, first install it using pip:

.. code-block:: console

   (.venv) $ pip install read-csv-excel

Load dataframe from file
----------------

To read dataframe from csv or excel file,
you can use the ``df_csv_excel.read_data.read_data_by_path()`` function:

.. function:: df_csv_excel.read_data.read_data_by_path(file_path)

The ``file_path`` parameter should be either ``".csv"``
or ``"xlsx"``. Otherwise, :py:func:`df_csv_excel.read_data.read_data_by_path`
will raise an exception.   

   :param file_path: The file name to be load.   

For example:

>>> from df_csv_excel import read_data
>>> df = read_data.read_data_by_path('a.xlsx')

