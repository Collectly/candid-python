# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import pydantic_v1
from .....core.request_options import RequestOptions
from ....commons.types.page_token import PageToken
from .types.payer import Payer
from .types.payer_page import PayerPage
from .types.payer_uuid import PayerUuid


class V3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, payer_uuid: PayerUuid, *, request_options: typing.Optional[RequestOptions] = None) -> Payer:
        """
        Parameters
        ----------
        payer_uuid : PayerUuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payer

        Examples
        --------
        import uuid

        from candid.client import CandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = CandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.payers.v_3.get(payer_uuid=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", ), )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/payers/v3/{jsonable_encoder(payer_uuid)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Payer, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        search_term: typing.Optional[str] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayerPage:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of entities per page, defaults to 100.

        search_term : typing.Optional[str]

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPage

        Examples
        --------
        from candid.client import CandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = CandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        client.payers.v_3.get_all(limit=100, search_term='john', page_token='eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9', )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/payers/v3",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            params={"limit": limit, "search_term": search_term, "page_token": page_token},
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PayerPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, payer_uuid: PayerUuid, *, request_options: typing.Optional[RequestOptions] = None) -> Payer:
        """
        Parameters
        ----------
        payer_uuid : PayerUuid

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payer

        Examples
        --------
        import asyncio
        import uuid

        from candid.client import AsyncCandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = AsyncCandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.payers.v_3.get(payer_uuid=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", ), )
        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/payers/v3/{jsonable_encoder(payer_uuid)}",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Payer, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        search_term: typing.Optional[str] = None,
        page_token: typing.Optional[PageToken] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PayerPage:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of entities per page, defaults to 100.

        search_term : typing.Optional[str]

        page_token : typing.Optional[PageToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PayerPage

        Examples
        --------
        import asyncio

        from candid.client import AsyncCandidApiClient
        from candid.environment import CandidApiClientEnvironment

        client = AsyncCandidApiClient(environment=CandidApiClientEnvironment., client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", )
        async def main() -> None:
            await client.payers.v_3.get_all(limit=100, search_term='john', page_token='eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9', )
        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/payers/v3",
            base_url=self._client_wrapper.get_environment().candid_api,
            method="GET",
            params={"limit": limit, "search_term": search_term, "page_token": page_token},
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PayerPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
