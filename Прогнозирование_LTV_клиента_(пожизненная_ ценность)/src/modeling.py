#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate_model(model, X_train, y_train, X_test, y_test):
    """Обучает модель и считает MAE и RMSE"""
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    return mae, rmse

def print_results(results):
    """Печатает таблицу с результатами"""
    print("\nРезультаты моделей:")
    print("Model\tMAE\tRMSE")
    for name, metrics in results.items():
        print(f"{name}\t{metrics['MAE']:.4f}\t{metrics['RMSE']:.4f}")

