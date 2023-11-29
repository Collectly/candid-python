# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .types.insurance_adjudication import InsuranceAdjudication
from .types.insurance_adjudication_create import InsuranceAdjudicationCreate
from .types.insurance_adjudication_id import InsuranceAdjudicationId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, insurance_adjudication_id: InsuranceAdjudicationId) -> InsuranceAdjudication:
        """
        Retrieves a previously created insurance adjudication by its `insurance_adjudication_id`.

        Parameters:
            - insurance_adjudication_id: InsuranceAdjudicationId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/insurance-adjudications/v1/{insurance_adjudication_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InsuranceAdjudication, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request: InsuranceAdjudicationCreate) -> InsuranceAdjudication:
        """
        Creates a new insurance adjudication record and returns the newly created InsuranceAdjudication object.

        Parameters:
            - request: InsuranceAdjudicationCreate.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/insurance-adjudications/v1"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InsuranceAdjudication, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, insurance_adjudication_id: InsuranceAdjudicationId) -> None:
        """
        Deletes the insurance adjudication record matching the provided insurance_adjudication_id.

        Parameters:
            - insurance_adjudication_id: InsuranceAdjudicationId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/insurance-adjudications/v1/{insurance_adjudication_id}"
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
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, insurance_adjudication_id: InsuranceAdjudicationId) -> InsuranceAdjudication:
        """
        Retrieves a previously created insurance adjudication by its `insurance_adjudication_id`.

        Parameters:
            - insurance_adjudication_id: InsuranceAdjudicationId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/insurance-adjudications/v1/{insurance_adjudication_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InsuranceAdjudication, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, request: InsuranceAdjudicationCreate) -> InsuranceAdjudication:
        """
        Creates a new insurance adjudication record and returns the newly created InsuranceAdjudication object.

        Parameters:
            - request: InsuranceAdjudicationCreate.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/insurance-adjudications/v1"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InsuranceAdjudication, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, insurance_adjudication_id: InsuranceAdjudicationId) -> None:
        """
        Deletes the insurance adjudication record matching the provided insurance_adjudication_id.

        Parameters:
            - insurance_adjudication_id: InsuranceAdjudicationId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/insurance-adjudications/v1/{insurance_adjudication_id}"
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
        raise ApiError(status_code=_response.status_code, body=_response_json)
