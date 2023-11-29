# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .date_range_optional_end import DateRangeOptionalEnd

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RemovableDateRangeOptionalEnd_DateRange(DateRangeOptionalEnd):
    type: typing_extensions.Literal["date_range"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class RemovableDateRangeOptionalEnd_Remove(pydantic.BaseModel):
    type: typing_extensions.Literal["remove"]

    class Config:
        frozen = True
        smart_union = True


RemovableDateRangeOptionalEnd = typing.Union[
    RemovableDateRangeOptionalEnd_DateRange, RemovableDateRangeOptionalEnd_Remove
]
