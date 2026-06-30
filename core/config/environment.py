from enum import Enum

from pydantic import BaseModel, ConfigDict, HttpUrl


class EnvironmentName(str, Enum):
    LOCAL = "local"
    PRODUCTION = "production"


class EnvironmentConfig(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: EnvironmentName
    base_url: HttpUrl
    api_url: HttpUrl | None = None