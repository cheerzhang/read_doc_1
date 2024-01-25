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



Calculate Jaccard similarity
------------------------

.. function:: get_similarity(df, column_str_1, column_str_2)

   This function is to calculate Jaccard similarity scores between two specified columns in a DataFrame.
   
   :param df: The input DataFrame.
   :type df: pandas.DataFrame

   :param column_str_1: The name of the first column.
   :type column_str_1: str

   :param column_str_2: The name of the second column.
   :type column_str_2: str

   :return: An array of Jaccard similarity scores.
   :rtype: numpy.ndarray

   :raises ValueError: If the DataFrame is empty or if one or more specified columns are not found.


   Example:

   .. code-block:: python

      from df_csv_excel.fe_functions import get_similarity

      score = get_similarity(df, column_str_1='column1', column_str_2='column2')


   .. note::

      The Jaccard similarity is calculated by comparing the unique values in the specified columns. It is a
      measure of the similarity between the sets of values in the two columns.
      A score of 0 indicates no similarity, and a score of 1 indicates complete similarity.


Calculate Information Value (IV)
--------------------------------

.. function:: calculate_iv(data, feature, target, num_bins=10)

   This function calculates the Information Value (IV) for a given feature in a binary classification task.

   :param data: DataFrame containing the feature and target columns.
   :type data: pandas.DataFrame

   :param feature: Name of the feature column.
   :type feature: str

   :param target: Name of the target column.
   :type target: str

   :param num_bins: Number of bins to discretize the continuous feature.
   :type num_bins: int, optional, default: 10

   :return: Information Value (IV) for the feature, pivot table, and a bar chart.
   :rtype: Tuple[float, pandas.DataFrame, matplotlib.pyplot]

   :raises ValueError: If the DataFrame is empty or if one or more specified columns are not found.

   This function discretizes the continuous feature into bins, calculates Weight of Evidence (WoE) and IV, and
   returns the overall IV.

   The formula for IV is:

   .. math::

       IV = \sum_{i} \left( \text{WoE}_i \cdot (\text{good\_percentage}_i - \text{bad\_percentage}_i) \right)

   where WoE (Weight of Evidence) is given by:

   .. math::

       \text{WoE}_i = \ln\left(\frac{\text{good\_percentage}_i + \epsilon}{\text{bad\_percentage}_i + \epsilon}\right)

   and \(\epsilon\) is a small constant added to avoid division by zero.

   The IV indicates the predictive power of the feature:

      - IV < 0.02: Weak predictor   
      - 0.02 <= IV < 0.1: Medium predictor   
      - IV >= 0.1: Strong predictor   

   Example:

   .. code-block:: python

      from df_csv_excel.fe_functions import calculate_iv

      total_iv, pivot_table, plt = calculate_iv(data, 'age', 'label', custom_bins=[0, 20, 40, 60, 80, 100])

   .. note::

      Adjust the value of `num_bins` based on your specific requirements and the characteristics of your data.

   .. warning::

      Ensure that the specified feature and target columns exist in the DataFrame to avoid errors.

   The function also returns a pivot table containing counts and percentages for each bin and target label, as well as a bar chart
   visualizing the counts for each bin and label.

   .. image:: _static/calculate_iv_example.png
      :width: 600
      :alt: calculate_iv_example.png text

      Example Bar Chart of Counts for Each Bin and Label.

