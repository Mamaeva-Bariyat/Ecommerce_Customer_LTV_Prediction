# 📦 Customer Value  Prediction for E-Commerce
**📄 Описание проекта:**
Этот проект посвящён исследованию поведения клиентов онлайн-ритейла, прогнозированию Lifetime Value (LTV).
Проект выполнен в исследовательском формате (Research Project)<p>
**Основные задачи:**
- Предобработка данных (чистка, обработка пропусков, преобразование признаков).
- Feature Engineering: создание RFM-признаков, среднего чека, интервалов между заказами, LTV.
- Моделирование: Ridge, CatBoost, LGBM, Stacking.
- Интерпретация моделей: важность признаков.
- Финальные выводы по сегментам клиентов и бизнес-инсайты.<p>

  **📂 Структура проекта:**
```project/
│
├── data/                  # Папка для данных (пустая в GitHub)
│  
│
├── notebooks/             # Jupyter ноутбуки с этапами анализа
│   ├── 1.LTV_Preprocessed_data.ipynb
│   ├── 2.0.LTV_EDA.ipynb
|   ├── 2.1.LTV_reviews_geo_clustering
|   ├── 2.2.LTV_text_clustering_reviews
│   ├── 3.LTV_feature_engineering.ipynb
│   ├── 4.LTV_ modeling_with_optuna_stacking.ipynb
│ 
│
├── src/                   # Скрипты Python
│   ├── utils.py           # Вспомогательные функции
│   ├── modeling.py        # Запуск и обучение моделей
│
├── requirements.txt       # Зависимости Python
├── download_data.py       # Скрипт для загрузки данных с Kaggle
├── .gitignore             # Файлы/папки, игнорируемые Git
└── README.md              # Описание проекта
```
# 📥 Установка и запуск
1️⃣ Клонирование репозитория<p>
```
git clone https://github.com/username/project.git
cd project
```
2️⃣ Установка зависимостей<p>
```
pip install -r requirements.txt
```
3️⃣ Загрузка данных<p>
Проект использует датасет с Kaggle. Перед запуском ноутбуков его нужно скачать.
Установите ```Kaggle CLI.```
Скачайте датасет:
```python download_data.py```
Файл будет сохранён в data/.<p>
4️⃣ Запуск ноутбуков
```jupyter notebook.```
Откройте и выполняйте шаги в ноутбуках по порядку.
# 📊 Результаты
**LTV Prediction:** модель LGBM показала лучшие метрики ```(MAE ≈ 3.56, RMSE ≈ 83.29).``` <p>
**Наиболее важные факторы:** ``` monetary, frequency, avg_order_value.```







