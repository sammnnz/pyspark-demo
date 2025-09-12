FROM quay.io/jupyter/pyspark-notebook:spark-3.5.3

WORKDIR /home/jovyan/work

COPY pyproject.toml README.md ./

RUN pip install --upgrade pip
RUN pip install poetry==2.1.2
RUN poetry config virtualenvs.create false
RUN poetry lock
RUN poetry install --no-interaction --no-root --with test
