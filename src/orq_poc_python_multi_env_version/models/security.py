"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_poc_python_multi_env_version.types import BaseModel
from orq_poc_python_multi_env_version.utils import FieldMetadata, SecurityMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SecurityTypedDict(TypedDict):
    api_key: NotRequired[str]


class Security(BaseModel):
    api_key: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="http",
                sub_type="bearer",
                field_name="Authorization",
            )
        ),
    ] = None