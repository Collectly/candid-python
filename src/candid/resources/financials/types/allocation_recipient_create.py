# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.claim_id import ClaimId
from ...commons.types.provider_id import ProviderId
from ...commons.types.service_line_id import ServiceLineId


class AllocationRecipientCreate_ServiceLineById(pydantic.BaseModel):
    type: typing_extensions.Literal["service_line_by_id"]
    value: ServiceLineId

    class Config:
        frozen = True
        smart_union = True


class AllocationRecipientCreate_ClaimById(pydantic.BaseModel):
    type: typing_extensions.Literal["claim_by_id"]
    value: ClaimId

    class Config:
        frozen = True
        smart_union = True


class AllocationRecipientCreate_BillingProviderById(pydantic.BaseModel):
    type: typing_extensions.Literal["billing_provider_by_id"]
    value: ProviderId

    class Config:
        frozen = True
        smart_union = True


AllocationRecipientCreate = typing.Union[
    AllocationRecipientCreate_ServiceLineById,
    AllocationRecipientCreate_ClaimById,
    AllocationRecipientCreate_BillingProviderById,
]
