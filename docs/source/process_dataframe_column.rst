Process Dataframe Column
========================

Process Date Column
--------------------

The :func: ``parse_dates`` function is designed to parse date columns in a Pandas DataFrame. It provides flexibility by allowing users to specify a date format or automatically extracting the format from an error message. You can use the :func: ``df_csv_excel.read_data.parse_dates`` function.

.. autofunction:: df_csv_excel.read_data.parse_dates

**Parameters**

- **df** (:class: `pandas.DataFrame`)
  The dataframe that includes the date column.

- **date_column_name** (:class: `str`)
  The name of the date column.

- **format** (:class: `str`, optional)
  The format of the date column, for example, ``%d/%m/%Y %H:%M:%S``.

**Examples**

Example 1: Parsing dates with default settings

.. code-block:: python

   from df_csv_excel import read_data

   # Parsing dates with default settings
   df['date_column'] = read_data.parse_dates(df, 'date_column')

Example 2: Parsing dates with a specified format

.. code-block:: python

   from df_csv_excel import read_data

   # Parsing dates with a specified format
   df['date_column'] = read_data.parse_dates(df, 'date_column', format='%d/%m/%Y %H:%M:%S')
