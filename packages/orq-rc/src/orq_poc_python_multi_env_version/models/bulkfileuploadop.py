"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
import io
from orq_poc_python_multi_env_version.types import BaseModel
from orq_poc_python_multi_env_version.utils import FieldMetadata, MultipartFormMetadata
import pydantic
from typing import IO, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class BulkFileUploadFilesTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]


class BulkFileUploadFiles(BaseModel):
    file_name: Annotated[
        str, pydantic.Field(alias="files"), FieldMetadata(multipart=True)
    ]

    content: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(content=True)),
    ]

    content_type: Annotated[
        Optional[str],
        pydantic.Field(alias="Content-Type"),
        FieldMetadata(multipart=True),
    ] = None


BulkFileUploadPurpose = Literal["retrieval"]
r"""The intended purpose of the uploaded file."""


class BulkFileUploadRequestBodyTypedDict(TypedDict):
    files: List[BulkFileUploadFilesTypedDict]
    purpose: BulkFileUploadPurpose
    r"""The intended purpose of the uploaded file."""


class BulkFileUploadRequestBody(BaseModel):
    files: Annotated[List[BulkFileUploadFiles], FieldMetadata(multipart=True)]

    purpose: Annotated[BulkFileUploadPurpose, FieldMetadata(multipart=True)]
    r"""The intended purpose of the uploaded file."""


BulkFileUploadFilesPurpose = Literal["retrieval"]
r"""The intended purpose of the uploaded file."""


class ResponseBodyTypedDict(TypedDict):
    id: str
    object_name: str
    r"""path to the file in the storage"""
    purpose: BulkFileUploadFilesPurpose
    r"""The intended purpose of the uploaded file."""
    bytes: float
    file_name: str
    created: NotRequired[datetime]
    r"""The date and time the resource was created"""


class ResponseBody(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]

    object_name: str
    r"""path to the file in the storage"""

    purpose: BulkFileUploadFilesPurpose
    r"""The intended purpose of the uploaded file."""

    bytes: float

    file_name: str

    created: Optional[datetime] = dateutil.parser.isoparse("2024-11-25T11:22:28.171Z")
    r"""The date and time the resource was created"""
