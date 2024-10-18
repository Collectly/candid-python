# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.oauth_token_provider import OAuthTokenProvider
from .environment import CandidApiClientEnvironment
from .resources.auth.client import AsyncAuthClient, AuthClient
from .resources.billing_notes.client import AsyncBillingNotesClient, BillingNotesClient
from .resources.contracts.client import AsyncContractsClient, ContractsClient
from .resources.credentialing.client import AsyncCredentialingClient, CredentialingClient
from .resources.custom_schemas.client import AsyncCustomSchemasClient, CustomSchemasClient
from .resources.diagnoses.client import AsyncDiagnosesClient, DiagnosesClient
from .resources.eligibility.client import AsyncEligibilityClient, EligibilityClient
from .resources.encounter_providers.client import AsyncEncounterProvidersClient, EncounterProvidersClient
from .resources.encounters.client import AsyncEncountersClient, EncountersClient
from .resources.expected_network_status.client import AsyncExpectedNetworkStatusClient, ExpectedNetworkStatusClient
from .resources.exports.client import AsyncExportsClient, ExportsClient
from .resources.external_payment_account_config.client import (
    AsyncExternalPaymentAccountConfigClient,
    ExternalPaymentAccountConfigClient,
)
from .resources.fee_schedules.client import AsyncFeeSchedulesClient, FeeSchedulesClient
from .resources.guarantor.client import AsyncGuarantorClient, GuarantorClient
from .resources.import_invoice.client import AsyncImportInvoiceClient, ImportInvoiceClient
from .resources.insurance_adjudications.client import AsyncInsuranceAdjudicationsClient, InsuranceAdjudicationsClient
from .resources.insurance_payments.client import AsyncInsurancePaymentsClient, InsurancePaymentsClient
from .resources.insurance_refunds.client import AsyncInsuranceRefundsClient, InsuranceRefundsClient
from .resources.medication_dispense.client import AsyncMedicationDispenseClient, MedicationDispenseClient
from .resources.non_insurance_payer_payments.client import (
    AsyncNonInsurancePayerPaymentsClient,
    NonInsurancePayerPaymentsClient,
)
from .resources.non_insurance_payer_refunds.client import (
    AsyncNonInsurancePayerRefundsClient,
    NonInsurancePayerRefundsClient,
)
from .resources.non_insurance_payers.client import AsyncNonInsurancePayersClient, NonInsurancePayersClient
from .resources.organization_providers.client import AsyncOrganizationProvidersClient, OrganizationProvidersClient
from .resources.organization_service_facilities.client import (
    AsyncOrganizationServiceFacilitiesClient,
    OrganizationServiceFacilitiesClient,
)
from .resources.patient_payments.client import AsyncPatientPaymentsClient, PatientPaymentsClient
from .resources.patient_refunds.client import AsyncPatientRefundsClient, PatientRefundsClient
from .resources.payers.client import AsyncPayersClient, PayersClient
from .resources.pre_encounter.client import AsyncPreEncounterClient, PreEncounterClient
from .resources.service_facility.client import AsyncServiceFacilityClient, ServiceFacilityClient
from .resources.service_lines.client import AsyncServiceLinesClient, ServiceLinesClient
from .resources.tasks.client import AsyncTasksClient, TasksClient
from .resources.write_offs.client import AsyncWriteOffsClient, WriteOffsClient


class CandidApiClient:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    environment : CandidApiClientEnvironment
        The environment to use for requests from the client. from .environment import CandidApiClientEnvironment



        Defaults to CandidApiClientEnvironment.PRODUCTION



    client_id : str
    client_secret : str
    _token_getter_override : typing.Optional[typing.Callable[[], str]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from candid.client import CandidApiClient

    client = CandidApiClient(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    )
    """

    def __init__(
        self,
        *,
        environment: CandidApiClientEnvironment = CandidApiClientEnvironment.PRODUCTION,
        client_id: str,
        client_secret: str,
        _token_getter_override: typing.Optional[typing.Callable[[], str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        oauth_token_provider = OAuthTokenProvider(
            client_id=client_id,
            client_secret=client_secret,
            client_wrapper=SyncClientWrapper(
                environment=environment,
                httpx_client=httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
                if follow_redirects is not None
                else httpx.Client(timeout=_defaulted_timeout),
                timeout=_defaulted_timeout,
            ),
        )
        self._client_wrapper = SyncClientWrapper(
            environment=environment,
            token=_token_getter_override if _token_getter_override is not None else oauth_token_provider.get_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.auth = AuthClient(client_wrapper=self._client_wrapper)
        self.billing_notes = BillingNotesClient(client_wrapper=self._client_wrapper)
        self.contracts = ContractsClient(client_wrapper=self._client_wrapper)
        self.credentialing = CredentialingClient(client_wrapper=self._client_wrapper)
        self.custom_schemas = CustomSchemasClient(client_wrapper=self._client_wrapper)
        self.eligibility = EligibilityClient(client_wrapper=self._client_wrapper)
        self.encounter_providers = EncounterProvidersClient(client_wrapper=self._client_wrapper)
        self.encounters = EncountersClient(client_wrapper=self._client_wrapper)
        self.expected_network_status = ExpectedNetworkStatusClient(client_wrapper=self._client_wrapper)
        self.exports = ExportsClient(client_wrapper=self._client_wrapper)
        self.external_payment_account_config = ExternalPaymentAccountConfigClient(client_wrapper=self._client_wrapper)
        self.fee_schedules = FeeSchedulesClient(client_wrapper=self._client_wrapper)
        self.guarantor = GuarantorClient(client_wrapper=self._client_wrapper)
        self.import_invoice = ImportInvoiceClient(client_wrapper=self._client_wrapper)
        self.insurance_adjudications = InsuranceAdjudicationsClient(client_wrapper=self._client_wrapper)
        self.insurance_payments = InsurancePaymentsClient(client_wrapper=self._client_wrapper)
        self.insurance_refunds = InsuranceRefundsClient(client_wrapper=self._client_wrapper)
        self.medication_dispense = MedicationDispenseClient(client_wrapper=self._client_wrapper)
        self.non_insurance_payer_payments = NonInsurancePayerPaymentsClient(client_wrapper=self._client_wrapper)
        self.non_insurance_payer_refunds = NonInsurancePayerRefundsClient(client_wrapper=self._client_wrapper)
        self.non_insurance_payers = NonInsurancePayersClient(client_wrapper=self._client_wrapper)
        self.organization_service_facilities = OrganizationServiceFacilitiesClient(client_wrapper=self._client_wrapper)
        self.organization_providers = OrganizationProvidersClient(client_wrapper=self._client_wrapper)
        self.patient_payments = PatientPaymentsClient(client_wrapper=self._client_wrapper)
        self.patient_refunds = PatientRefundsClient(client_wrapper=self._client_wrapper)
        self.payers = PayersClient(client_wrapper=self._client_wrapper)
        self.service_lines = ServiceLinesClient(client_wrapper=self._client_wrapper)
        self.tasks = TasksClient(client_wrapper=self._client_wrapper)
        self.write_offs = WriteOffsClient(client_wrapper=self._client_wrapper)
        self.pre_encounter = PreEncounterClient(client_wrapper=self._client_wrapper)
        self.diagnoses = DiagnosesClient(client_wrapper=self._client_wrapper)
        self.service_facility = ServiceFacilityClient(client_wrapper=self._client_wrapper)


class AsyncCandidApiClient:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    environment : CandidApiClientEnvironment
        The environment to use for requests from the client. from .environment import CandidApiClientEnvironment



        Defaults to CandidApiClientEnvironment.PRODUCTION



    client_id : str
    client_secret : str
    _token_getter_override : typing.Optional[typing.Callable[[], str]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from candid.client import AsyncCandidApiClient

    client = AsyncCandidApiClient(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    )
    """

    def __init__(
        self,
        *,
        environment: CandidApiClientEnvironment = CandidApiClientEnvironment.PRODUCTION,
        client_id: str,
        client_secret: str,
        _token_getter_override: typing.Optional[typing.Callable[[], str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        oauth_token_provider = OAuthTokenProvider(
            client_id=client_id,
            client_secret=client_secret,
            client_wrapper=SyncClientWrapper(
                environment=environment,
                httpx_client=httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
                if follow_redirects is not None
                else httpx.Client(timeout=_defaulted_timeout),
                timeout=_defaulted_timeout,
            ),
        )
        self._client_wrapper = AsyncClientWrapper(
            environment=environment,
            token=_token_getter_override if _token_getter_override is not None else oauth_token_provider.get_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        self.billing_notes = AsyncBillingNotesClient(client_wrapper=self._client_wrapper)
        self.contracts = AsyncContractsClient(client_wrapper=self._client_wrapper)
        self.credentialing = AsyncCredentialingClient(client_wrapper=self._client_wrapper)
        self.custom_schemas = AsyncCustomSchemasClient(client_wrapper=self._client_wrapper)
        self.eligibility = AsyncEligibilityClient(client_wrapper=self._client_wrapper)
        self.encounter_providers = AsyncEncounterProvidersClient(client_wrapper=self._client_wrapper)
        self.encounters = AsyncEncountersClient(client_wrapper=self._client_wrapper)
        self.expected_network_status = AsyncExpectedNetworkStatusClient(client_wrapper=self._client_wrapper)
        self.exports = AsyncExportsClient(client_wrapper=self._client_wrapper)
        self.external_payment_account_config = AsyncExternalPaymentAccountConfigClient(
            client_wrapper=self._client_wrapper
        )
        self.fee_schedules = AsyncFeeSchedulesClient(client_wrapper=self._client_wrapper)
        self.guarantor = AsyncGuarantorClient(client_wrapper=self._client_wrapper)
        self.import_invoice = AsyncImportInvoiceClient(client_wrapper=self._client_wrapper)
        self.insurance_adjudications = AsyncInsuranceAdjudicationsClient(client_wrapper=self._client_wrapper)
        self.insurance_payments = AsyncInsurancePaymentsClient(client_wrapper=self._client_wrapper)
        self.insurance_refunds = AsyncInsuranceRefundsClient(client_wrapper=self._client_wrapper)
        self.medication_dispense = AsyncMedicationDispenseClient(client_wrapper=self._client_wrapper)
        self.non_insurance_payer_payments = AsyncNonInsurancePayerPaymentsClient(client_wrapper=self._client_wrapper)
        self.non_insurance_payer_refunds = AsyncNonInsurancePayerRefundsClient(client_wrapper=self._client_wrapper)
        self.non_insurance_payers = AsyncNonInsurancePayersClient(client_wrapper=self._client_wrapper)
        self.organization_service_facilities = AsyncOrganizationServiceFacilitiesClient(
            client_wrapper=self._client_wrapper
        )
        self.organization_providers = AsyncOrganizationProvidersClient(client_wrapper=self._client_wrapper)
        self.patient_payments = AsyncPatientPaymentsClient(client_wrapper=self._client_wrapper)
        self.patient_refunds = AsyncPatientRefundsClient(client_wrapper=self._client_wrapper)
        self.payers = AsyncPayersClient(client_wrapper=self._client_wrapper)
        self.service_lines = AsyncServiceLinesClient(client_wrapper=self._client_wrapper)
        self.tasks = AsyncTasksClient(client_wrapper=self._client_wrapper)
        self.write_offs = AsyncWriteOffsClient(client_wrapper=self._client_wrapper)
        self.pre_encounter = AsyncPreEncounterClient(client_wrapper=self._client_wrapper)
        self.diagnoses = AsyncDiagnosesClient(client_wrapper=self._client_wrapper)
        self.service_facility = AsyncServiceFacilityClient(client_wrapper=self._client_wrapper)
