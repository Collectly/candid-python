# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .....commons.types.street_address_long_zip import StreetAddressLongZip
from .service_facility_mode import ServiceFacilityMode
from .service_facility_operational_status import ServiceFacilityOperationalStatus
from .service_facility_physical_type import ServiceFacilityPhysicalType
from .service_facility_status import ServiceFacilityStatus
from .service_facility_type import ServiceFacilityType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class OrganizationServiceFacilityUpdate(pydantic.BaseModel):
    """
    from candid import State, StreetAddressLongZip
    from candid.resources.organization_service_facilities.v_2 import (
        OrganizationServiceFacilityUpdate,
        ServiceFacilityMode,
        ServiceFacilityOperationalStatus,
        ServiceFacilityPhysicalType,
        ServiceFacilityStatus,
        ServiceFacilityType,
    )

    OrganizationServiceFacilityUpdate(
        name="Test Service Facility",
        aliases=["Test Service Facility Alias"],
        description="Test Service Facility Description",
        status=ServiceFacilityStatus.ACTIVE,
        operational_status=ServiceFacilityOperationalStatus.C,
        mode=ServiceFacilityMode.INSTANCE,
        type=ServiceFacilityType.DX,
        physical_type=ServiceFacilityPhysicalType.SI,
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

    name: typing.Optional[str] = pydantic.Field(default=None, description="The name of the service facility.")
    aliases: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None, description="A list of alternate names for the service facility."
    )
    description: typing.Optional[str] = pydantic.Field(
        default=None, description="A description of the service facility."
    )
    status: typing.Optional[ServiceFacilityStatus] = pydantic.Field(
        default=None, description="The status of the service facility."
    )
    operational_status: typing.Optional[ServiceFacilityOperationalStatus] = pydantic.Field(
        default=None, description="The operational status of the service facility."
    )
    mode: typing.Optional[ServiceFacilityMode] = pydantic.Field(
        default=None, description="The mode of the service facility."
    )
    type: typing.Optional[ServiceFacilityType] = pydantic.Field(
        default=None, description="The type of the service facility."
    )
    physical_type: typing.Optional[ServiceFacilityPhysicalType] = pydantic.Field(
        default=None, description="The physical type of the service facility."
    )
    telecoms: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None, description="A list of contact methods for the service facility."
    )
    address: typing.Optional[StreetAddressLongZip] = pydantic.Field(
        default=None, description="The address of the service facility."
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