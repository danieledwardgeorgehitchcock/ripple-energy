# Generated by ariadne-codegen on 2023-09-13 00:38
# Source: src/ripple_energy/graphql

from typing import Optional

from .base_model import BaseModel


class Version(BaseModel):
    version: Optional[str]


Version.update_forward_refs()
