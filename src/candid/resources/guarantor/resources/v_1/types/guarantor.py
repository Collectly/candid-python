# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .....commons.types.email import Email
from .....commons.types.phone_number import PhoneNumber
from .guarantor_base import GuarantorBase
from .guarantor_id import GuarantorId


class Guarantor(GuarantorBase):
    guarantor_id: GuarantorId
    phone_numbers: typing.List[PhoneNumber]
    phone_consent: bool
    email: typing.Optional[Email]
    email_consent: bool

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
