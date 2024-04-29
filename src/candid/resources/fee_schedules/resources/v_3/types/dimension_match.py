# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .match_cpt_code import MatchCptCode
from .match_date import MatchDate
from .match_facility_type_code import MatchFacilityTypeCode
from .match_geo import MatchGeo
from .match_license_type import MatchLicenseType
from .match_modifiers import MatchModifiers
from .match_network_types import MatchNetworkTypes
from .match_payer import MatchPayer
from .match_provider import MatchProvider

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DimensionMatch(pydantic.BaseModel):
    """
    Dimension matching for a service line
    """

    payer: MatchPayer
    geography: MatchGeo
    organization_billing_provider: MatchProvider
    date_of_service: MatchDate
    cpt_code: MatchCptCode
    modifiers: MatchModifiers
    license_type: MatchLicenseType
    facility_type_code: MatchFacilityTypeCode
    network_types: MatchNetworkTypes

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
