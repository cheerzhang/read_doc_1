Process Dataframe Column
========================

Process Date Column
--------------------

.. function:: parse_dates(df, date_column_name, format=None)
  
  The :func:`~parse_dates` function is designed to parse date columns in a Pandas DataFrame. It provides flexibility by allowing users to specify a date format or automatically extracting the format from an error message. You can use the :func:`~df_csv_excel.read_data.parse_dates` function.

  :param df: The DataFrame that includes the date column.
  :type df: :class:`pandas.DataFrame`

  :param date_column_name: The name of the date column.
  :type date_column_name: :class:`str`

  :param format: The format of the date column, for example, ``%d/%m/%Y %H:%M:%S``. Optional, default is None.
  :type format: :class:`str`, optional

  :return: Values of the date column with datetime datatype.
  :rtype: :class:`numpy.ndarray`

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


Example: Extracting features from a JSON column

.. code-block:: python

   from df_csv_excel import read_data

   # Example DataFrame
   data = {'json_column': ['{"a": {"b": {"c": 42}}}', '{"a": {"b": {"c": 24}}}']}
   df = pd.DataFrame(data)

   # Extract features
   df['c_value'] = get_feature_from_json(df, 'json_column', ['a', 'b', 'c'])
   
  

.. note::

   The functions use the :mod:`json` module to handle JSON parsing.
   If an error occurs during processing, the corresponding value in the result column is set to `None`.


Get Latest Row by Column
--------------------

.. function:: get_latest_row_by_column(df, date_column, duplicate_column)
  
   This function retrieves the latest row for each unique value in a specified column based on the values in another date column. It is useful when you have duplicate entries in a DataFrame and want to keep only the rows with the latest date.

   :param df: The input DataFrame.
   :type df: :class:`pandas.DataFrame`

   :param date_column: The name of the date column used for sorting and determining the latest row.
   :type date_column: :class:`str`

   :param duplicate_column: The name of the column containing duplicate values, for which the latest rows will be retained.
   :type duplicate_column: :class:`str`

   :return: A DataFrame containing the latest row for each unique value in the specified duplicate column.
   :rtype: :class:`pandas.DataFrame`

Example

   .. code-block:: python

      from df_csv_excel import read_data

      # Example DataFrame
      data = {'Email': ['john@example.com', 'alice@example.com', 'john@example.com'],
              'created_at': ['2022-01-15', '2022-01-14', '2022-01-16']}

      df = pd.DataFrame(data)

      # Get the latest row for each unique 'Email'
      result = read_data.get_latest_row_by_column(df, 'created_at', 'Email')

.. note::
   
   The input DataFrame is modified in-place during the process.


Get Email Domain and Prefix from Email Column
--------------------

.. function:: get_email_host(df, email_column='email')

   Extract email prefixes and domains from a DataFrame column.

   :param df: The pandas DataFrame containing the email column.
   :type df: :class:`pandas.DataFrame`

   :param email_column: The name of the email column in the DataFrame.
   :type email_column: :class:`str`, optional, default: 'email'

   :return: Tuple of NumPy arrays containing email prefixes and domains.

Example

.. code-block:: python

      from df_csv_excel.read_data import get_email_host

      # Assuming 'df' is your DataFrame
      prefixes, domains = get_email_host(df, email_column='user_email')

This function extracts the email prefixes and domains from a specified column in a pandas DataFrame. It handles empty email cases by setting the 'email_domain' and 'email_prefix' to empty strings in such cases.



.. note::

      This function handles empty email cases by setting the 'email_domain' and 'email_prefix' to empty strings when the email is empty.

   


