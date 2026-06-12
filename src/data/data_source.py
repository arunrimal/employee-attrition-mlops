# data_source.py
from feast import FileSource

attrition_source = FileSource(
    path="../data/processed/employee_attrition.parquet",
    timestamp_field="event_timestamp"   # feast needs a time column (added by prepare_feast_data.py)
)