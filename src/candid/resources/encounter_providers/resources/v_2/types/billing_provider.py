# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from .....commons.types.street_address_long_zip import StreetAddressLongZip
from .encounter_provider_base import EncounterProviderBase


class BillingProvider(EncounterProviderBase):
    """
    The billing provider is the provider or business entity submitting the claim.
    Billing provider may be, but is not necessarily, the same person/NPI as the rendering provider.
    From a payer's perspective, this represents the person or entity being reimbursed.
    When a contract exists with the target payer, the billing provider should be the entity contracted with the payer.
    In some circumstances, this will be an individual provider. In that case, submit that provider's NPI and the
    tax ID (TIN) that the provider gave to the payer during contracting.
    In other cases, the billing entity will be a medical group. If so, submit the group NPI and the group's tax ID.
    Box 33 on the CMS-1500 claim form.
    """

    address: StreetAddressLongZip
    tax_id: str = pydantic.Field(
        description=(
            "If the provider has a contract with insurance, this must be the same tax ID given to the payer on an IRS W-9 form completed during contracting.\n"
        )
    )
    npi: str
    taxonomy_code: typing.Optional[str]

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