# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .in_network_contracting_status_result import InNetworkContractingStatusResult
from .out_of_network_contracting_status_result import OutOfNetworkContractingStatusResult


class AttributableContractingStatusResult_OutOfNetwork(OutOfNetworkContractingStatusResult):
    contracting_status: typing_extensions.Literal["out_of_network"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class AttributableContractingStatusResult_InNetwork(InNetworkContractingStatusResult):
    contracting_status: typing_extensions.Literal["in_network"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class AttributableContractingStatusResult_Unknown(pydantic.BaseModel):
    contracting_status: typing_extensions.Literal["unknown"]

    class Config:
        frozen = True


AttributableContractingStatusResult = typing_extensions.Annotated[
    typing.Union[
        AttributableContractingStatusResult_OutOfNetwork,
        AttributableContractingStatusResult_InNetwork,
        AttributableContractingStatusResult_Unknown,
    ],
    pydantic.Field(discriminator="contracting_status"),
]
