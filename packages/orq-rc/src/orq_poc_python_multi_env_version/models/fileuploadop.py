"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import dateutil.parser
import io
from orq_poc_python_multi_env_version.types import BaseModel
from orq_poc_python_multi_env_version.utils import FieldMetadata, MultipartFormMetadata
import pydantic
from typing import IO, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class FileTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]


class File(BaseModel):
    file_name: Annotated[
        str, pydantic.Field(alias="file"), FieldMetadata(multipart=True)
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


Purpose = Literal["retrieval"]
r"""The intended purpose of the uploaded file."""


class FileUploadRequestBodyTypedDict(TypedDict):
    file: NotRequired[FileTypedDict]
    r"""The file to be uploaded."""
    purpose: NotRequired[Purpose]
    r"""The intended purpose of the uploaded file."""


class FileUploadRequestBody(BaseModel):
    file: Annotated[
        Optional[File],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(file=True)),
    ] = None
    r"""The file to be uploaded."""

    purpose: Annotated[Optional[Purpose], FieldMetadata(multipart=True)] = "retrieval"
    r"""The intended purpose of the uploaded file."""


FileUploadPurpose = Literal["retrieval"]
r"""The intended purpose of the uploaded file."""


class FileUploadResponseBodyTypedDict(TypedDict):
    r"""File uploaded successfully"""

    id: str
    object_name: str
    r"""path to the file in the storage"""
    purpose: FileUploadPurpose
    r"""The intended purpose of the uploaded file."""
    bytes: float
    file_name: str
    created: NotRequired[datetime]
    r"""The date and time the resource was created"""


class FileUploadResponseBody(BaseModel):
    r"""File uploaded successfully"""

    id: Annotated[str, pydantic.Field(alias="_id")]

    object_name: str
    r"""path to the file in the storage"""

    purpose: FileUploadPurpose
    r"""The intended purpose of the uploaded file."""

    bytes: float

    file_name: str

    created: Optional[datetime] = dateutil.parser.isoparse("2024-11-25T11:22:28.171Z")
    r"""The date and time the resource was created"""
