"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_poc_python_multi_env_version.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from orq_poc_python_multi_env_version.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class DeploymentsRequestTypedDict(TypedDict):
    limit: NotRequired[float]
    r"""A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10"""
    after: NotRequired[str]
    r"""A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `ed33dade-ae32-4959-8c5c-7ae4aad748b5`, your subsequent call can include `after=ed33dade-ae32-4959-8c5c-7ae4aad748b5` in order to fetch the next page of the list."""


class DeploymentsRequest(BaseModel):
    limit: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10
    r"""A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10"""

    after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `ed33dade-ae32-4959-8c5c-7ae4aad748b5`, your subsequent call can include `after=ed33dade-ae32-4959-8c5c-7ae4aad748b5` in order to fetch the next page of the list."""


Object = Literal["list"]

DeploymentsDeploymentsType = Literal["function"]
r"""The type of the tool. Currently, only `function` is supported."""

DeploymentsDeploymentsResponse200Type = Literal["object"]


class DeploymentsParametersTypedDict(TypedDict):
    r"""The parameters the functions accepts, described as a JSON Schema object.

    Omitting `parameters` defines a function with an empty parameter list.
    """

    type: DeploymentsDeploymentsResponse200Type
    properties: Dict[str, Any]
    required: NotRequired[List[str]]
    additional_properties: NotRequired[bool]


class DeploymentsParameters(BaseModel):
    r"""The parameters the functions accepts, described as a JSON Schema object.

    Omitting `parameters` defines a function with an empty parameter list.
    """

    type: DeploymentsDeploymentsResponse200Type

    properties: Dict[str, Any]

    required: Optional[List[str]] = None

    additional_properties: Annotated[
        Optional[bool], pydantic.Field(alias="additionalProperties")
    ] = None


class DeploymentsDeploymentsFunctionTypedDict(TypedDict):
    name: str
    r"""The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."""
    parameters: DeploymentsParametersTypedDict
    r"""The parameters the functions accepts, described as a JSON Schema object.

    Omitting `parameters` defines a function with an empty parameter list.
    """
    description: NotRequired[str]
    r"""A description of what the function does, used by the model to choose when and how to call the function."""
    strict: NotRequired[bool]


class DeploymentsDeploymentsFunction(BaseModel):
    name: str
    r"""The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64."""

    parameters: DeploymentsParameters
    r"""The parameters the functions accepts, described as a JSON Schema object.

    Omitting `parameters` defines a function with an empty parameter list.
    """

    description: Optional[str] = None
    r"""A description of what the function does, used by the model to choose when and how to call the function."""

    strict: Optional[bool] = None


class DeploymentsToolsTypedDict(TypedDict):
    type: DeploymentsDeploymentsType
    r"""The type of the tool. Currently, only `function` is supported."""
    function: DeploymentsDeploymentsFunctionTypedDict
    id: NotRequired[float]


class DeploymentsTools(BaseModel):
    type: DeploymentsDeploymentsType
    r"""The type of the tool. Currently, only `function` is supported."""

    function: DeploymentsDeploymentsFunction

    id: Optional[float] = None


ModelType = Literal[
    "chat", "completion", "embedding", "vision", "image", "tts", "stt", "rerank"
]
r"""The type of the model"""

DeploymentsFormat = Literal["url", "b64_json", "text", "json_object"]
r"""Only supported on `image` models."""

DeploymentsQuality = Literal["standard", "hd"]
r"""Only supported on `image` models."""

DeploymentsResponseFormatType = Literal["json_object"]


class DeploymentsResponseFormat2TypedDict(TypedDict):
    type: DeploymentsResponseFormatType


class DeploymentsResponseFormat2(BaseModel):
    type: DeploymentsResponseFormatType


DeploymentsResponseFormatDeploymentsType = Literal["json_schema"]


class ResponseFormatJSONSchemaTypedDict(TypedDict):
    name: str
    strict: bool
    schema_: Dict[str, Any]


class ResponseFormatJSONSchema(BaseModel):
    name: str

    strict: bool

    schema_: Annotated[Dict[str, Any], pydantic.Field(alias="schema")]


class DeploymentsResponseFormat1TypedDict(TypedDict):
    type: DeploymentsResponseFormatDeploymentsType
    json_schema: ResponseFormatJSONSchemaTypedDict


class DeploymentsResponseFormat1(BaseModel):
    type: DeploymentsResponseFormatDeploymentsType

    json_schema: ResponseFormatJSONSchema


DeploymentsResponseFormatTypedDict = TypeAliasType(
    "DeploymentsResponseFormatTypedDict",
    Union[DeploymentsResponseFormat2TypedDict, DeploymentsResponseFormat1TypedDict],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


DeploymentsResponseFormat = TypeAliasType(
    "DeploymentsResponseFormat",
    Union[DeploymentsResponseFormat2, DeploymentsResponseFormat1],
)
r"""An object specifying the format that the model must output.

Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
"""


DeploymentsPhotoRealVersion = Literal["v1", "v2"]
r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

DeploymentsEncodingFormat = Literal["float", "base64"]
r"""The format to return the embeddings"""


class ModelParametersTypedDict(TypedDict):
    r"""Model Parameters: Not all parameters apply to every model"""

    temperature: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    max_tokens: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    top_k: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    top_p: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    frequency_penalty: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    presence_penalty: NotRequired[float]
    r"""Only supported on `chat` and `completion` models."""
    num_images: NotRequired[float]
    r"""Only supported on `image` models."""
    seed: NotRequired[float]
    r"""Best effort deterministic seed for the model. Currently only OpenAI models support these"""
    format: NotRequired[DeploymentsFormat]
    r"""Only supported on `image` models."""
    dimensions: NotRequired[str]
    r"""Only supported on `image` models."""
    quality: NotRequired[DeploymentsQuality]
    r"""Only supported on `image` models."""
    style: NotRequired[str]
    r"""Only supported on `image` models."""
    response_format: NotRequired[Nullable[DeploymentsResponseFormatTypedDict]]
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """
    photo_real_version: NotRequired[DeploymentsPhotoRealVersion]
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""
    encoding_format: NotRequired[DeploymentsEncodingFormat]
    r"""The format to return the embeddings"""


class ModelParameters(BaseModel):
    r"""Model Parameters: Not all parameters apply to every model"""

    temperature: Optional[float] = None
    r"""Only supported on `chat` and `completion` models."""

    max_tokens: Annotated[Optional[float], pydantic.Field(alias="maxTokens")] = None
    r"""Only supported on `chat` and `completion` models."""

    top_k: Annotated[Optional[float], pydantic.Field(alias="topK")] = None
    r"""Only supported on `chat` and `completion` models."""

    top_p: Annotated[Optional[float], pydantic.Field(alias="topP")] = None
    r"""Only supported on `chat` and `completion` models."""

    frequency_penalty: Annotated[
        Optional[float], pydantic.Field(alias="frequencyPenalty")
    ] = None
    r"""Only supported on `chat` and `completion` models."""

    presence_penalty: Annotated[
        Optional[float], pydantic.Field(alias="presencePenalty")
    ] = None
    r"""Only supported on `chat` and `completion` models."""

    num_images: Annotated[Optional[float], pydantic.Field(alias="numImages")] = None
    r"""Only supported on `image` models."""

    seed: Optional[float] = None
    r"""Best effort deterministic seed for the model. Currently only OpenAI models support these"""

    format: Optional[DeploymentsFormat] = None
    r"""Only supported on `image` models."""

    dimensions: Optional[str] = None
    r"""Only supported on `image` models."""

    quality: Optional[DeploymentsQuality] = None
    r"""Only supported on `image` models."""

    style: Optional[str] = None
    r"""Only supported on `image` models."""

    response_format: Annotated[
        OptionalNullable[DeploymentsResponseFormat],
        pydantic.Field(alias="responseFormat"),
    ] = UNSET
    r"""An object specifying the format that the model must output.

    Setting to `{ \"type\": \"json_schema\", \"json_schema\": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema

    Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which ensures the message the model generates is valid JSON.

    Important: when using JSON mode, you must also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly \"stuck\" request. Also note that the message content may be partially cut off if finish_reason=\"length\", which indicates the generation exceeded max_tokens or the conversation exceeded the max context length.
    """

    photo_real_version: Annotated[
        Optional[DeploymentsPhotoRealVersion], pydantic.Field(alias="photoRealVersion")
    ] = None
    r"""The version of photoReal to use. Must be v1 or v2. Only available for `leonardoai` provider"""

    encoding_format: Optional[DeploymentsEncodingFormat] = None
    r"""The format to return the embeddings"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "temperature",
            "maxTokens",
            "topK",
            "topP",
            "frequencyPenalty",
            "presencePenalty",
            "numImages",
            "seed",
            "format",
            "dimensions",
            "quality",
            "style",
            "responseFormat",
            "photoRealVersion",
            "encoding_format",
        ]
        nullable_fields = ["responseFormat"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


DeploymentsProvider = Literal[
    "cohere",
    "openai",
    "anthropic",
    "huggingface",
    "replicate",
    "google",
    "google-ai",
    "azure",
    "aws",
    "anyscale",
    "perplexity",
    "groq",
    "fal",
    "leonardoai",
    "nvidia",
]

DeploymentsDeploymentsRole = Literal[
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

Deployments2DeploymentsResponseType = Literal["image_url"]


class Deployments2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    id: NotRequired[str]
    r"""The orq.ai id of the image"""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class Deployments2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    id: Optional[str] = None
    r"""The orq.ai id of the image"""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class Deployments2Deployments2TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: Deployments2DeploymentsResponseType
    image_url: Deployments2ImageURLTypedDict


class Deployments2Deployments2(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: Deployments2DeploymentsResponseType

    image_url: Deployments2ImageURL


Deployments2DeploymentsType = Literal["text"]


class Deployments21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: Deployments2DeploymentsType
    text: str


class Deployments21(BaseModel):
    r"""Text content part of a prompt message"""

    type: Deployments2DeploymentsType

    text: str


DeploymentsContent2TypedDict = TypeAliasType(
    "DeploymentsContent2TypedDict",
    Union[Deployments21TypedDict, Deployments2Deployments2TypedDict],
)


DeploymentsContent2 = TypeAliasType(
    "DeploymentsContent2", Union[Deployments21, Deployments2Deployments2]
)


DeploymentsDeploymentsContentTypedDict = TypeAliasType(
    "DeploymentsDeploymentsContentTypedDict",
    Union[str, List[DeploymentsContent2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentsDeploymentsContent = TypeAliasType(
    "DeploymentsDeploymentsContent", Union[str, List[DeploymentsContent2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


DeploymentsDeploymentsResponseType = Literal["function"]


class DeploymentsDeploymentsResponseFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentsDeploymentsResponseFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class DeploymentsDeploymentsToolCallsTypedDict(TypedDict):
    type: DeploymentsDeploymentsResponseType
    function: DeploymentsDeploymentsResponseFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class DeploymentsDeploymentsToolCalls(BaseModel):
    type: DeploymentsDeploymentsResponseType

    function: DeploymentsDeploymentsResponseFunction

    id: Optional[str] = None

    index: Optional[float] = None


class DeploymentsMessagesTypedDict(TypedDict):
    role: DeploymentsDeploymentsRole
    r"""The role of the prompt message"""
    content: DeploymentsDeploymentsContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[DeploymentsDeploymentsToolCallsTypedDict]]


class DeploymentsMessages(BaseModel):
    role: DeploymentsDeploymentsRole
    r"""The role of the prompt message"""

    content: DeploymentsDeploymentsContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[DeploymentsDeploymentsToolCalls]] = None


class PromptConfigTypedDict(TypedDict):
    tools: List[DeploymentsToolsTypedDict]
    model: str
    model_type: ModelType
    r"""The type of the model"""
    model_parameters: ModelParametersTypedDict
    r"""Model Parameters: Not all parameters apply to every model"""
    provider: DeploymentsProvider
    messages: List[DeploymentsMessagesTypedDict]


class PromptConfig(BaseModel):
    tools: List[DeploymentsTools]

    model: str

    model_type: ModelType
    r"""The type of the model"""

    model_parameters: ModelParameters
    r"""Model Parameters: Not all parameters apply to every model"""

    provider: DeploymentsProvider

    messages: List[DeploymentsMessages]


class DataTypedDict(TypedDict):
    id: str
    r"""Unique identifier for the object."""
    created: str
    r"""Date in ISO 8601 format at which the object was created."""
    updated: str
    r"""Date in ISO 8601 format at which the object was last updated."""
    key: str
    r"""The deployment unique key"""
    description: str
    r"""An arbitrary string attached to the object. Often useful for displaying to users."""
    prompt_config: PromptConfigTypedDict
    version: str
    r"""THe version of the deployment"""


class Data(BaseModel):
    id: str
    r"""Unique identifier for the object."""

    created: str
    r"""Date in ISO 8601 format at which the object was created."""

    updated: str
    r"""Date in ISO 8601 format at which the object was last updated."""

    key: str
    r"""The deployment unique key"""

    description: str
    r"""An arbitrary string attached to the object. Often useful for displaying to users."""

    prompt_config: PromptConfig

    version: str
    r"""THe version of the deployment"""


class DeploymentsResponseBodyTypedDict(TypedDict):
    r"""List of deployments"""

    object: Object
    data: List[DataTypedDict]
    has_more: bool


class DeploymentsResponseBody(BaseModel):
    r"""List of deployments"""

    object: Object

    data: List[Data]

    has_more: bool
