# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.removable_date_range_optional_end import RemovableDateRangeOptionalEnd
from .identifier_code import IdentifierCode
from .identifier_id import IdentifierId
from .identifier_value import IdentifierValue

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class IdentifierUpdate(pydantic.BaseModel):
    identifier_id: IdentifierId
    identifier_code: typing.Optional[IdentifierCode] = None
    identifier_value: typing.Optional[IdentifierValue] = None
    period: typing.Optional[RemovableDateRangeOptionalEnd] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
