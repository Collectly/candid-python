# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from ....commons.types.claim_id import ClaimId
from ....commons.types.invoice_id import InvoiceId
from ....commons.types.page_token import PageToken
from ....commons.types.patient_external_id import PatientExternalId
from ....commons.types.provider_id import ProviderId
from ....commons.types.service_line_id import ServiceLineId
from ....commons.types.sort_direction import SortDirection
from ....financials.types.allocation_create import AllocationCreate
from ....financials.types.patient_transaction_source import PatientTransactionSource
from .types.patient_payment import PatientPayment
from .types.patient_payment_id import PatientPaymentId
from .types.patient_payment_sort_field import PatientPaymentSortField
from .types.patient_payments_page import PatientPaymentsPage

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V4Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        patient_external_id: typing.Optional[PatientExternalId] = None,
        claim_id: typing.Optional[ClaimId] = None,
        service_line_id: typing.Optional[ServiceLineId] = None,
        billing_provider_id: typing.Optional[ProviderId] = None,
        invoice_id: typing.Optional[InvoiceId] = None,
        sources: typing.Optional[typing.Union[PatientTransactionSource, typing.List[PatientTransactionSource]]] = None,
        sort: typing.Optional[PatientPaymentSortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        page_token: typing.Optional[PageToken] = None,
    ) -> PatientPaymentsPage:
        """
        Returns all patient payments satisfying the search criteria AND whose organization_id matches
        the current organization_id of the authenticated user.

        Parameters:
            - limit: typing.Optional[int]. Defaults to 100. The value must be greater than 0 and less than 1000.

            - patient_external_id: typing.Optional[PatientExternalId].

            - claim_id: typing.Optional[ClaimId].

            - service_line_id: typing.Optional[ServiceLineId].

            - billing_provider_id: typing.Optional[ProviderId].

            - invoice_id: typing.Optional[InvoiceId].

            - sources: typing.Optional[typing.Union[PatientTransactionSource, typing.List[PatientTransactionSource]]].

            - sort: typing.Optional[PatientPaymentSortField]. Defaults to payment_timestamp

            - sort_direction: typing.Optional[SortDirection]. Sort direction. Defaults to descending order if not provided.

            - page_token: typing.Optional[PageToken].
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/patient-payments/v4"),
            params=remove_none_from_dict(
                {
                    "limit": limit,
                    "patient_external_id": patient_external_id,
                    "claim_id": jsonable_encoder(claim_id),
                    "service_line_id": jsonable_encoder(service_line_id),
                    "billing_provider_id": jsonable_encoder(billing_provider_id),
                    "invoice_id": jsonable_encoder(invoice_id),
                    "sources": sources,
                    "sort": sort,
                    "sort_direction": sort_direction,
                    "page_token": page_token,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatientPaymentsPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, patient_payment_id: PatientPaymentId) -> PatientPayment:
        """
        Retrieves a previously created patient payment by its `patient_payment_id`.

        Parameters:
            - patient_payment_id: PatientPaymentId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/patient-payments/v4/{patient_payment_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatientPayment, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        amount_cents: int,
        payment_timestamp: typing.Optional[dt.datetime] = OMIT,
        payment_note: typing.Optional[str] = OMIT,
        patient_external_id: PatientExternalId,
        allocations: typing.List[AllocationCreate],
        invoice: typing.Optional[InvoiceId] = OMIT,
    ) -> PatientPayment:
        """
        Creates a new patient payment record and returns the newly created PatientPayment object.
        The allocations can describe whether the payment is being applied toward a specific service line,
        claim, or billing provider.

        Parameters:
            - amount_cents: int.

            - payment_timestamp: typing.Optional[dt.datetime].

            - payment_note: typing.Optional[str].

            - patient_external_id: PatientExternalId.

            - allocations: typing.List[AllocationCreate].

            - invoice: typing.Optional[InvoiceId].
        """
        _request: typing.Dict[str, typing.Any] = {
            "amount_cents": amount_cents,
            "patient_external_id": patient_external_id,
            "allocations": allocations,
        }
        if payment_timestamp is not OMIT:
            _request["payment_timestamp"] = payment_timestamp
        if payment_note is not OMIT:
            _request["payment_note"] = payment_note
        if invoice is not OMIT:
            _request["invoice"] = invoice
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/patient-payments/v4"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatientPayment, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, patient_payment_id: PatientPaymentId) -> None:
        """
        Deletes the patient payment record matching the provided patient_payment_id.

        Parameters:
            - patient_payment_id: PatientPaymentId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/patient-payments/v4/{patient_payment_id}"
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


class AsyncV4Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        patient_external_id: typing.Optional[PatientExternalId] = None,
        claim_id: typing.Optional[ClaimId] = None,
        service_line_id: typing.Optional[ServiceLineId] = None,
        billing_provider_id: typing.Optional[ProviderId] = None,
        invoice_id: typing.Optional[InvoiceId] = None,
        sources: typing.Optional[typing.Union[PatientTransactionSource, typing.List[PatientTransactionSource]]] = None,
        sort: typing.Optional[PatientPaymentSortField] = None,
        sort_direction: typing.Optional[SortDirection] = None,
        page_token: typing.Optional[PageToken] = None,
    ) -> PatientPaymentsPage:
        """
        Returns all patient payments satisfying the search criteria AND whose organization_id matches
        the current organization_id of the authenticated user.

        Parameters:
            - limit: typing.Optional[int]. Defaults to 100. The value must be greater than 0 and less than 1000.

            - patient_external_id: typing.Optional[PatientExternalId].

            - claim_id: typing.Optional[ClaimId].

            - service_line_id: typing.Optional[ServiceLineId].

            - billing_provider_id: typing.Optional[ProviderId].

            - invoice_id: typing.Optional[InvoiceId].

            - sources: typing.Optional[typing.Union[PatientTransactionSource, typing.List[PatientTransactionSource]]].

            - sort: typing.Optional[PatientPaymentSortField]. Defaults to payment_timestamp

            - sort_direction: typing.Optional[SortDirection]. Sort direction. Defaults to descending order if not provided.

            - page_token: typing.Optional[PageToken].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/patient-payments/v4"),
            params=remove_none_from_dict(
                {
                    "limit": limit,
                    "patient_external_id": patient_external_id,
                    "claim_id": jsonable_encoder(claim_id),
                    "service_line_id": jsonable_encoder(service_line_id),
                    "billing_provider_id": jsonable_encoder(billing_provider_id),
                    "invoice_id": jsonable_encoder(invoice_id),
                    "sources": sources,
                    "sort": sort,
                    "sort_direction": sort_direction,
                    "page_token": page_token,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatientPaymentsPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, patient_payment_id: PatientPaymentId) -> PatientPayment:
        """
        Retrieves a previously created patient payment by its `patient_payment_id`.

        Parameters:
            - patient_payment_id: PatientPaymentId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/patient-payments/v4/{patient_payment_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatientPayment, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        amount_cents: int,
        payment_timestamp: typing.Optional[dt.datetime] = OMIT,
        payment_note: typing.Optional[str] = OMIT,
        patient_external_id: PatientExternalId,
        allocations: typing.List[AllocationCreate],
        invoice: typing.Optional[InvoiceId] = OMIT,
    ) -> PatientPayment:
        """
        Creates a new patient payment record and returns the newly created PatientPayment object.
        The allocations can describe whether the payment is being applied toward a specific service line,
        claim, or billing provider.

        Parameters:
            - amount_cents: int.

            - payment_timestamp: typing.Optional[dt.datetime].

            - payment_note: typing.Optional[str].

            - patient_external_id: PatientExternalId.

            - allocations: typing.List[AllocationCreate].

            - invoice: typing.Optional[InvoiceId].
        """
        _request: typing.Dict[str, typing.Any] = {
            "amount_cents": amount_cents,
            "patient_external_id": patient_external_id,
            "allocations": allocations,
        }
        if payment_timestamp is not OMIT:
            _request["payment_timestamp"] = payment_timestamp
        if payment_note is not OMIT:
            _request["payment_note"] = payment_note
        if invoice is not OMIT:
            _request["invoice"] = invoice
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/patient-payments/v4"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PatientPayment, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, patient_payment_id: PatientPaymentId) -> None:
        """
        Deletes the patient payment record matching the provided patient_payment_id.

        Parameters:
            - patient_payment_id: PatientPaymentId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/patient-payments/v4/{patient_payment_id}"
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
