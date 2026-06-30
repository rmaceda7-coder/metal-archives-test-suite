from pydantic import BaseModel, ConfigDict


class AccessibilityConfig(BaseModel):
    model_config = ConfigDict(frozen=True)

    enabled: bool
    keyboard_validation_enabled: bool
    focus_validation_enabled: bool
    aria_validation_enabled: bool
    axe_enabled: bool