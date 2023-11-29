# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .payer_info import PayerInfo
from .payer_uuid import PayerUuid

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PayerIdentifier_PayerInfo(PayerInfo):
    type: typing_extensions.Literal["payer_info"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class PayerIdentifier_PayerUuid(pydantic.BaseModel):
    type: typing_extensions.Literal["payer_uuid"]
    value: PayerUuid

    class Config:
        frozen = True
        smart_union = True


PayerIdentifier = typing.Union[PayerIdentifier_PayerInfo, PayerIdentifier_PayerUuid]