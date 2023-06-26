# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BillableStatusType(str, enum.Enum):
    BILLABLE = "BILLABLE"
    NOT_BILLABLE = "NOT_BILLABLE"

    def visit(self, billable: typing.Callable[[], T_Result], not_billable: typing.Callable[[], T_Result]) -> T_Result:
        if self is BillableStatusType.BILLABLE:
            return billable()
        if self is BillableStatusType.NOT_BILLABLE:
            return not_billable()
