Process Dataframe Column
========================

Process Date Column
--------------------

**Functions**
## function: parse_dates()
The ``parse_dates()`` function is designed to parse date columns in a Pandas DataFrame. It provides flexibility by allowing users to specify a date format or automatically extracting the format from an error message. You can use the :func: ``df_csv_excel.read_data.parse_dates`` function.

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


Process JSON Data in DataFrame
--------------------
.. function:: get_feature_from_json(df, json_column_name, key_names)

  The :func: ``get_feature_from_json`` extracts the value of a nested key in a JSON string column of a Pandas DataFrame.

  :param df: The DataFrame containing the JSON column.
  :type df: :class:`pandas.DataFrame`

  :param json_column_name: The name of the column containing JSON strings.
  :type json_column_name: :class:`str`

  :param key_names: A list of keys to navigate through the JSON structure.
  :type key_names: :class:`list`

  :return: If successful, the function adds a new column ('json_feature') to the DataFrame, containing the extracted values.
           If an error occurs during processing (JSONDecodeError, TypeError, KeyError), it returns `None`.
  :rtype: :class:`numpy.ndarray`

**Examples**

Example 1: Extracting features from a JSON column   

.. code-block:: python

   from df_csv_excel import read_data

   # Example DataFrame
   data = {'json_column': ['{"a": {"b": {"c": 42}}}', '{"a": {"b": {"c": 24}}}']}
   df = pd.DataFrame(data)

   # Extract features
   result = read_data.get_feature_from_json(df, 'json_column', ['a', 'b', 'c'])

   # Resulting DataFrame
   #    json_column  json_feature
   # 0  {"a": {"b": {"c": 42}}}           42
   # 1  {"a": {"b": {"c": 24}}}           24

.. note::

- The functions use the :mod:`json` module to handle JSON parsing.
- If an error occurs during processing, the corresponding value in the result column is set to `None`.


