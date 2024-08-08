# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ........core.datetime_utils import serialize_datetime
from ........core.pydantic_utilities import deep_union_pydantic_dicts
from .....common.types.address import Address
from .....common.types.contact_point import ContactPoint
from .....common.types.disability_status import DisabilityStatus
from .....common.types.ethnicity import Ethnicity
from .....common.types.gender import Gender
from .....common.types.human_name import HumanName
from .....common.types.race import Race
from .....common.types.sex import Sex
from .....common.types.sexual_orientation import SexualOrientation
from .contact import Contact
from .external_provenance import ExternalProvenance
from .external_provider import ExternalProvider
from .filing_order import FilingOrder
from .marital_status import MaritalStatus


class MutablePatient(pydantic.BaseModel):
    """
    An object representing patient demographics information.
    """

    name: HumanName
    other_names: typing.List[HumanName] = pydantic.Field()
    """
    Other names for the patient.
    """

    gender: typing.Optional[Gender] = None
    birth_date: dt.date
    social_security_number: typing.Optional[str] = None
    biological_sex: typing.Optional[Sex] = pydantic.Field(default=None)
    """
    The biological sex of the patient.
    """

    sexual_orientation: typing.Optional[SexualOrientation] = pydantic.Field(default=None)
    """
    The sexual orientation of the patient.
    """

    race: typing.Optional[Race] = None
    ethnicity: typing.Optional[Ethnicity] = None
    disability_status: typing.Optional[DisabilityStatus] = None
    marital_status: typing.Optional[MaritalStatus] = None
    deceased: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Time of death for the patient. Leave unset if the patient is not deceased.
    """

    multiple_birth: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of siblings the patient was born with. Leave unset if the patient was not part of a multiple birth.
    """

    primary_address: Address = pydantic.Field()
    """
    The primary address for the patient.
    """

    other_addresses: typing.List[Address] = pydantic.Field()
    """
    Other addresses for the patient.
    """

    primary_telecom: ContactPoint = pydantic.Field()
    """
    The primary phone number for the patient.
    """

    other_telecoms: typing.List[ContactPoint] = pydantic.Field()
    """
    Other phone numbers for the patient.
    """

    email: typing.Optional[str] = None
    electronic_communication_opt_in: typing.Optional[bool] = None
    photo: typing.Optional[str] = None
    language: typing.Optional[str] = None
    external_provenance: typing.Optional[ExternalProvenance] = pydantic.Field(default=None)
    """
    Information about the upstream system that owns this patient data. Leave unset if Candid owns patient data.
    """

    contacts: typing.List[Contact] = pydantic.Field()
    """
    Contacts for the patient.
    """

    general_practitioners: typing.List[ExternalProvider]
    filing_order: FilingOrder

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
