# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .insurance_card_base import InsuranceCardBase
from .insurance_card_id import InsuranceCardId


class InsuranceCard(InsuranceCardBase):
    """
    Examples
    --------
    import uuid

    from candid import InsuranceTypeCode, SourceOfPaymentCode
    from candid.resources.insurance_cards.v_2 import InsuranceCard

    InsuranceCard(
        insurance_card_id=uuid.UUID(
            "ca5b7711-4419-4161-9b7c-3494ac40c8d4",
        ),
        member_id="E85313B4-0FFC-4119-8042-8161A4ECFF0A",
        payer_name="John Doe",
        payer_id="836DDAA6-863F-4020-ACCA-205A689F0002",
        rx_bin="610014",
        rx_pcn="MEDDPRIME",
        image_url_front="https://s3.amazonaws.com/front.jpg",
        image_url_back="https://s3.amazonaws.com/back.jpg",
        group_number="ABC12345",
        plan_name="Silver PPO Plan",
        plan_type=SourceOfPaymentCode.SELF_PAY,
        insurance_type=InsuranceTypeCode.C_12,
    )
    """

    insurance_card_id: InsuranceCardId
    member_id: str
    payer_name: str
    payer_id: str
    rx_bin: typing.Optional[str] = None
    rx_pcn: typing.Optional[str] = None
    image_url_front: typing.Optional[str] = None
    image_url_back: typing.Optional[str] = None

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
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
