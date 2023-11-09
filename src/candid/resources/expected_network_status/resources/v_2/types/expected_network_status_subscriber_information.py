# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from .....payers.resources.v_3.types.payer_uuid import PayerUuid
from .insurance_type import InsuranceType


class ExpectedNetworkStatusSubscriberInformation(pydantic.BaseModel):
    payer_uuid: PayerUuid = pydantic.Field(
        description="The UUID that corresponds with the payer on the patient’s insurance card"
    )
    member_id: str = pydantic.Field(description="The member_id on the patient’s insurance card")
    insurance_type: InsuranceType = pydantic.Field(
        description="The insurance information on the patient's insurance card"
    )

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
