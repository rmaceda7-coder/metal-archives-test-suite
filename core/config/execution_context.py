from pydantic import BaseModel, ConfigDict

from core.config.accessibility import AccessibilityConfig
from core.config.browser import BrowserConfig
from core.config.environment import EnvironmentConfig
from core.config.execution import ExecutionConfig
from core.config.reporting import ReportingConfig


class ExecutionContext(BaseModel):
    model_config = ConfigDict(frozen=True)

    environment: EnvironmentConfig
    execution: ExecutionConfig
    browser: BrowserConfig
    reporting: ReportingConfig
    accessibility: AccessibilityConfig