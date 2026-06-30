from enum import Enum

from pydantic import BaseModel, ConfigDict


class RunMode(str, Enum):
    LOCAL = "local"
    CI = "ci"


class ExecutionConfig(BaseModel):
    model_config = ConfigDict(frozen=True)

    run_mode: RunMode
    default_timeout_ms: int
    navigation_timeout_ms: int
    retry_count: int