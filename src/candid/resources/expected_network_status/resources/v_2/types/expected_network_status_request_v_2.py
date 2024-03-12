# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .....commons.types.facility_type_code import FacilityTypeCode
from .....commons.types.street_address_short_zip import StreetAddressShortZip
from .....organization_providers.resources.v_2.types.organization_provider_id import OrganizationProviderId
from .....organization_service_facilities.resources.v_2.types.organization_service_facility_id import (
    OrganizationServiceFacilityId,
)
from .expected_network_status_subscriber_information import ExpectedNetworkStatusSubscriberInformation
from .service_type import ServiceType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ExpectedNetworkStatusRequestV2(pydantic.BaseModel):
    service_type: ServiceType = pydantic.Field(
        description=(
            "For some payers, payer routing depends on whether the rendered service qualifies as a behavioral health visit\n"
            "(e.g. Blue Shield of California routes to Magellan for behavioral health visits).\n"
            "\n"
            "For post appointment payer routing, Candid uses a CPT code list to determine whether the appointment qualifies as a\n"
            "behavioral health visit\n"
            "(see “Inputs: Service Type” in the appendix for list of qualifying CPT codes and behavioral health routing logic).\n"
            "Since CPT codes are not available pre-appointment, the service type input is used to determine whether the appointment is expected\n"
            "to qualify as behavioral health.\n"
        )
    )
    place_of_service_code: FacilityTypeCode = pydantic.Field(description="Expected place of service")
    subscriber_information: ExpectedNetworkStatusSubscriberInformation = pydantic.Field(
        description="Information present on the patient's insurance card"
    )
    patient_address: StreetAddressShortZip
    billing_provider_id: OrganizationProviderId
    organization_service_facility_id: OrganizationServiceFacilityId = pydantic.Field(
        description="The id of the service facility where the appointment will be rendered"
    )
    date_of_service: dt.date = pydantic.Field(description="Expected date of service")

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
