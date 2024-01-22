Process Dataframe Column
=====


Process Date Column
------------

The `parse_dates` function is designed to parse date columns in a Pandas DataFrame. It provides flexibility by allowing users to specify a date format or automatically extracting the format from an error message:



Example 1: Parsing dates with default settings

.. code-block:: console

   (.venv) $ from df_csv_excel import read_data
   (.venv) $ df['date_column'] = read_data.parse_dates(df, 'date_column')


Example 2: Parsing dates with a specified format

.. code-block:: console

   (.venv) $ from df_csv_excel import read_data
   (.venv) $ df['date_column'] = read_data.parse_dates(df, 'date_column', format='%d/%m/%Y %H:%M:%S')


