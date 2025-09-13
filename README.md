# pyspark-demo

Демо проект для PySpark.
Посмотреть результат можно в [pyspark.ipynb](https://github.com/sammnnz/pyspark-demo/blob/main/pyspark.ipynb).

## Features
[pyspark_utils](https://github.com/sammnnz/pyspark-demo/blob/main/src/pyspark_utils/utils.py):
- `get_all_rows_joins_unsafe` - функция принимающая 2 целевых датафрейма, связующий датафрейм и некоторые другие аргументы. Возврашает все "связанные" строки относительно одного из целевых датафреймов (левого или правого, в зависимости от аргумента `mode`).

## Dev
~~~~shell
git clone https://github.com/sammnnz/pyspark-demo.git
cd pyspark-demo
docker compose up spark-poetry
~~~~
Далее `Attach to Running Container` в VSCode.
