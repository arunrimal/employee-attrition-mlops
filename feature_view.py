# feature_view.py
from feast import FeatureView, Feature, ValueType
from datetime import timedelta

attrition_fv = FeatureView(
    name="attrition_features",
    entities=["employee_id"],
    ttl=timedelta(days=365),      # how long features are valid
    features=[
        Feature(name="age",                      dtype=ValueType.INT64),
        Feature(name="gender",                   dtype=ValueType.STRING),
        Feature(name="years_at_company",         dtype=ValueType.INT64),
        Feature(name="job_role",                 dtype=ValueType.STRING),
        Feature(name="monthly_income",           dtype=ValueType.INT64),
        Feature(name="work_life_balance",        dtype=ValueType.STRING),
        Feature(name="job_satisfaction",         dtype=ValueType.STRING),
        Feature(name="performance_rating",       dtype=ValueType.STRING),
        Feature(name="number_of_promotions",     dtype=ValueType.INT64),
        Feature(name="overtime",                 dtype=ValueType.STRING),
        Feature(name="distance_from_home",       dtype=ValueType.INT64),
        Feature(name="education_level",          dtype=ValueType.STRING),
        Feature(name="marital_status",           dtype=ValueType.STRING),
        Feature(name="number_of_dependents",     dtype=ValueType.INT64),
        Feature(name="job_level",                dtype=ValueType.STRING),
        Feature(name="company_size",             dtype=ValueType.STRING),
        Feature(name="company_tenure",           dtype=ValueType.INT64),
        Feature(name="remote_work",              dtype=ValueType.STRING),
        Feature(name="leadership_opportunities", dtype=ValueType.STRING),
        Feature(name="innovation_opportunities", dtype=ValueType.STRING),
        Feature(name="company_reputation",       dtype=ValueType.STRING),
        Feature(name="employee_recognition",     dtype=ValueType.STRING),
    ],
    source=attrition_source
)