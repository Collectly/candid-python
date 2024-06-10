# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .rx_cui import RxCui


class Medication(pydantic.BaseModel):
    """
    Examples
    --------
    from candid.resources.encounters.v_4 import Medication

    Medication(
        name="Lisinopril",
        rx_cui="860975",
        dosage="10mg",
        dosage_form="Tablet",
        frequency="Once Daily",
        as_needed=True,
    )
    """

    name: str
    rx_cui: typing.Optional[RxCui] = None
    dosage: typing.Optional[str] = None
    dosage_form: typing.Optional[str] = None
    frequency: typing.Optional[str] = None
    as_needed: typing.Optional[bool] = None

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
