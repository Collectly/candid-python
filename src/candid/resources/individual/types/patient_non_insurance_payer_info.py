# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts
from ...non_insurance_payers.resources.v_1.types.non_insurance_payer import NonInsurancePayer


class PatientNonInsurancePayerInfo(pydantic.BaseModel):
    """
    Examples
    --------
    import uuid

    from candid import PatientNonInsurancePayerInfo
    from candid.resources.non_insurance_payers.v_1 import NonInsurancePayer

    PatientNonInsurancePayerInfo(
        non_insurance_payer=NonInsurancePayer(
            non_insurance_payer_id=uuid.UUID(
                "eb7623ab-d5bc-4b25-b257-2b8fcec578de",
            ),
            name="Sunrise Foundation",
            category="Foundation",
            description="Sunrise Foundation is a non-profit organization that provides financial assistance to patients in need.",
            enabled=True,
        ),
        member_id="123456789",
    )
    """

    non_insurance_payer: NonInsurancePayer
    member_id: typing.Optional[str] = None

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
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
