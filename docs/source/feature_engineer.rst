Feature Engineering
========================

Check Significant Association with Chi_square
------------------------

This function checks for a significant association between a specified categorical feature and a binary target in a pandas DataFrame using the Chi-Square test. It returns `True` if there is a significant association and `False` if the variables are independent. The significance level for the Chi-Square test is controlled by the `alpha` parameter.
s

.. function:: significant_association_chi_square(df, column_category, column_target, alpha=0.05)

   Check for significant association between a categorical feature and a binary target using the Chi-Square test.

   :param df: The pandas DataFrame containing the data.
   :type df: :class:`pandas.DataFrame`

   :param column_category: The name of the categorical feature column.
   :type column_category: :class:`str`

   :param column_target: The name of the binary target column.
   :type column_target: :class:`str`

   :param alpha: The significance level for the Chi-Square test.
   :type alpha: :class:`float`, optional, default: 0.05

   :return: True if there is a significant association, False if the variables are independent.
   :rtype: :class:`bool`

   :raises ValueError: If one or more specified columns are not found in the DataFrame.

Example

   .. code-block:: python

      from from df_csv_excel.fe_functions import significant_association_chi_square

      # Assuming 'df' is your DataFrame
      result = significant_association_chi_square(df, column_category='category', column_target='target')


   