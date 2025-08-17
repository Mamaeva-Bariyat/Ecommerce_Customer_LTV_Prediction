#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import kaggle

# Параметры
DATASET = "olistbr/brazilian-ecommerce"  
RAW_DATA_PATH = "data/raw"

def download_kaggle_dataset(dataset: str, path: str):
    os.makedirs(path, exist_ok=True)
    kaggle.api.dataset_download_files(dataset, path=path, unzip=True)
    print(f"Датасет {dataset} скачан в {path}")

if __name__ == "__main__":
    download_kaggle_dataset(DATASET, RAW_DATA_PATH)


