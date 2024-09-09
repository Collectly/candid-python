# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts


class NonInsurancePayerDescriptionUpdate_Remove(pydantic.BaseModel):
    type: typing.Literal["remove"] = "remove"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class NonInsurancePayerDescriptionUpdate_Set(pydantic.BaseModel):
    value: str
    type: typing.Literal["set"] = "set"

    class Config:
        frozen = True
        smart_union = True


NonInsurancePayerDescriptionUpdate = typing.Union[
    NonInsurancePayerDescriptionUpdate_Remove, NonInsurancePayerDescriptionUpdate_Set
]
