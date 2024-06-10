# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import pydantic_v1
from .....core.request_options import RequestOptions
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

    def get(
        self,
        organization_service_facility_id: OrganizationServiceFacilityId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationServiceFacility:
        """
        Parameters
        ----------
        organization_service_facility_id : OrganizationServiceFacilityId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationServiceFacility

        Examples
        --------
        import uuid

        from candid.client import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.organization_service_facilities.v_2.get(
            organization_service_facility_id=uuid.UUID(
                "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/organization-service-facilities/v2/{jsonable_encoder(organization_service_facility_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(OrganizationServiceFacility, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationServiceFacilityPage:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Limit the number of results returned. Defaults to 100.

        name : typing.Optional[str]
            Filter to a name or a part of a name.

        page_token : typing.Optional[PageToken]
            The page token to continue paging through a previous request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationServiceFacilityPage

        Examples
        --------
        from candid.client import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.organization_service_facilities.v_2.get_multi(
            limit=100,
            name="Test Service Facility",
            page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/organization-service-facilities/v2",
            method="GET",
            params={"limit": limit, "name": name, "page_token": page_token},
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(OrganizationServiceFacilityPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self, *, request: OrganizationServiceFacilityCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationServiceFacility:
        """
        Parameters
        ----------
        request : OrganizationServiceFacilityCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationServiceFacility

        Examples
        --------
        from candid import State, StreetAddressLongZip
        from candid.client import CandidApiClient
        from candid.resources.organization_service_facilities.v_2 import (
            OrganizationServiceFacilityCreate,
            ServiceFacilityMode,
            ServiceFacilityOperationalStatus,
            ServiceFacilityPhysicalType,
            ServiceFacilityStatus,
            ServiceFacilityType,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.organization_service_facilities.v_2.create(
            request=OrganizationServiceFacilityCreate(
                name="Test Service Facility",
                aliases=["Test Service Facility Alias"],
                description="Test Service Facility Description",
                status=ServiceFacilityStatus.ACTIVE,
                operational_status=ServiceFacilityOperationalStatus.CLOSED,
                mode=ServiceFacilityMode.INSTANCE,
                type=ServiceFacilityType.DIAGNOSTICS_OR_THERAPEUTICS_UNIT,
                physical_type=ServiceFacilityPhysicalType.SITE,
                telecoms=["555-555-5555"],
                address=StreetAddressLongZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/organization-service-facilities/v2",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(OrganizationServiceFacility, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic_v1.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        organization_service_facility_id: OrganizationServiceFacilityId,
        *,
        request: OrganizationServiceFacilityUpdate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationServiceFacility:
        """
        Parameters
        ----------
        organization_service_facility_id : OrganizationServiceFacilityId

        request : OrganizationServiceFacilityUpdate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationServiceFacility

        Examples
        --------
        import uuid

        from candid import State, StreetAddressLongZip
        from candid.client import CandidApiClient
        from candid.resources.organization_service_facilities.v_2 import (
            OrganizationServiceFacilityUpdate,
            ServiceFacilityMode,
            ServiceFacilityOperationalStatus,
            ServiceFacilityPhysicalType,
            ServiceFacilityStatus,
            ServiceFacilityType,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.organization_service_facilities.v_2.update(
            organization_service_facility_id=uuid.UUID(
                "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
            ),
            request=OrganizationServiceFacilityUpdate(
                name="Test Service Facility",
                aliases=["Test Service Facility Alias"],
                description="Test Service Facility Description",
                status=ServiceFacilityStatus.ACTIVE,
                operational_status=ServiceFacilityOperationalStatus.CLOSED,
                mode=ServiceFacilityMode.INSTANCE,
                type=ServiceFacilityType.DIAGNOSTICS_OR_THERAPEUTICS_UNIT,
                physical_type=ServiceFacilityPhysicalType.SITE,
                telecoms=["555-555-5555"],
                address=StreetAddressLongZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/organization-service-facilities/v2/{jsonable_encoder(organization_service_facility_id)}",
            method="PATCH",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(OrganizationServiceFacility, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic_v1.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self,
        organization_service_facility_id: OrganizationServiceFacilityId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organization_service_facility_id : OrganizationServiceFacilityId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import uuid

        from candid.client import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.organization_service_facilities.v_2.delete(
            organization_service_facility_id=uuid.UUID(
                "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/organization-service-facilities/v2/{jsonable_encoder(organization_service_facility_id)}",
            method="DELETE",
            request_options=request_options,
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
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        organization_service_facility_id: OrganizationServiceFacilityId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationServiceFacility:
        """
        Parameters
        ----------
        organization_service_facility_id : OrganizationServiceFacilityId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationServiceFacility

        Examples
        --------
        import uuid

        from candid.client import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.organization_service_facilities.v_2.get(
            organization_service_facility_id=uuid.UUID(
                "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/organization-service-facilities/v2/{jsonable_encoder(organization_service_facility_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(OrganizationServiceFacility, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationServiceFacilityPage:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Limit the number of results returned. Defaults to 100.

        name : typing.Optional[str]
            Filter to a name or a part of a name.

        page_token : typing.Optional[PageToken]
            The page token to continue paging through a previous request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationServiceFacilityPage

        Examples
        --------
        from candid.client import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.organization_service_facilities.v_2.get_multi(
            limit=100,
            name="Test Service Facility",
            page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/organization-service-facilities/v2",
            method="GET",
            params={"limit": limit, "name": name, "page_token": page_token},
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(OrganizationServiceFacilityPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self, *, request: OrganizationServiceFacilityCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationServiceFacility:
        """
        Parameters
        ----------
        request : OrganizationServiceFacilityCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationServiceFacility

        Examples
        --------
        from candid import State, StreetAddressLongZip
        from candid.client import AsyncCandidApiClient
        from candid.resources.organization_service_facilities.v_2 import (
            OrganizationServiceFacilityCreate,
            ServiceFacilityMode,
            ServiceFacilityOperationalStatus,
            ServiceFacilityPhysicalType,
            ServiceFacilityStatus,
            ServiceFacilityType,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.organization_service_facilities.v_2.create(
            request=OrganizationServiceFacilityCreate(
                name="Test Service Facility",
                aliases=["Test Service Facility Alias"],
                description="Test Service Facility Description",
                status=ServiceFacilityStatus.ACTIVE,
                operational_status=ServiceFacilityOperationalStatus.CLOSED,
                mode=ServiceFacilityMode.INSTANCE,
                type=ServiceFacilityType.DIAGNOSTICS_OR_THERAPEUTICS_UNIT,
                physical_type=ServiceFacilityPhysicalType.SITE,
                telecoms=["555-555-5555"],
                address=StreetAddressLongZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/organization-service-facilities/v2",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(OrganizationServiceFacility, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic_v1.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        organization_service_facility_id: OrganizationServiceFacilityId,
        *,
        request: OrganizationServiceFacilityUpdate,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationServiceFacility:
        """
        Parameters
        ----------
        organization_service_facility_id : OrganizationServiceFacilityId

        request : OrganizationServiceFacilityUpdate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationServiceFacility

        Examples
        --------
        import uuid

        from candid import State, StreetAddressLongZip
        from candid.client import AsyncCandidApiClient
        from candid.resources.organization_service_facilities.v_2 import (
            OrganizationServiceFacilityUpdate,
            ServiceFacilityMode,
            ServiceFacilityOperationalStatus,
            ServiceFacilityPhysicalType,
            ServiceFacilityStatus,
            ServiceFacilityType,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.organization_service_facilities.v_2.update(
            organization_service_facility_id=uuid.UUID(
                "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
            ),
            request=OrganizationServiceFacilityUpdate(
                name="Test Service Facility",
                aliases=["Test Service Facility Alias"],
                description="Test Service Facility Description",
                status=ServiceFacilityStatus.ACTIVE,
                operational_status=ServiceFacilityOperationalStatus.CLOSED,
                mode=ServiceFacilityMode.INSTANCE,
                type=ServiceFacilityType.DIAGNOSTICS_OR_THERAPEUTICS_UNIT,
                physical_type=ServiceFacilityPhysicalType.SITE,
                telecoms=["555-555-5555"],
                address=StreetAddressLongZip(
                    address_1="123 Main St",
                    address_2="Apt 1",
                    city="New York",
                    state=State.NY,
                    zip_code="10001",
                    zip_plus_four_code="1234",
                ),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/organization-service-facilities/v2/{jsonable_encoder(organization_service_facility_id)}",
            method="PATCH",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(OrganizationServiceFacility, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationError":
                raise HttpRequestValidationError(
                    pydantic_v1.parse_obj_as(RequestValidationError, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self,
        organization_service_facility_id: OrganizationServiceFacilityId,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organization_service_facility_id : OrganizationServiceFacilityId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import uuid

        from candid.client import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.organization_service_facilities.v_2.delete(
            organization_service_facility_id=uuid.UUID(
                "30f55ee6-8c0e-43fc-a7fc-dac00d5bf569",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/organization-service-facilities/v2/{jsonable_encoder(organization_service_facility_id)}",
            method="DELETE",
            request_options=request_options,
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
                    pydantic_v1.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
