# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import CandidApiEnvironment
from .resources.auth.client import AsyncAuthClient, AuthClient
from .resources.billing_notes.client import AsyncBillingNotesClient, BillingNotesClient
from .resources.eligibility.client import AsyncEligibilityClient, EligibilityClient
from .resources.encounters.client import AsyncEncountersClient, EncountersClient
from .resources.expected_network_status.client import AsyncExpectedNetworkStatusClient, ExpectedNetworkStatusClient
from .resources.exports.client import AsyncExportsClient, ExportsClient
from .resources.guarantor.client import AsyncGuarantorClient, GuarantorClient
from .resources.insurance_adjudications.client import AsyncInsuranceAdjudicationsClient, InsuranceAdjudicationsClient
from .resources.insurance_refunds.client import AsyncInsuranceRefundsClient, InsuranceRefundsClient
from .resources.organization_providers.client import AsyncOrganizationProvidersClient, OrganizationProvidersClient
from .resources.organization_service_facilities.client import (
    AsyncOrganizationServiceFacilitiesClient,
    OrganizationServiceFacilitiesClient,
)
from .resources.patient_payments.client import AsyncPatientPaymentsClient, PatientPaymentsClient
from .resources.patient_refunds.client import AsyncPatientRefundsClient, PatientRefundsClient
from .resources.payers.client import AsyncPayersClient, PayersClient
from .resources.tasks.client import AsyncTasksClient, TasksClient
from .resources.write_offs.client import AsyncWriteOffsClient, WriteOffsClient


class CandidApi:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.auth = AuthClient(client_wrapper=self._client_wrapper)
        self.billing_notes = BillingNotesClient(client_wrapper=self._client_wrapper)
        self.eligibility = EligibilityClient(client_wrapper=self._client_wrapper)
        self.encounters = EncountersClient(client_wrapper=self._client_wrapper)
        self.expected_network_status = ExpectedNetworkStatusClient(client_wrapper=self._client_wrapper)
        self.exports = ExportsClient(client_wrapper=self._client_wrapper)
        self.guarantor = GuarantorClient(client_wrapper=self._client_wrapper)
        self.insurance_adjudications = InsuranceAdjudicationsClient(client_wrapper=self._client_wrapper)
        self.insurance_refunds = InsuranceRefundsClient(client_wrapper=self._client_wrapper)
        self.organization_service_facilities = OrganizationServiceFacilitiesClient(client_wrapper=self._client_wrapper)
        self.organization_providers = OrganizationProvidersClient(client_wrapper=self._client_wrapper)
        self.patient_payments = PatientPaymentsClient(client_wrapper=self._client_wrapper)
        self.patient_refunds = PatientRefundsClient(client_wrapper=self._client_wrapper)
        self.payers = PayersClient(client_wrapper=self._client_wrapper)
        self.tasks = TasksClient(client_wrapper=self._client_wrapper)
        self.write_offs = WriteOffsClient(client_wrapper=self._client_wrapper)


class AsyncCandidApi:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        self.billing_notes = AsyncBillingNotesClient(client_wrapper=self._client_wrapper)
        self.eligibility = AsyncEligibilityClient(client_wrapper=self._client_wrapper)
        self.encounters = AsyncEncountersClient(client_wrapper=self._client_wrapper)
        self.expected_network_status = AsyncExpectedNetworkStatusClient(client_wrapper=self._client_wrapper)
        self.exports = AsyncExportsClient(client_wrapper=self._client_wrapper)
        self.guarantor = AsyncGuarantorClient(client_wrapper=self._client_wrapper)
        self.insurance_adjudications = AsyncInsuranceAdjudicationsClient(client_wrapper=self._client_wrapper)
        self.insurance_refunds = AsyncInsuranceRefundsClient(client_wrapper=self._client_wrapper)
        self.organization_service_facilities = AsyncOrganizationServiceFacilitiesClient(
            client_wrapper=self._client_wrapper
        )
        self.organization_providers = AsyncOrganizationProvidersClient(client_wrapper=self._client_wrapper)
        self.patient_payments = AsyncPatientPaymentsClient(client_wrapper=self._client_wrapper)
        self.patient_refunds = AsyncPatientRefundsClient(client_wrapper=self._client_wrapper)
        self.payers = AsyncPayersClient(client_wrapper=self._client_wrapper)
        self.tasks = AsyncTasksClient(client_wrapper=self._client_wrapper)
        self.write_offs = AsyncWriteOffsClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: CandidApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
