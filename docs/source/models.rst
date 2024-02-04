Models
====================

AnomalyDetectionModel
------------------------

Anomaly Detection Model using Gaussian Distribution.

    This class provides a simple implementation of an anomaly detection model
    based on the Gaussian distribution. It includes methods for estimating
    Gaussian parameters, calculating p-values, selecting the threshold, and making predictions.

    .. function:: train(X_train, X_val, y_val)

        Train the model.

        :param X_train: Training data matrix.
        :type X_train: ndarray

        :param X_val: Validation data matrix.
        :type X_val: ndarray

        :param y_val: Ground truth labels for validation data.
        :type y_val: ndarray

    .. function:: predict(X)

        Predict anomalies in the input data.

        :param X: Data matrix for prediction.
        :type X: ndarray

    Example
    -------
    Create an instance of the `AnomalyDetectionModel` and train it using a training dataset. Then, predict anomalies in a validation dataset.

    .. code-block:: python

        from df_csv_excel.models import AnomalyDetectionModel  # Replace 'your_module' with the actual module name

        # Load your datasets (X_train, X_val, y_val)
        # ...

        # Create an instance of AnomalyDetectionModel
        model = AnomalyDetectionModel()

        # Train the model
        model.train(X_train, X_val, y_val)

        # Predict anomalies in the validation dataset
        anomalies = model.predict(X_val)

        print(anomalies)

    .. note::
        The anomaly detection model assumes that the input data follows a Gaussian distribution.

    .. warning::
        This class is designed for educational purposes and may not be suitable for all types of data.