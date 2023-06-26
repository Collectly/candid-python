# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PhoneNumberType(str, enum.Enum):
    HOME = "Home"
    MOBILE = "Mobile"
    WORK = "Work"

    def visit(
        self,
        home: typing.Callable[[], T_Result],
        mobile: typing.Callable[[], T_Result],
        work: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PhoneNumberType.HOME:
            return home()
        if self is PhoneNumberType.MOBILE:
            return mobile()
        if self is PhoneNumberType.WORK:
            return work()