from enum import Enum

from pydantic import BaseModel, ConfigDict


class BrowserType(str, Enum):
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"


class BrowserConfig(BaseModel):
    model_config = ConfigDict(frozen=True)

    browser_type: BrowserType
    headless: bool
    slow_mo_ms: int
    viewport_width: int
    viewport_height: int
    locale: str
    timezone: str