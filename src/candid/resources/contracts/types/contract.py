# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import uuid

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...organization_providers.resources.v_2.types.organization_provider import OrganizationProvider
from ...payers.types.payer import Payer
from .contract_base import ContractBase
from .contract_id import ContractId


class Contract(ContractBase):
    contract_id: ContractId
    contracting_provider: OrganizationProvider = pydantic.Field(description=("The provider under contract\n"))
    rendering_providers: typing.Dict[uuid.UUID, OrganizationProvider] = pydantic.Field(
        description=("The providers who can render medical services under the contract\n")
    )
    payer: typing.Optional[Payer] = pydantic.Field(description=("The insurance company under contract\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
