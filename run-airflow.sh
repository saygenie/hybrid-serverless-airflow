export AIRFLOW_HOME="$(pwd)"

AIRFLOW_VERSION=2.2.4
PYTHON_VERSION=3.9

pipenv --python "${PYTHON_VERSION}"
pipenv install "apache-airflow==${AIRFLOW_VERSION}"

pipenv run airflow standalone
