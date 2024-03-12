# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.street_address_long_zip import StreetAddressLongZip

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EncounterServiceFacilityBase(pydantic.BaseModel):
    """
    Encounter Service facility is typically the location a medical service was rendered, such as a provider office or hospital.
    For telehealth, service facility can represent the provider's location when the service was delivered (e.g., home),
    or the location where an in-person visit would have taken place, whichever is easier to identify.
    If the provider is in-network, service facility may be defined in payer contracts.
    Box 32 on the CMS-1500 claim form.
    Note that for an in-network claim to be successfully adjudicated, the service facility address listed on claims
    must match what was provided to the payer during the credentialing process.
    """

    organization_name: str
    npi: typing.Optional[str] = pydantic.Field(
        default=None,
        description=(
            "An NPI specific to the service facility if applicable, i.e. if it has one and is not under the billing provider's NPI.\n"
            "Box 32 section (a) of the CMS-1500 claim form.\n"
        ),
    )
    address: StreetAddressLongZip = pydantic.Field(
        description='zip_plus_four_code is required for service facility address. When the zip_plus_four_code is not available use "9998" as per CMS documentation.'
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
