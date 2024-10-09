# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts
from ...commons.types.email import Email
from ...commons.types.phone_number import PhoneNumber
from ...non_insurance_payers.resources.v_1.types.non_insurance_payer_id import NonInsurancePayerId
from .patient_base import PatientBase
from .patient_non_insurance_payer_info_create import PatientNonInsurancePayerInfoCreate


class PatientCreate(PatientBase):
    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None
    phone_consent: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Defaults to false
    """

    email: typing.Optional[Email] = None
    non_insurance_payers: typing.Optional[typing.List[NonInsurancePayerId]] = None
    non_insurance_payers_info: typing.Optional[typing.List[PatientNonInsurancePayerInfoCreate]] = None
    email_consent: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Defaults to false
    """

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
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
