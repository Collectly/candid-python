# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.pydantic_utilities import pydantic_v1
from .....core.request_options import RequestOptions
from .errors.too_many_requests_error import TooManyRequestsError
from .types.auth_get_token_response import AuthGetTokenResponse
from .types.too_many_requests_error_type import TooManyRequestsErrorType

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_token(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthGetTokenResponse:
        """
        Authenticating with the Candid Health API.

        Candid Health utilizes the [OAuth 2.0 bearer token authentication scheme](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) in our auth flow. You obtain the bearer token for all
        subsequent API requests via the `/auth/token` endpoint defined below, which requires you to provide your `client_id` and `client_secret`. Your `client_id` and `client_secret` can be [generated](https://support.joincandidhealth.com/hc/en-us/articles/23065219476244--Generating-Candid-API-Keys) from the "Users & Credentials" tab by your org admin.

        The bearer token should be provided in the `Authorization` header for all subsequent API calls.

        **Warning:**

        The bearer token expires 5 hours after it has been created. After it has expired, the client will receive an "HTTP 401
        Unauthorized" error, at which point the client should generate a new token. It is important that tokens be reused between requests; if the client attempts to generate a token too often, it will be rate-limited and will receive an "HTTP 429 Too Many Requests" error.

        Parameters
        ----------
        client_id : str
            Your application's Client ID.

        client_secret : str
            Your application's Client Secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthGetTokenResponse

        Examples
        --------
        from candid.client import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.auth.v_2.get_token(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/auth/v2/token",
            method="POST",
            json={"client_id": client_id, "client_secret": client_secret},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(AuthGetTokenResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "TooManyRequestsError":
                raise TooManyRequestsError(
                    pydantic_v1.parse_obj_as(TooManyRequestsErrorType, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_token(
        self, *, client_id: str, client_secret: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthGetTokenResponse:
        """
        Authenticating with the Candid Health API.

        Candid Health utilizes the [OAuth 2.0 bearer token authentication scheme](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) in our auth flow. You obtain the bearer token for all
        subsequent API requests via the `/auth/token` endpoint defined below, which requires you to provide your `client_id` and `client_secret`. Your `client_id` and `client_secret` can be [generated](https://support.joincandidhealth.com/hc/en-us/articles/23065219476244--Generating-Candid-API-Keys) from the "Users & Credentials" tab by your org admin.

        The bearer token should be provided in the `Authorization` header for all subsequent API calls.

        **Warning:**

        The bearer token expires 5 hours after it has been created. After it has expired, the client will receive an "HTTP 401
        Unauthorized" error, at which point the client should generate a new token. It is important that tokens be reused between requests; if the client attempts to generate a token too often, it will be rate-limited and will receive an "HTTP 429 Too Many Requests" error.

        Parameters
        ----------
        client_id : str
            Your application's Client ID.

        client_secret : str
            Your application's Client Secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthGetTokenResponse

        Examples
        --------
        from candid.client import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.auth.v_2.get_token(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/auth/v2/token",
            method="POST",
            json={"client_id": client_id, "client_secret": client_secret},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(AuthGetTokenResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "TooManyRequestsError":
                raise TooManyRequestsError(
                    pydantic_v1.parse_obj_as(TooManyRequestsErrorType, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
