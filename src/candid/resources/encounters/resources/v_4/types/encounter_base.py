# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .....commons.types.date import Date
from .....commons.types.delay_reason_code import DelayReasonCode
from .....commons.types.encounter_external_id import EncounterExternalId
from .....commons.types.street_address_long_zip import StreetAddressLongZip
from .billable_status_type import BillableStatusType
from .intervention import Intervention
from .medication import Medication
from .prior_authorization_number import PriorAuthorizationNumber
from .responsible_party_type import ResponsiblePartyType
from .service_authorization_exception_code import ServiceAuthorizationExceptionCode
from .synchronicity_type import SynchronicityType
from .vitals import Vitals

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EncounterBase(pydantic.BaseModel):
    external_id: EncounterExternalId = pydantic.Field(
        description=(
            "A client-specified unique ID to associate with this encounter;\n"
            "for example, your internal encounter ID or a Dr. Chrono encounter ID.\n"
            "This field should not contain PHI.\n"
        )
    )
    date_of_service: Date = pydantic.Field(
        description=(
            "Date formatted as YYYY-MM-DD; eg: 2019-08-24.\n"
            "This date must be the local date in the timezone where the service occurred.\n"
            "Box 24a on the CMS-1500 claim form.\n"
            "If service occurred over a range of dates, this should be the start date.\n"
        )
    )
    end_date_of_service: typing.Optional[Date] = pydantic.Field(
        default=None,
        description=(
            "Date formatted as YYYY-MM-DD; eg: 2019-08-25.\n"
            "This date must be the local date in the timezone where the service occurred.\n"
            "If omitted, the Encounter is assumed to be for a single day.\n"
            "Must not be temporally before the date_of_service field.\n"
        ),
    )
    prior_authorization_number: typing.Optional[PriorAuthorizationNumber] = pydantic.Field(
        default=None, description="Box 23 on the CMS-1500 claim form."
    )
    patient_authorized_release: bool = pydantic.Field(
        description=(
            "Whether this patient has authorized the release of medical information\n"
            "for billing purpose.\n"
            "Box 12 on the CMS-1500 claim form.\n"
        )
    )
    benefits_assigned_to_provider: bool = pydantic.Field(
        description=(
            "Whether this patient has authorized insurance payments to be made to you,\n"
            "not them. If false, patient may receive reimbursement.\n"
            "Box 13 on the CMS-1500 claim form.\n"
        )
    )
    provider_accepts_assignment: bool = pydantic.Field(
        description=(
            "Whether you have accepted the patient's authorization for insurance payments\n"
            "to be made to you, not them.\n"
            "Box 27 on the CMS-1500 claim form.\n"
        )
    )
    appointment_type: typing.Optional[str] = pydantic.Field(
        default=None, description='Human-readable description of the appointment type (ex: "Acupuncture - Headaches").'
    )
    existing_medications: typing.Optional[typing.List[Medication]] = None
    vitals: typing.Optional[Vitals] = None
    interventions: typing.Optional[typing.List[Intervention]] = None
    pay_to_address: typing.Optional[StreetAddressLongZip] = pydantic.Field(
        default=None, description="Specifies the address to which payments for the claim should be sent."
    )
    synchronicity: typing.Optional[SynchronicityType] = pydantic.Field(
        default=None,
        description=(
            "Whether or not this was a synchronous or asynchronous encounter.\n"
            "Asynchronous encounters occur when providers and patients communicate online using\n"
            "forms, instant messaging, or other pre-recorded digital mediums.\n"
            "Synchronous encounters occur in live, real-time settings where the patient interacts\n"
            "directly with the provider, such as over video or a phone call.\n"
        ),
    )
    billable_status: BillableStatusType = pydantic.Field(
        description=(
            "Defines if the Encounter is to be billed by Candid to the responsible_party.\n"
            "Examples for when this should be set to NOT_BILLABLE include\n"
            "if the Encounter has not occurred yet or if there is no intention of ever billing the responsible_party.\n"
        )
    )
    responsible_party: ResponsiblePartyType = pydantic.Field(
        description="Defines the party to be billed with the initial balance owed on the claim."
    )
    additional_information: typing.Optional[str] = pydantic.Field(
        default=None,
        description=(
            "Defines additional information on the claim needed by the payer.\n" "Box 19 on the CMS-1500 claim form.\n"
        ),
    )
    service_authorization_exception_code: typing.Optional[ServiceAuthorizationExceptionCode] = pydantic.Field(
        default=None,
        description=(
            "837p Loop2300 REF\*4N\n"
            "Required when mandated by government law or regulation to obtain authorization for specific service(s) but, for the\n"
            "reasons listed in one of the enum values of ServiceAuthorizationExceptionCode, the service was performed without\n"
            "obtaining the authorization.\n"
        ),
    )
    admission_date: typing.Optional[Date] = pydantic.Field(
        default=None,
        description=(
            "837p Loop2300 DTP\*435, CMS-1500 Box 18\n"
            "Required on all ambulance claims when the patient was known to be admitted to the hospital.\n"
            "OR\n"
            "Required on all claims involving inpatient medical visits.\n"
        ),
    )
    discharge_date: typing.Optional[Date] = pydantic.Field(
        default=None,
        description=(
            "837p Loop2300 DTP\*096, CMS-1500 Box 18\n"
            "Required for inpatient claims when the patient was discharged from the facility and the discharge date is known.\n"
        ),
    )
    onset_of_current_illness_or_symptom_date: typing.Optional[Date] = pydantic.Field(
        default=None,
        description=(
            "837p Loop2300 DTP\*431, CMS-1500 Box 14\n"
            "Required for the initial medical service or visit performed in response to a medical emergency when the date is available and is different than the date of service.\n"
            "OR\n"
            "This date is the onset of acute symptoms for the current illness or condition.\n"
        ),
    )
    last_menstrual_period_date: typing.Optional[Date] = pydantic.Field(
        default=None,
        description=(
            "837p Loop2300 DTP\*484, CMS-1500 Box 14\n"
            "Required when, in the judgment of the provider, the services on this claim are related to the patient's pregnancy.\n"
        ),
    )
    delay_reason_code: typing.Optional[DelayReasonCode] = pydantic.Field(
        default=None,
        description=("837i Loop2300, CLM-1300 Box 20\n" "Code indicating the reason why a request was delayed\n"),
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
