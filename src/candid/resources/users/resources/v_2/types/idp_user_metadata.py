# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .auth_zero_metadata import AuthZeroMetadata
from .google_apps_metadata import GoogleAppsMetadata
from .other_idp_metadata import OtherIdpMetadata


class IdpUserMetadata_AuthZeroMetadata(AuthZeroMetadata):
    type: typing_extensions.Literal["auth_zero_metadata"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class IdpUserMetadata_GoogleAppsMetadata(GoogleAppsMetadata):
    type: typing_extensions.Literal["google_apps_metadata"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class IdpUserMetadata_OtherIdpMetadata(OtherIdpMetadata):
    type: typing_extensions.Literal["other_idp_metadata"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


IdpUserMetadata = typing.Union[
    IdpUserMetadata_AuthZeroMetadata, IdpUserMetadata_GoogleAppsMetadata, IdpUserMetadata_OtherIdpMetadata
]