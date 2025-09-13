FROM quay.io/jupyter/pyspark-notebook:spark-3.5.3

WORKDIR /home/jovyan/work

COPY pyproject.toml README.md ./

RUN pip install --upgrade pip
RUN pip install poetry==2.1.2
RUN poetry config virtualenvs.create false
RUN poetry lock
RUN mkdir -m 750 -p ./src/pyspark_utils

COPY --chmod=750 ./src/pyspark_utils/ ./src/pyspark_utils

# install only 'pyspark_utils' in editable mode
RUN poetry install --only-root
# install only deps
RUN poetry install --no-root --no-interaction --with test
