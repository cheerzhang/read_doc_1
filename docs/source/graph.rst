graph
========================

Plot Pie Chart
------------------------

Plot a pie chart based on specified label_column values.

.. function:: plot_pie_chart(df, label_column, diff_data=[0, 1], diff_labels=['Good', 'Bad'], autopct='%1.1f%%', startangle=90)

   Plot a pie chart to visualize the distribution of categorical values in the specified column.

   :param df: pandas.DataFrame
       The input DataFrame.
   :type df: :class:`pandas.DataFrame`

   :param label_column: str
       The name of the column containing categorical values for which the pie chart is created.
   :type label_column: str

   :param diff_data: list, optional (default=[0, 1])
       The unique values from the `label_column` for which the pie chart is generated.
   :type diff_data: list

   :param diff_labels: list, optional (default=['Good', 'Bad'])
       Labels corresponding to the unique values in diff_data.
   :type diff_labels: list

   :param autopct: str, optional (default='%1.1f%%')
       Format for displaying the percentage contribution of each category.
   :type autopct: str

   :param startangle: float, optional (default=90)
       The angle by which the start of the pie chart is rotated.
   :type startangle: float

   :return: matplotlib.figure.Figure
       The created matplotlib figure.

   :return: pandas.Series
       A Series containing counts of occurrences for each unique value in label_column.

   Example:
   
    .. code-block:: python
        
        from df_csv_excel.plot_data import plot_pie_chart
        
        fig, options = plot_pie_chart(df, 'label')

