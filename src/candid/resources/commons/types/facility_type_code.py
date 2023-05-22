# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FacilityTypeCode(str, enum.Enum):
    """
    Box 24B on the CMS-1500 claim form. Line-level place of service is not currently supported.
    02 for telemedicine, 11 for in-person. Full list here:
    https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set
    """

    PHARMACY = "01"
    TELEHEALTH = "02"
    SCHOOL = "03"
    HOMELESS_SHELTER = "04"
    INDIAN_HEALTH_SERVICE_FREE_STANDING = "05"
    INDIAN_HEALTH_SERVICE_PROVIDER_BASED = "06"
    TRIBAL_FREE_STANDING = "07"
    TRIBAL_PROVIDER_BASED = "08"
    PRISON_OR_CORRECTIONAL_FACILITY = "09"
    TELEHEALTH_PATIENT_HOME = "10"
    OFFICE = "11"
    HOME = "12"
    ASSISTED_LIVING_FACILITY = "13"
    GROUP_HOME = "14"
    MOBILE_UNIT = "15"
    TEMPORARY_LODGING = "16"
    WALK_IN_RETAIL_HEALTH_CLINIC = "17"
    PLACE_OF_EMPLOYMENT_WORKSITE = "18"
    OFF_CAMPUS_OUTPATIENT_HOSPITAL = "19"
    URGENT_CARE_FACILITY = "20"
    INPATIENT_HOSPITAL = "21"
    OUTPATIENT_HOSPITAL = "22"
    EMERGENCY_ROOM_HOSPITAL = "23"
    AMBULATORY_SURGICAL_CENTER = "24"
    BIRTHING_CENTER = "25"
    MILITARY_TREATMENT_FACILITY = "26"
    SKILLED_NURSING_FACILITY = "31"
    NURSING_FACILITY = "32"
    CUSTODIAL_CARE_FACILITY = "33"
    HOSPICE = "34"
    AMBULANCE_LAND = "41"
    AMBULANCE_AIR_OR_WATER = "42"
    INDEPENDENT_CLINIC = "49"
    FEDERALLY_QUALIFIED_HEALTH_CENTER = "50"
    INPATIENT_PSYCHIATRIC_FACILITY = "51"
    PSYCHIATRIC_FACILITY_PARTIAL_HOSPITALIZATION = "52"
    COMMUNITY_MENTAL_HEALTH_CENTER = "53"
    INTERMEDIATE_CARE_FACILITY_MENTALLY_RETARDED = "54"
    RESIDENTIAL_SUBSTANCE_ABUSE_TREATMENT_FACILITY = "55"
    PSYCHIATRIC_RESIDENTIAL_TREATMENT_CENTER = "56"
    NON_RESIDENTIAL_SUBSTANCE_ABUSE_TREATMENT_FACILITY = "57"
    NON_RESIDENTIAL_OPIOID_TREATMENT_FACILITY = "58"
    MASS_IMMUNIZATION_CENTER = "60"
    COMPREHENSIVE_INPATIENT_REHABILITATION_FACILITY = "61"
    COMPREHENSIVE_OUTPATIENT_REHABILITATION_FACILITY = "62"
    END_STAGE_RENAL_DISEASE_TREATMENT_FACILITY = "65"
    STATE_OR_LOCAL_PUBLIC_HEALTH_CLINIC = "71"
    RURAL_HEALTH_CLINIC = "72"
    INDEPENDENT_LABORATORY = "81"
    OTHER_UNLISTED_FACILITY = "99"

    def visit(
        self,
        pharmacy: typing.Callable[[], T_Result],
        telehealth: typing.Callable[[], T_Result],
        school: typing.Callable[[], T_Result],
        homeless_shelter: typing.Callable[[], T_Result],
        indian_health_service_free_standing: typing.Callable[[], T_Result],
        indian_health_service_provider_based: typing.Callable[[], T_Result],
        tribal_free_standing: typing.Callable[[], T_Result],
        tribal_provider_based: typing.Callable[[], T_Result],
        prison_or_correctional_facility: typing.Callable[[], T_Result],
        telehealth_patient_home: typing.Callable[[], T_Result],
        office: typing.Callable[[], T_Result],
        home: typing.Callable[[], T_Result],
        assisted_living_facility: typing.Callable[[], T_Result],
        group_home: typing.Callable[[], T_Result],
        mobile_unit: typing.Callable[[], T_Result],
        temporary_lodging: typing.Callable[[], T_Result],
        walk_in_retail_health_clinic: typing.Callable[[], T_Result],
        place_of_employment_worksite: typing.Callable[[], T_Result],
        off_campus_outpatient_hospital: typing.Callable[[], T_Result],
        urgent_care_facility: typing.Callable[[], T_Result],
        inpatient_hospital: typing.Callable[[], T_Result],
        outpatient_hospital: typing.Callable[[], T_Result],
        emergency_room_hospital: typing.Callable[[], T_Result],
        ambulatory_surgical_center: typing.Callable[[], T_Result],
        birthing_center: typing.Callable[[], T_Result],
        military_treatment_facility: typing.Callable[[], T_Result],
        skilled_nursing_facility: typing.Callable[[], T_Result],
        nursing_facility: typing.Callable[[], T_Result],
        custodial_care_facility: typing.Callable[[], T_Result],
        hospice: typing.Callable[[], T_Result],
        ambulance_land: typing.Callable[[], T_Result],
        ambulance_air_or_water: typing.Callable[[], T_Result],
        independent_clinic: typing.Callable[[], T_Result],
        federally_qualified_health_center: typing.Callable[[], T_Result],
        inpatient_psychiatric_facility: typing.Callable[[], T_Result],
        psychiatric_facility_partial_hospitalization: typing.Callable[[], T_Result],
        community_mental_health_center: typing.Callable[[], T_Result],
        intermediate_care_facility_mentally_retarded: typing.Callable[[], T_Result],
        residential_substance_abuse_treatment_facility: typing.Callable[[], T_Result],
        psychiatric_residential_treatment_center: typing.Callable[[], T_Result],
        non_residential_substance_abuse_treatment_facility: typing.Callable[[], T_Result],
        non_residential_opioid_treatment_facility: typing.Callable[[], T_Result],
        mass_immunization_center: typing.Callable[[], T_Result],
        comprehensive_inpatient_rehabilitation_facility: typing.Callable[[], T_Result],
        comprehensive_outpatient_rehabilitation_facility: typing.Callable[[], T_Result],
        end_stage_renal_disease_treatment_facility: typing.Callable[[], T_Result],
        state_or_local_public_health_clinic: typing.Callable[[], T_Result],
        rural_health_clinic: typing.Callable[[], T_Result],
        independent_laboratory: typing.Callable[[], T_Result],
        other_unlisted_facility: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FacilityTypeCode.PHARMACY:
            return pharmacy()
        if self is FacilityTypeCode.TELEHEALTH:
            return telehealth()
        if self is FacilityTypeCode.SCHOOL:
            return school()
        if self is FacilityTypeCode.HOMELESS_SHELTER:
            return homeless_shelter()
        if self is FacilityTypeCode.INDIAN_HEALTH_SERVICE_FREE_STANDING:
            return indian_health_service_free_standing()
        if self is FacilityTypeCode.INDIAN_HEALTH_SERVICE_PROVIDER_BASED:
            return indian_health_service_provider_based()
        if self is FacilityTypeCode.TRIBAL_FREE_STANDING:
            return tribal_free_standing()
        if self is FacilityTypeCode.TRIBAL_PROVIDER_BASED:
            return tribal_provider_based()
        if self is FacilityTypeCode.PRISON_OR_CORRECTIONAL_FACILITY:
            return prison_or_correctional_facility()
        if self is FacilityTypeCode.TELEHEALTH_PATIENT_HOME:
            return telehealth_patient_home()
        if self is FacilityTypeCode.OFFICE:
            return office()
        if self is FacilityTypeCode.HOME:
            return home()
        if self is FacilityTypeCode.ASSISTED_LIVING_FACILITY:
            return assisted_living_facility()
        if self is FacilityTypeCode.GROUP_HOME:
            return group_home()
        if self is FacilityTypeCode.MOBILE_UNIT:
            return mobile_unit()
        if self is FacilityTypeCode.TEMPORARY_LODGING:
            return temporary_lodging()
        if self is FacilityTypeCode.WALK_IN_RETAIL_HEALTH_CLINIC:
            return walk_in_retail_health_clinic()
        if self is FacilityTypeCode.PLACE_OF_EMPLOYMENT_WORKSITE:
            return place_of_employment_worksite()
        if self is FacilityTypeCode.OFF_CAMPUS_OUTPATIENT_HOSPITAL:
            return off_campus_outpatient_hospital()
        if self is FacilityTypeCode.URGENT_CARE_FACILITY:
            return urgent_care_facility()
        if self is FacilityTypeCode.INPATIENT_HOSPITAL:
            return inpatient_hospital()
        if self is FacilityTypeCode.OUTPATIENT_HOSPITAL:
            return outpatient_hospital()
        if self is FacilityTypeCode.EMERGENCY_ROOM_HOSPITAL:
            return emergency_room_hospital()
        if self is FacilityTypeCode.AMBULATORY_SURGICAL_CENTER:
            return ambulatory_surgical_center()
        if self is FacilityTypeCode.BIRTHING_CENTER:
            return birthing_center()
        if self is FacilityTypeCode.MILITARY_TREATMENT_FACILITY:
            return military_treatment_facility()
        if self is FacilityTypeCode.SKILLED_NURSING_FACILITY:
            return skilled_nursing_facility()
        if self is FacilityTypeCode.NURSING_FACILITY:
            return nursing_facility()
        if self is FacilityTypeCode.CUSTODIAL_CARE_FACILITY:
            return custodial_care_facility()
        if self is FacilityTypeCode.HOSPICE:
            return hospice()
        if self is FacilityTypeCode.AMBULANCE_LAND:
            return ambulance_land()
        if self is FacilityTypeCode.AMBULANCE_AIR_OR_WATER:
            return ambulance_air_or_water()
        if self is FacilityTypeCode.INDEPENDENT_CLINIC:
            return independent_clinic()
        if self is FacilityTypeCode.FEDERALLY_QUALIFIED_HEALTH_CENTER:
            return federally_qualified_health_center()
        if self is FacilityTypeCode.INPATIENT_PSYCHIATRIC_FACILITY:
            return inpatient_psychiatric_facility()
        if self is FacilityTypeCode.PSYCHIATRIC_FACILITY_PARTIAL_HOSPITALIZATION:
            return psychiatric_facility_partial_hospitalization()
        if self is FacilityTypeCode.COMMUNITY_MENTAL_HEALTH_CENTER:
            return community_mental_health_center()
        if self is FacilityTypeCode.INTERMEDIATE_CARE_FACILITY_MENTALLY_RETARDED:
            return intermediate_care_facility_mentally_retarded()
        if self is FacilityTypeCode.RESIDENTIAL_SUBSTANCE_ABUSE_TREATMENT_FACILITY:
            return residential_substance_abuse_treatment_facility()
        if self is FacilityTypeCode.PSYCHIATRIC_RESIDENTIAL_TREATMENT_CENTER:
            return psychiatric_residential_treatment_center()
        if self is FacilityTypeCode.NON_RESIDENTIAL_SUBSTANCE_ABUSE_TREATMENT_FACILITY:
            return non_residential_substance_abuse_treatment_facility()
        if self is FacilityTypeCode.NON_RESIDENTIAL_OPIOID_TREATMENT_FACILITY:
            return non_residential_opioid_treatment_facility()
        if self is FacilityTypeCode.MASS_IMMUNIZATION_CENTER:
            return mass_immunization_center()
        if self is FacilityTypeCode.COMPREHENSIVE_INPATIENT_REHABILITATION_FACILITY:
            return comprehensive_inpatient_rehabilitation_facility()
        if self is FacilityTypeCode.COMPREHENSIVE_OUTPATIENT_REHABILITATION_FACILITY:
            return comprehensive_outpatient_rehabilitation_facility()
        if self is FacilityTypeCode.END_STAGE_RENAL_DISEASE_TREATMENT_FACILITY:
            return end_stage_renal_disease_treatment_facility()
        if self is FacilityTypeCode.STATE_OR_LOCAL_PUBLIC_HEALTH_CLINIC:
            return state_or_local_public_health_clinic()
        if self is FacilityTypeCode.RURAL_HEALTH_CLINIC:
            return rural_health_clinic()
        if self is FacilityTypeCode.INDEPENDENT_LABORATORY:
            return independent_laboratory()
        if self is FacilityTypeCode.OTHER_UNLISTED_FACILITY:
            return other_unlisted_facility()
