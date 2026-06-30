from enum import Enum

from pydantic import BaseModel, ConfigDict


class ArtifactRetainPolicy(str, Enum):
    ON_FAILURE = "on_failure"
    ALWAYS = "always"
    NEVER = "never"


class ReportingConfig(BaseModel):
    model_config = ConfigDict(frozen=True)

    screenshots_enabled: bool
    videos_enabled: bool
    traces_enabled: bool
    html_report_enabled: bool
    retain_policy: ArtifactRetainPolicy