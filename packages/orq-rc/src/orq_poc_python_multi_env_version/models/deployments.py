"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_poc_python_multi_env_version.types import BaseModel
from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import NotRequired, TypedDict


InputsTypedDict = Union[str, float, bool]


Inputs = Union[str, float, bool]


Role = Literal[
    "system",
    "assistant",
    "user",
    "exception",
    "tool",
    "prompt",
    "correction",
    "expected_output",
]
r"""The role of the prompt message"""

TwoType = Literal["image_url"]


class ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class Two2TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: TwoType
    image_url: ImageURLTypedDict


class Two2(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: TwoType

    image_url: ImageURL


Deployments2Type = Literal["text"]


class OneTypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: Deployments2Type
    text: str


class One(BaseModel):
    r"""Text content part of a prompt message"""

    type: Deployments2Type

    text: str


TwoTypedDict = Union[OneTypedDict, Two2TypedDict]


Two = Union[One, Two2]


ContentTypedDict = Union[str, List[TwoTypedDict]]
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


Content = Union[str, List[Two]]
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


Type = Literal["function"]


class FunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class Function(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class ToolCallsTypedDict(TypedDict):
    type: Type
    function: FunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class ToolCalls(BaseModel):
    type: Type

    function: Function

    id: Optional[str] = None

    index: Optional[float] = None


class PrefixMessagesTypedDict(TypedDict):
    role: Role
    r"""The role of the prompt message"""
    content: ContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[ToolCallsTypedDict]]


class PrefixMessages(BaseModel):
    role: Role
    r"""The role of the prompt message"""

    content: Content
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[ToolCalls]] = None


DeploymentsRole = Literal[
    "system",
    "assistant",
    "user",
    "exception",
    "tool",
    "prompt",
    "correction",
    "expected_output",
]
r"""The role of the prompt message"""

Deployments2MessagesContentType = Literal["image_url"]


class TwoImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class TwoImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class Deployments22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: Deployments2MessagesContentType
    image_url: TwoImageURLTypedDict


class Deployments22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: Deployments2MessagesContentType

    image_url: TwoImageURL


Deployments2MessagesType = Literal["text"]


class Two1TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: Deployments2MessagesType
    text: str


class Two1(BaseModel):
    r"""Text content part of a prompt message"""

    type: Deployments2MessagesType

    text: str


Content2TypedDict = Union[Two1TypedDict, Deployments22TypedDict]


Content2 = Union[Two1, Deployments22]


DeploymentsContentTypedDict = Union[str, List[Content2TypedDict]]
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentsContent = Union[str, List[Content2]]
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentsType = Literal["function"]


class DeploymentsFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentsFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentsToolCallsTypedDict(TypedDict):
    type: DeploymentsType
    function: DeploymentsFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class DeploymentsToolCalls(BaseModel):
    type: DeploymentsType

    function: DeploymentsFunction

    id: Optional[str] = None

    index: Optional[float] = None


class MessagesTypedDict(TypedDict):
    role: DeploymentsRole
    r"""The role of the prompt message"""
    content: DeploymentsContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[DeploymentsToolCallsTypedDict]]


class Messages(BaseModel):
    role: DeploymentsRole
    r"""The role of the prompt message"""

    content: DeploymentsContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[DeploymentsToolCalls]] = None


UserIDTypedDict = Union[str, float]
r"""Unique ID that identifies a user. This is useful for tracking the same user across multiple requests"""


UserID = Union[str, float]
r"""Unique ID that identifies a user. This is useful for tracking the same user across multiple requests"""


class InvokeOptionsTypedDict(TypedDict):
    include_retrievals: NotRequired[bool]
    r"""Whether to include the retrieved knowledge chunks in the response."""


class InvokeOptions(BaseModel):
    include_retrievals: Optional[bool] = False
    r"""Whether to include the retrieved knowledge chunks in the response."""


class DeploymentsTypedDict(TypedDict):
    r"""The deployment request payload"""

    key: str
    r"""The deployment id to invoke"""
    stream: NotRequired[bool]
    r"""If set, partial message content will be sent. Tokens will be sent as data-only `server-sent events` as they become available, with the stream terminated by a `data: [DONE]` message."""
    inputs: NotRequired[Dict[str, InputsTypedDict]]
    r"""Key-value pairs variables to replace in your prompts. If a variable is not provided that is defined in the prompt, the default variables are used."""
    context: NotRequired[Dict[str, Any]]
    r"""Key-value pairs that match your data model and fields declared in your configuration matrix. If you send multiple prompt keys, the context will be applied to the evaluation of each key."""
    prefix_messages: NotRequired[List[PrefixMessagesTypedDict]]
    r"""A list of messages to include after the `System` message, but before the  `User` and `Assistant` pairs configured in your deployment."""
    messages: NotRequired[List[MessagesTypedDict]]
    r"""A list of messages to send to the deployment."""
    file_ids: NotRequired[List[str]]
    r"""A list of file IDs that are associated with the deployment request."""
    metadata: NotRequired[Dict[str, Any]]
    r"""Key-value pairs that you want to attach to the log generated by this request."""
    chain_id: NotRequired[str]
    r"""Unique ID that identifies a chaining operation. This is useful for tracking a chain of completions across multiple"""
    conversation_id: NotRequired[str]
    r"""Unique ID that identifies a chat conversation. This is useful for tracking the same conversation across multiple requests"""
    user_id: NotRequired[UserIDTypedDict]
    r"""Unique ID that identifies a user. This is useful for tracking the same user across multiple requests"""
    deployment_id: NotRequired[str]
    r"""Unique ID that identifies a deployment entity."""
    deployment_variant_id: NotRequired[str]
    r"""Unique ID that identifies a specific variant of a deployment."""
    extra_params: NotRequired[Dict[str, Any]]
    r"""Utilized for passing additional parameters to the model provider. Exercise caution when using this feature, as the included parameters will overwrite any parameters specified in the deployment prompt configuration."""
    invoke_options: NotRequired[InvokeOptionsTypedDict]


class Deployments(BaseModel):
    r"""The deployment request payload"""

    key: str
    r"""The deployment id to invoke"""

    stream: Optional[bool] = False
    r"""If set, partial message content will be sent. Tokens will be sent as data-only `server-sent events` as they become available, with the stream terminated by a `data: [DONE]` message."""

    inputs: Optional[Dict[str, Inputs]] = None
    r"""Key-value pairs variables to replace in your prompts. If a variable is not provided that is defined in the prompt, the default variables are used."""

    context: Optional[Dict[str, Any]] = None
    r"""Key-value pairs that match your data model and fields declared in your configuration matrix. If you send multiple prompt keys, the context will be applied to the evaluation of each key."""

    prefix_messages: Optional[List[PrefixMessages]] = None
    r"""A list of messages to include after the `System` message, but before the  `User` and `Assistant` pairs configured in your deployment."""

    messages: Optional[List[Messages]] = None
    r"""A list of messages to send to the deployment."""

    file_ids: Optional[List[str]] = None
    r"""A list of file IDs that are associated with the deployment request."""

    metadata: Optional[Dict[str, Any]] = None
    r"""Key-value pairs that you want to attach to the log generated by this request."""

    chain_id: Optional[str] = None
    r"""Unique ID that identifies a chaining operation. This is useful for tracking a chain of completions across multiple"""

    conversation_id: Optional[str] = None
    r"""Unique ID that identifies a chat conversation. This is useful for tracking the same conversation across multiple requests"""

    user_id: Optional[UserID] = None
    r"""Unique ID that identifies a user. This is useful for tracking the same user across multiple requests"""

    deployment_id: Optional[str] = None
    r"""Unique ID that identifies a deployment entity."""

    deployment_variant_id: Optional[str] = None
    r"""Unique ID that identifies a specific variant of a deployment."""

    extra_params: Optional[Dict[str, Any]] = None
    r"""Utilized for passing additional parameters to the model provider. Exercise caution when using this feature, as the included parameters will overwrite any parameters specified in the deployment prompt configuration."""

    invoke_options: Optional[InvokeOptions] = None
