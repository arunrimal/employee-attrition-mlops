import subprocess
from datetime import datetime

import pandas as pd

from feast import FeatureStore


def run_demo():
    store = FeatureStore(repo_path=".")
    print("--- Run feast apply ---")
    subprocess.run(["feast", "apply"], check=True)

    print("--- Historical features for training ---")
    fetch_historical_features_entity_df(store, for_batch_scoring=False)

    print("--- Historical features for batch scoring ---")
    fetch_historical_features_entity_df(store, for_batch_scoring=True)

    print("--- Load features into online store ---")
    store.materialize_incremental(end_date=datetime.now())

    print("--- Online features ---")
    fetch_online_features(store)

    print("--- Run feast teardown ---")
    subprocess.run(["feast", "teardown"], check=True)


def fetch_historical_features_entity_df(store: FeatureStore, for_batch_scoring: bool):
    entity_df = pd.DataFrame(
        {
            "employee_id": [1, 2, 3],
            "event_timestamp": [
                datetime(2024, 1, 1, 0, 0, 0),
                datetime(2024, 1, 2, 0, 0, 0),
                datetime(2024, 1, 3, 0, 0, 0),
            ],
        }
    )
    if for_batch_scoring:
        entity_df["event_timestamp"] = pd.to_datetime("now", utc=True)

    training_df = store.get_historical_features(
        entity_df=entity_df,
        features=[
            "attrition_features:age",
            "attrition_features:monthly_income",
        ],
    ).to_df()
    print(training_df.head())


def fetch_online_features(store):
    entity_rows = [{"employee_id": 1}, {"employee_id": 2}]
    returned_features = store.get_online_features(
        features=["attrition_features:age", "attrition_features:monthly_income"],
        entity_rows=entity_rows,
    ).to_dict()
    for key, value in sorted(returned_features.items()):
        print(key, " : ", value)


if __name__ == "__main__":
    run_demo()
