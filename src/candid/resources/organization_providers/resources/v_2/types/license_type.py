# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LicenseType(str, enum.Enum):
    MD = "MD"
    NP = "NP"
    PA = "PA"
    LMFT = "LMFT"
    LCPC = "LCPC"
    LCSW = "LCSW"
    PMHNP = "PMHNP"
    FNP = "FNP"
    LPCC = "LPCC"
    DO = "DO"
    RD = "RD"
    SLP = "SLP"
    APRN = "APRN"
    LPC = "LPC"
    PHD = "PHD"
    PSYD = "PSYD"
    LMSW = "LMSW"
    LMHC = "LMHC"
    OTHER_MASTERS = "OTHER_MASTERS"
    BCBA = "BCBA"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        md: typing.Callable[[], T_Result],
        np: typing.Callable[[], T_Result],
        pa: typing.Callable[[], T_Result],
        lmft: typing.Callable[[], T_Result],
        lcpc: typing.Callable[[], T_Result],
        lcsw: typing.Callable[[], T_Result],
        pmhnp: typing.Callable[[], T_Result],
        fnp: typing.Callable[[], T_Result],
        lpcc: typing.Callable[[], T_Result],
        do: typing.Callable[[], T_Result],
        rd: typing.Callable[[], T_Result],
        slp: typing.Callable[[], T_Result],
        aprn: typing.Callable[[], T_Result],
        lpc: typing.Callable[[], T_Result],
        phd: typing.Callable[[], T_Result],
        psyd: typing.Callable[[], T_Result],
        lmsw: typing.Callable[[], T_Result],
        lmhc: typing.Callable[[], T_Result],
        other_masters: typing.Callable[[], T_Result],
        bcba: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LicenseType.MD:
            return md()
        if self is LicenseType.NP:
            return np()
        if self is LicenseType.PA:
            return pa()
        if self is LicenseType.LMFT:
            return lmft()
        if self is LicenseType.LCPC:
            return lcpc()
        if self is LicenseType.LCSW:
            return lcsw()
        if self is LicenseType.PMHNP:
            return pmhnp()
        if self is LicenseType.FNP:
            return fnp()
        if self is LicenseType.LPCC:
            return lpcc()
        if self is LicenseType.DO:
            return do()
        if self is LicenseType.RD:
            return rd()
        if self is LicenseType.SLP:
            return slp()
        if self is LicenseType.APRN:
            return aprn()
        if self is LicenseType.LPC:
            return lpc()
        if self is LicenseType.PHD:
            return phd()
        if self is LicenseType.PSYD:
            return psyd()
        if self is LicenseType.LMSW:
            return lmsw()
        if self is LicenseType.LMHC:
            return lmhc()
        if self is LicenseType.OTHER_MASTERS:
            return other_masters()
        if self is LicenseType.BCBA:
            return bcba()
        if self is LicenseType.UNKNOWN:
            return unknown()
