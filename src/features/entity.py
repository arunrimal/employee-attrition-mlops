# entity.py
from feast import Entity
from feast.value_type import ValueType

employee = Entity(
    name="employee_id",
    value_type=ValueType.INT64,
    description="unique employee identifier"
)