from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class InputHandling(str, Enum):
    none = "none"
    basic = "basic"
    strict = "strict"

class DBMS(str, Enum):
    mysql = "mysql"
    postgresql = "postgresql"
    oracle = "oracle"
    mssql = "mssql"
    other = "other"

class Component(BaseModel):
    name: str
    type: Optional[str] = Field(None, description="Type of the component (e.g., web_server, database, api, application)")
    requires_authentication: Optional[bool] = Field(False, description="Does this component require authentication?")
    authentication: Optional[bool] = Field(False, description="Is authentication properly enabled?")
    sensitive_data: Optional[bool] = Field(False, description="Does this component handle sensitive data?")
    encryption: Optional[bool] = Field(False, description="Is the data encrypted?")
    input_handling: InputHandling = Field(InputHandling.none, description="Input validation level")
    tags: Optional[List[str]] = Field(default_factory=list, description="Additional tags for the component")
    dbms: Optional[DBMS] = Field(None, description="Database management system used, if applicable")
    prepared_statements: Optional[bool] = Field(False, description="Whether prepared statements are used (for databases)")
    exposed: Optional[bool] = Field(False, description="Whether the component is externally accessible")
    description: Optional[str] = Field(None, description="Additional context or notes about the component")
