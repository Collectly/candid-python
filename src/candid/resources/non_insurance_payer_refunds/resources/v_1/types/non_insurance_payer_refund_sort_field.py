# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NonInsurancePayerRefundSortField(str, enum.Enum):
    AMOUNT_CENTS = "amount_cents"
    REFUND_TIMESTAMP = "refund_timestamp"

    def visit(
        self, amount_cents: typing.Callable[[], T_Result], refund_timestamp: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is NonInsurancePayerRefundSortField.AMOUNT_CENTS:
            return amount_cents()
        if self is NonInsurancePayerRefundSortField.REFUND_TIMESTAMP:
            return refund_timestamp()
