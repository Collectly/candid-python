# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from ....commons.errors.entity_not_found_error import EntityNotFoundError
from ....commons.errors.http_request_validation_error import HttpRequestValidationError
from ....commons.types.entity_not_found_error_message import EntityNotFoundErrorMessage
from ....commons.types.page_token import PageToken
from ....commons.types.request_validation_error import RequestValidationError
from .types.organization_service_facility import OrganizationServiceFacility
from .types.organization_service_facility_create import OrganizationServiceFacilityCreate
from .types.organization_service_facility_id import OrganizationServiceFacilityId
from .types.organization_service_facility_page import OrganizationServiceFacilityPage
from .types.organization_service_facility_update import OrganizationServiceFacilityUpdate

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, organization_service_facility_id: OrganizationServiceFacilityId) -> OrganizationServiceFacility:
        """
        Parameters:
            - organization_service_facility_id: OrganizationServiceFacilityId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/organization-service-facilities/v2/{organization_service_facility_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationServiceFacility, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        page_token: typing.Optional[PageToken] = None,
    ) -> OrganizationServiceFacilityPage:
        """
        Parameters:
            - limit: typing.Optional[int]. Limit the number of results returned. Defaults to 100.

            - name: typing.Optional[str]. Filter to a name or a part of a name.

            - page_token: typing.Optional[PageToken]. The page token to continue paging through a previous request.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/organization-service-facilities/v2"),
            params=remove_none_from_dict({"limit": limit, "name": name, "page_token": page_token}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationServiceFacilityPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request: OrganizationServiceFacilityCreate) -> OrganizationServiceFacility:
        """
        Parameters:
            - request: OrganizationServiceFacilityCreate.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/organization-service-facilities/v2"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationServiceFacility, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        organization_service_facility_id: OrganizationServiceFacilityId,
        *,
        request: OrganizationServiceFacilityUpdate,
    ) -> OrganizationServiceFacility:
        """
        Parameters:
            - organization_service_facility_id: OrganizationServiceFacilityId.

            - request: OrganizationServiceFacilityUpdate.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/organization-service-facilities/v2/{organization_service_facility_id}",
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationServiceFacility, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, organization_service_facility_id: OrganizationServiceFacilityId) -> None:
        """
        Parameters:
            - organization_service_facility_id: OrganizationServiceFacilityId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/organization-service-facilities/v2/{organization_service_facility_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, organization_service_facility_id: OrganizationServiceFacilityId) -> OrganizationServiceFacility:
        """
        Parameters:
            - organization_service_facility_id: OrganizationServiceFacilityId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/organization-service-facilities/v2/{organization_service_facility_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationServiceFacility, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        page_token: typing.Optional[PageToken] = None,
    ) -> OrganizationServiceFacilityPage:
        """
        Parameters:
            - limit: typing.Optional[int]. Limit the number of results returned. Defaults to 100.

            - name: typing.Optional[str]. Filter to a name or a part of a name.

            - page_token: typing.Optional[PageToken]. The page token to continue paging through a previous request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/organization-service-facilities/v2"),
            params=remove_none_from_dict({"limit": limit, "name": name, "page_token": page_token}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationServiceFacilityPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, request: OrganizationServiceFacilityCreate) -> OrganizationServiceFacility:
        """
        Parameters:
            - request: OrganizationServiceFacilityCreate.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/organization-service-facilities/v2"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationServiceFacility, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        organization_service_facility_id: OrganizationServiceFacilityId,
        *,
        request: OrganizationServiceFacilityUpdate,
    ) -> OrganizationServiceFacility:
        """
        Parameters:
            - organization_service_facility_id: OrganizationServiceFacilityId.

            - request: OrganizationServiceFacilityUpdate.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/organization-service-facilities/v2/{organization_service_facility_id}",
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(OrganizationServiceFacility, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, organization_service_facility_id: OrganizationServiceFacilityId) -> None:
        """
        Parameters:
            - organization_service_facility_id: OrganizationServiceFacilityId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/organization-service-facilities/v2/{organization_service_facility_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
