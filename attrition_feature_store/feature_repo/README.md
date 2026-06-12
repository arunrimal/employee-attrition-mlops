# Feast feature repo for Employee Attrition

This directory contains Feast feature definitions for the employee attrition project.

Quick steps to use this feature repo (run from this folder or set `repo_path` accordingly):

1. Install Feast and runtime deps (if not already):

```bash
pip install feast
```

2. Apply the feature definitions to register them:

```bash
# from the feature repo folder
feast apply
```

3. Materialize historical features into the offline store (for training):

```bash
# materialize features for a time range
feast materialize 2024-01-01T00:00:00 2026-12-31T23:59:59
# or incremental
feast materialize-incremental
```

4. (Optional) Populate / configure an online store to serve features in low-latency:

- For local development, Redis is a common choice. Configure `feature_repo/feature_repo.yaml` (or `feature_store.yaml`) to point to your Redis instance.
- Start Redis locally (example using Docker):

```bash
docker run -d --name feast-redis -p 6379:6379 redis:6
```

- After configuring, materialize the features into the online store:

```bash
feast materialize-incremental
```

5. Using the store from training or serving code:

```python
from feast import FeatureStore
store = FeatureStore(repo_path=".")

# Training: historical features (entity_df must contain `event_timestamp` and entity keys)
training_df = store.get_historical_features(entity_df=entity_df, features=["attrition_features:age"]).to_df()

# Serving: online features
features = store.get_online_features(features=["attrition_features:age"], entity_rows=[{"employee_id": 1001}]).to_dict()
```

Operational notes:
- Ensure that the `entity_df` you pass to `get_historical_features` contains an `event_timestamp` column (pandas datetime) and the entity join keys.
- If you want the latest feature values for batch scoring, set `event_timestamp` to `pd.to_datetime('now')` for each row (or the desired scoring time).
- For production serving, ensure an online store (Redis/Redis Cluster) is accessible to the serving process and that the features have been materialized/pushed to the online store.

See Feast docs for full configuration options: https://docs.feast.dev/
