# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MeasurementUnitCode(str, enum.Enum):
    MILLILITERS = "ML"
    UNITS = "UN"
    GRAMS = "GR"
    INTERNATIONAL_UNIT = "F2"
    MILLIGRAM = "ME"

    def visit(
        self,
        milliliters: typing.Callable[[], T_Result],
        units: typing.Callable[[], T_Result],
        grams: typing.Callable[[], T_Result],
        international_unit: typing.Callable[[], T_Result],
        milligram: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MeasurementUnitCode.MILLILITERS:
            return milliliters()
        if self is MeasurementUnitCode.UNITS:
            return units()
        if self is MeasurementUnitCode.GRAMS:
            return grams()
        if self is MeasurementUnitCode.INTERNATIONAL_UNIT:
            return international_unit()
        if self is MeasurementUnitCode.MILLIGRAM:
            return milligram()