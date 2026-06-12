from datetime import timedelta

from feast import Entity, FeatureView, FileSource, Project, Field
from feast.types import Int64, String
from feast.value_type import ValueType

# Define a project for the feature repo
project = Project(name="attrition_feature_store", description="A project for employee attrition")

# Define the employee entity used for feature joins
employee = Entity(
    name="employee_id",
    value_type=ValueType.INT64,
    description="Unique employee identifier",
)

# FileSource for cleaned attrition data. The path is relative to the feature repo root.
attrition_source = FileSource(
    name="attrition_source",
    path="../../data/employee_attrition.parquet",
    timestamp_field="event_timestamp",
)

# Feature view definition for the employee attrition dataset
attrition_features = FeatureView(
    name="attrition_features",
    entities=[employee],
    ttl=timedelta(days=365),
    schema=[
        Field(name="age", dtype=Int64),
        Field(name="gender", dtype=String),
        Field(name="years_at_company", dtype=Int64),
        Field(name="job_role", dtype=String),
        Field(name="monthly_income", dtype=Int64),
        Field(name="work-life_balance", dtype=String),
        Field(name="job_satisfaction", dtype=String),
        Field(name="performance_rating", dtype=String),
        Field(name="number_of_promotions", dtype=Int64),
        Field(name="overtime", dtype=String),
        Field(name="distance_from_home", dtype=Int64),
        Field(name="education_level", dtype=String),
        Field(name="marital_status", dtype=String),
        Field(name="number_of_dependents", dtype=Int64),
        Field(name="job_level", dtype=String),
        Field(name="company_size", dtype=String),
        Field(name="company_tenure", dtype=Int64),
        Field(name="remote_work", dtype=String),
        Field(name="leadership_opportunities", dtype=String),
        Field(name="innovation_opportunities", dtype=String),
        Field(name="company_reputation", dtype=String),
        Field(name="employee_recognition", dtype=String),
    ],
    online=True,
    source=attrition_source,
)
