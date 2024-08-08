# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from ..environment import CandidApiClientEnvironment
from .http_client import AsyncHttpClient, HttpClient


class BaseClientWrapper:
    def __init__(
        self,
        *,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        environment: CandidApiClientEnvironment,
        timeout: typing.Optional[float] = None,
    ):
        self._token = token
        self._environment = environment
        self._timeout = timeout

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "candidhealth",
            "X-Fern-SDK-Version": "0.24.6",
        }
        token = self._get_token()
        if token is not None:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    def _get_token(self) -> typing.Optional[str]:
        if isinstance(self._token, str) or self._token is None:
            return self._token
        else:
            return self._token()

    def get_environment(self) -> CandidApiClientEnvironment:
        return self._environment

    def get_timeout(self) -> typing.Optional[float]:
        return self._timeout


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        environment: CandidApiClientEnvironment,
        timeout: typing.Optional[float] = None,
        httpx_client: httpx.Client,
    ):
        super().__init__(token=token, environment=environment, timeout=timeout)
        self.httpx_client = HttpClient(
            httpx_client=httpx_client, base_headers=self.get_headers(), base_timeout=self.get_timeout()
        )


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        environment: CandidApiClientEnvironment,
        timeout: typing.Optional[float] = None,
        httpx_client: httpx.AsyncClient,
    ):
        super().__init__(token=token, environment=environment, timeout=timeout)
        self.httpx_client = AsyncHttpClient(
            httpx_client=httpx_client, base_headers=self.get_headers(), base_timeout=self.get_timeout()
        )
