# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .medicaid_provider_identifier import MedicaidProviderIdentifier
from .medicare_provider_identifier import MedicareProviderIdentifier


class IdentifierValue_MedicareProviderIdentifier(MedicareProviderIdentifier):
    type: typing_extensions.Literal["medicare_provider_identifier"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class IdentifierValue_MedicaidProviderIdentifier(MedicaidProviderIdentifier):
    type: typing_extensions.Literal["medicaid_provider_identifier"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


IdentifierValue = typing.Union[IdentifierValue_MedicareProviderIdentifier, IdentifierValue_MedicaidProviderIdentifier]