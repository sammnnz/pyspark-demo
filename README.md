# pyspark-demo

Демо проект для PySpark.
Посмотреть результат можно в [pyspark.ipynb](https://github.com/sammnnz/pyspark-demo/blob/main/pyspark.ipynb).

# Features

- `get_all_rows_joins_unsafe` - функция принимающая 2 целевых датафрейма, связующий датафрейм и названия "pk" столбцов. Возврашает все "связанные" строки относительно одного из целевых датафреймов (в зависимости от аргумента `mode`).

## Dev
~~~~shell
git clone https://github.com/sammnnz/pyspark-demo.git
cd pyspark-demo
docker compose up spark
~~~~
Далее `Attach to Running Container` в VSCode.
