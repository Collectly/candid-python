# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NameUse(str, enum.Enum):
    USUAL = "USUAL"
    OFFICIAL = "OFFICIAL"
    TEMP = "TEMP"
    NICKNAME = "NICKNAME"
    ANONYMOUS = "ANONYMOUS"
    OLD = "OLD"
    MAIDEN = "MAIDEN"

    def visit(
        self,
        usual: typing.Callable[[], T_Result],
        official: typing.Callable[[], T_Result],
        temp: typing.Callable[[], T_Result],
        nickname: typing.Callable[[], T_Result],
        anonymous: typing.Callable[[], T_Result],
        old: typing.Callable[[], T_Result],
        maiden: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NameUse.USUAL:
            return usual()
        if self is NameUse.OFFICIAL:
            return official()
        if self is NameUse.TEMP:
            return temp()
        if self is NameUse.NICKNAME:
            return nickname()
        if self is NameUse.ANONYMOUS:
            return anonymous()
        if self is NameUse.OLD:
            return old()
        if self is NameUse.MAIDEN:
            return maiden()
