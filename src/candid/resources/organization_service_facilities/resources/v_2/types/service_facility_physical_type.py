# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ServiceFacilityPhysicalType(str, enum.Enum):
    """
    from candid.resources.organization_service_facilities.v_2 import (
        ServiceFacilityPhysicalType,
    )

    ServiceFacilityPhysicalType.SI
    """

    SITE = "si"
    """
    A collection of buildings or other locations such as a site or a campus.
    """

    BUILDING = "bu"
    """
    Any Building or structure. This may contain rooms, corridors, wings, etc. It might not have walls, or a roof, but is considered a defined/allocated space.
    """

    WING = "wi"
    """
    A Wing within a Building, this often contains levels, rooms and corridors.
    """

    WARD = "wa"
    """
    A Ward is a section of a medical facility that may contain rooms and other types of location.
    """

    LEVEL = "lvl"
    """
    A Level in a multi-level Building/Structure.
    """

    CORRIDOR = "co"
    """
    A Corridor within a Building.
    """

    ROOM = "ro"
    """
    A space that is allocated as a room, it may have walls/roof etc., but does not require these.
    """

    BED = "bd"
    """
    A space that is allocated for sleeping/laying on etc. typically within a building, section of a building or within a room.
    """

    VEHICLE = "ve"
    """
    A means of transportation.
    """

    HOUSE = "ho"
    """
    A residential dwelling. Usually used to reference a location that a person/patient may reside.
    """

    CABINET = "ca"
    """
    A container that can store goods, equipment, medications or other items.
    """

    ROAD = "rd"
    """
    A defined path to travel between 2 points that has a known name.
    """

    AREA = "area"
    """
    A defined physical boundary of something, such as a flood risk zone, region, postcode.
    """

    JURISDICTION = "jdn"
    """
    A wide scope that covers a conceptual domain, such as a Nation (Country wide community or Federal Government - e.g.  Ministry of Health), Province or State (community or Government), Business (throughout the enterprise), Nation with a business  scope of an agency (e.g. CDC, FDA etc.) or a Business segment (UK Pharmacy), not just an physical boundary.
    """

    def visit(
        self,
        site: typing.Callable[[], T_Result],
        building: typing.Callable[[], T_Result],
        wing: typing.Callable[[], T_Result],
        ward: typing.Callable[[], T_Result],
        level: typing.Callable[[], T_Result],
        corridor: typing.Callable[[], T_Result],
        room: typing.Callable[[], T_Result],
        bed: typing.Callable[[], T_Result],
        vehicle: typing.Callable[[], T_Result],
        house: typing.Callable[[], T_Result],
        cabinet: typing.Callable[[], T_Result],
        road: typing.Callable[[], T_Result],
        area: typing.Callable[[], T_Result],
        jurisdiction: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceFacilityPhysicalType.SITE:
            return site()
        if self is ServiceFacilityPhysicalType.BUILDING:
            return building()
        if self is ServiceFacilityPhysicalType.WING:
            return wing()
        if self is ServiceFacilityPhysicalType.WARD:
            return ward()
        if self is ServiceFacilityPhysicalType.LEVEL:
            return level()
        if self is ServiceFacilityPhysicalType.CORRIDOR:
            return corridor()
        if self is ServiceFacilityPhysicalType.ROOM:
            return room()
        if self is ServiceFacilityPhysicalType.BED:
            return bed()
        if self is ServiceFacilityPhysicalType.VEHICLE:
            return vehicle()
        if self is ServiceFacilityPhysicalType.HOUSE:
            return house()
        if self is ServiceFacilityPhysicalType.CABINET:
            return cabinet()
        if self is ServiceFacilityPhysicalType.ROAD:
            return road()
        if self is ServiceFacilityPhysicalType.AREA:
            return area()
        if self is ServiceFacilityPhysicalType.JURISDICTION:
            return jurisdiction()
