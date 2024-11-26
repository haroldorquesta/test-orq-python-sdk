"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from orq_poc_python_multi_env_version.types import BaseModel
import pydantic
from typing import List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


GetV2ResourcesEvaluatorsTemplatesObject = Literal["list"]

DataFunction = Literal[
    "is_valid_json",
    "bert_score",
    "bleu_score",
    "rouge_n",
    "meteor_score",
    "cosine_similarity",
    "levenshtein_distance",
    "exact_match",
    "contains",
    "contains_all",
    "contains_any",
    "contains_email",
    "contains_url",
    "contains_none",
    "contains_valid_link",
    "ends_with",
    "length_between",
    "length_greater_than",
    "length_less_than",
    "moderations_openai",
    "moderations_google",
    "one_line",
    "regex",
    "start_with",
]

DataOutputType = Literal["boolean", "number", "string", "enum"]


class DataMetadataTypedDict(TypedDict):
    required_model_with_tools_support: NotRequired[bool]
    required_retrieval_context: NotRequired[bool]
    required_expected_output: NotRequired[bool]
    supported_on_input_type: NotRequired[bool]
    supported_on_output_type: NotRequired[bool]


class DataMetadata(BaseModel):
    required_model_with_tools_support: Optional[bool] = None

    required_retrieval_context: Optional[bool] = None

    required_expected_output: Optional[bool] = None

    supported_on_input_type: Optional[bool] = None

    supported_on_output_type: Optional[bool] = None


GetV2ResourcesEvaluatorsTemplatesDataType = Literal["function_eval"]


class Data2TypedDict(TypedDict):
    id: str
    display_name: str
    description: str
    function: DataFunction
    output_type: DataOutputType
    type: GetV2ResourcesEvaluatorsTemplatesDataType
    enabled: NotRequired[bool]
    metadata: NotRequired[DataMetadataTypedDict]


class Data2(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]

    display_name: str

    description: str

    function: DataFunction

    output_type: DataOutputType

    type: GetV2ResourcesEvaluatorsTemplatesDataType

    enabled: Optional[bool] = True

    metadata: Optional[DataMetadata] = None


OutputType = Literal["boolean", "number", "string", "enum"]

DataType = Literal["llm_eval"]


class Data1TypedDict(TypedDict):
    id: str
    display_name: str
    description: str
    prompt: str
    output_type: OutputType
    type: DataType
    enabled: NotRequired[bool]


class Data1(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]

    display_name: str

    description: str

    prompt: str

    output_type: OutputType

    type: DataType

    enabled: Optional[bool] = True


GetV2ResourcesEvaluatorsTemplatesDataTypedDict = TypeAliasType(
    "GetV2ResourcesEvaluatorsTemplatesDataTypedDict",
    Union[Data1TypedDict, Data2TypedDict],
)


GetV2ResourcesEvaluatorsTemplatesData = TypeAliasType(
    "GetV2ResourcesEvaluatorsTemplatesData", Union[Data1, Data2]
)


class GetV2ResourcesEvaluatorsTemplatesResponseBodyTypedDict(TypedDict):
    r"""Successful operation"""

    object: GetV2ResourcesEvaluatorsTemplatesObject
    data: List[GetV2ResourcesEvaluatorsTemplatesDataTypedDict]
    has_more: bool


class GetV2ResourcesEvaluatorsTemplatesResponseBody(BaseModel):
    r"""Successful operation"""

    object: GetV2ResourcesEvaluatorsTemplatesObject

    data: List[GetV2ResourcesEvaluatorsTemplatesData]

    has_more: bool
