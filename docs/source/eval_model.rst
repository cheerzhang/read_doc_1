Model Evaluation
========================


Evaluate Binary Classification Performance
-----------------------------------------

.. function:: binary_classification_eval(df, true_column, predict_column)

   Evaluate binary classification performance.

   :param df: DataFrame containing the true and predicted labels.
   :type df: pandas.DataFrame

   :param true_column: Name of the column containing true class labels.
   :type true_column: str

   :param predict_column: Name of the column containing predicted class labels.
   :type predict_column: str

   :return: Dictionary containing evaluation metrics.
   :rtype: dict

   :raises AssertionError: If specified columns are not found in the DataFrame.

   This function computes common binary classification evaluation metrics, including accuracy, precision, recall, F1 score, confusion matrix, KS statistic, and Gini coefficient.

   Example
   -------

   .. code-block:: python

      from df_csv_excel.eval_model import binary_classification_eval

      result = binary_classification_eval(df, 'true_labels', 'predicted_labels')
      print(result)

   Metrics Included:

    - Confusion Matrix
    - Accuracy
    - Precision
    - Recall
    - F1 Score
    - KS Statistic
    - Gini Coefficient

