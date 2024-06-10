# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.street_address_long_zip import StreetAddressLongZip
from .organization_service_facility_id import OrganizationServiceFacilityId
from .service_facility_mode import ServiceFacilityMode
from .service_facility_operational_status import ServiceFacilityOperationalStatus
from .service_facility_physical_type import ServiceFacilityPhysicalType
from .service_facility_status import ServiceFacilityStatus
from .service_facility_type import ServiceFacilityType


class OrganizationServiceFacility(pydantic.BaseModel):
    """
    Examples
    --------
    import uuid

    from candid import State, StreetAddressLongZip
    from candid.resources.organization_service_facilities.v_2 import (
        OrganizationServiceFacility,
        ServiceFacilityMode,
        ServiceFacilityOperationalStatus,
        ServiceFacilityPhysicalType,
        ServiceFacilityStatus,
        ServiceFacilityType,
    )

    OrganizationServiceFacility(
        organization_service_facility_id=uuid.UUID(
            "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
        ),
        name="Test Service Facility",
        aliases=["Test Service Facility Alias"],
        description="Test Service Facility Description",
        status=ServiceFacilityStatus.ACTIVE,
        operational_status=ServiceFacilityOperationalStatus.CLOSED,
        mode=ServiceFacilityMode.INSTANCE,
        type=ServiceFacilityType.DIAGNOSTICS_OR_THERAPEUTICS_UNIT,
        physical_type=ServiceFacilityPhysicalType.SITE,
        telecoms=["555-555-5555"],
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
    )
    """

    organization_service_facility_id: OrganizationServiceFacilityId
    name: str = pydantic.Field()
    """
    The name of the service facility.
    """

    aliases: typing.List[str] = pydantic.Field()
    """
    A list of alternate names for the service facility.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the service facility.
    """

    npi: typing.Optional[str] = pydantic.Field(default=None)
    """
    An NPI specific to the service facility if applicable, i.e. if it has one and is not under the billing provider's NPI.
    Box 32 section (a) of the CMS-1500 claim form.
    """

    status: typing.Optional[ServiceFacilityStatus] = pydantic.Field(default=None)
    """
    The status of the service facility.
    """

    operational_status: typing.Optional[ServiceFacilityOperationalStatus] = pydantic.Field(default=None)
    """
    The operational status of the service facility.
    """

    mode: typing.Optional[ServiceFacilityMode] = pydantic.Field(default=None)
    """
    The mode of the service facility.
    """

    type: typing.Optional[ServiceFacilityType] = pydantic.Field(default=None)
    """
    The type of the service facility.
    """

    physical_type: typing.Optional[ServiceFacilityPhysicalType] = pydantic.Field(default=None)
    """
    The physical type of the service facility.
    """

    telecoms: typing.List[str] = pydantic.Field()
    """
    A list of contact methods for the service facility.
    """

    address: StreetAddressLongZip = pydantic.Field()
    """
    The address of the service facility.
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
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
