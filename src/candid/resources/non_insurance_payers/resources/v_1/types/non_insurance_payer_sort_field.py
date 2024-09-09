# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NonInsurancePayerSortField(str, enum.Enum):
    NAME = "NAME"
    CATEGORY = "CATEGORY"
    ENABLED = "ENABLED"
    UPDATED_AT = "UPDATED_AT"

    def visit(
        self,
        name: typing.Callable[[], T_Result],
        category: typing.Callable[[], T_Result],
        enabled: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NonInsurancePayerSortField.NAME:
            return name()
        if self is NonInsurancePayerSortField.CATEGORY:
            return category()
        if self is NonInsurancePayerSortField.ENABLED:
            return enabled()
        if self is NonInsurancePayerSortField.UPDATED_AT:
            return updated_at()
