# Config variables. This is generic.
dag_config = Variable.get("covid_daily", deserialize_json=True)
BQ_CONN_ID = dag_config["my_gcp_conn"]
BQ_PROJECT = dag_config["capstone-test"]
BQ_DATASET = dag_config["any_dataset_yourchoice"]