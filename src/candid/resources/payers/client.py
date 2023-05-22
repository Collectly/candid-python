# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
import uuid
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import CandidApiEnvironment
from ..commons.types.page_token import PageToken
from .types.payer import Payer
from .types.payer_page import PayerPage


class PayersClient:
    def __init__(self, *, environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token

    def get(self, payer_uuid: uuid.UUID) -> Payer:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"api/payers/v3/{payer_uuid}"),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Payer, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        search_term: typing.Optional[str] = None,
        page_token: typing.Optional[PageToken] = None,
    ) -> PayerPage:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/payers/v3"),
            params={"limit": limit, "search_term": search_term, "page_token": page_token},
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PayerPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPayersClient:
    def __init__(self, *, environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token

    async def get(self, payer_uuid: uuid.UUID) -> Payer:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"api/payers/v3/{payer_uuid}"),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Payer, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        search_term: typing.Optional[str] = None,
        page_token: typing.Optional[PageToken] = None,
    ) -> PayerPage:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "api/payers/v3"),
                params={"limit": limit, "search_term": search_term, "page_token": page_token},
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PayerPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
