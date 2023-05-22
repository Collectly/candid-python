# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import CandidApiEnvironment
from ..commons.types.date import Date
from ..commons.types.insurance_type_code import InsuranceTypeCode
from ..commons.types.state import State
from .types.expected_network_status_response import ExpectedNetworkStatusResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ExpectedNetworkStatusClient:
    def __init__(self, *, environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token

    def compute(
        self,
        *,
        external_patient_id: typing.Optional[str] = OMIT,
        subscriber_payer_id: str,
        subscriber_payer_name: str,
        subscriber_insurance_type: typing.Optional[InsuranceTypeCode] = OMIT,
        subscriber_plan_name: typing.Optional[str] = OMIT,
        billing_provider_npi: str,
        billing_provider_tin: str,
        rendering_provider_npi: str,
        contracted_state: State,
        date_of_service: Date,
    ) -> ExpectedNetworkStatusResponse:
        _request: typing.Dict[str, typing.Any] = {
            "subscriber_payer_id": subscriber_payer_id,
            "subscriber_payer_name": subscriber_payer_name,
            "billing_provider_npi": billing_provider_npi,
            "billing_provider_tin": billing_provider_tin,
            "rendering_provider_npi": rendering_provider_npi,
            "contracted_state": contracted_state,
            "date_of_service": date_of_service,
        }
        if external_patient_id is not OMIT:
            _request["external_patient_id"] = external_patient_id
        if subscriber_insurance_type is not OMIT:
            _request["subscriber_insurance_type"] = subscriber_insurance_type
        if subscriber_plan_name is not OMIT:
            _request["subscriber_plan_name"] = subscriber_plan_name
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/expected-network-status/v1"),
            json=jsonable_encoder(_request),
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
            return pydantic.parse_obj_as(ExpectedNetworkStatusResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncExpectedNetworkStatusClient:
    def __init__(self, *, environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token

    async def compute(
        self,
        *,
        external_patient_id: typing.Optional[str] = OMIT,
        subscriber_payer_id: str,
        subscriber_payer_name: str,
        subscriber_insurance_type: typing.Optional[InsuranceTypeCode] = OMIT,
        subscriber_plan_name: typing.Optional[str] = OMIT,
        billing_provider_npi: str,
        billing_provider_tin: str,
        rendering_provider_npi: str,
        contracted_state: State,
        date_of_service: Date,
    ) -> ExpectedNetworkStatusResponse:
        _request: typing.Dict[str, typing.Any] = {
            "subscriber_payer_id": subscriber_payer_id,
            "subscriber_payer_name": subscriber_payer_name,
            "billing_provider_npi": billing_provider_npi,
            "billing_provider_tin": billing_provider_tin,
            "rendering_provider_npi": rendering_provider_npi,
            "contracted_state": contracted_state,
            "date_of_service": date_of_service,
        }
        if external_patient_id is not OMIT:
            _request["external_patient_id"] = external_patient_id
        if subscriber_insurance_type is not OMIT:
            _request["subscriber_insurance_type"] = subscriber_insurance_type
        if subscriber_plan_name is not OMIT:
            _request["subscriber_plan_name"] = subscriber_plan_name
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "api/expected-network-status/v1"),
                json=jsonable_encoder(_request),
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
            return pydantic.parse_obj_as(ExpectedNetworkStatusResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
