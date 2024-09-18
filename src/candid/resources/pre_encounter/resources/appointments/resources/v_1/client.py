# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .......core.api_error import ApiError
from .......core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .......core.jsonable_encoder import jsonable_encoder
from .......core.pydantic_utilities import pydantic_v1
from .......core.request_options import RequestOptions
from ....common.errors.not_found_error import NotFoundError
from ....common.errors.version_conflict_error import VersionConflictError
from ....common.types.appointment_id import AppointmentId
from ....common.types.not_found_error_body import NotFoundErrorBody
from ....common.types.version_conflict_error_body import VersionConflictErrorBody
from .types.appointment import Appointment
from .types.mutable_appointment import MutableAppointment

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self, *, request: MutableAppointment, request_options: typing.Optional[RequestOptions] = None
    ) -> Appointment:
        """
        Adds an appointment. VersionConflictError is returned when the placer_appointment_id is already in use.

        Parameters
        ----------
        request : MutableAppointment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Appointment

        Examples
        --------
        import datetime

        from candid.client import CandidApiClient
        from candid.resources.pre_encounter.appointments.v_1 import (
            AppointmentStatus,
            AppointmentWorkQueue,
            MutableAppointment,
            Service,
            UniversalServiceIdentifier,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.pre_encounter.appointments.v_1.create(
            request=MutableAppointment(
                patient_id="string",
                start_timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                status=AppointmentStatus.PENDING,
                service_duration=1,
                services=[
                    Service(
                        universal_service_identifier=UniversalServiceIdentifier.MD_VISIT,
                        start_timestamp=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                    )
                ],
                placer_appointment_id="string",
                estimated_copay_cents=1,
                estimated_patient_responsibility_cents=1,
                patient_deposit_cents=1,
                checked_in_timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                notes="string",
                location_resource_id="string",
                automated_eligibility_check_complete=True,
                work_queue=AppointmentWorkQueue.EMERGENT_ISSUE,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "appointments/v1",
            base_url=self._client_wrapper.get_environment().pre_encounter,
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
            return pydantic_v1.parse_obj_as(Appointment, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "VersionConflictError":
                raise VersionConflictError(
                    pydantic_v1.parse_obj_as(VersionConflictErrorBody, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: AppointmentId, *, request_options: typing.Optional[RequestOptions] = None) -> Appointment:
        """
        Gets an appointment.

        Parameters
        ----------
        id : AppointmentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Appointment

        Examples
        --------
        from candid.client import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.pre_encounter.appointments.v_1.get(
            id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"appointments/v1/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Appointment, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_history(
        self, id: AppointmentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Appointment]:
        """
        Gets an appointment along with it's full history. The return list is ordered by version ascending.

        Parameters
        ----------
        id : AppointmentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Appointment]

        Examples
        --------
        from candid.client import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.pre_encounter.appointments.v_1.get_history(
            id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"appointments/v1/{jsonable_encoder(id)}/history",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Appointment], _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: AppointmentId,
        version: str,
        *,
        request: MutableAppointment,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Appointment:
        """
        Updates an appointment. The path must contain the most recent version to prevent race conditions. Updating historic versions is not supported.

        Parameters
        ----------
        id : AppointmentId

        version : str

        request : MutableAppointment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Appointment

        Examples
        --------
        import datetime

        from candid.client import CandidApiClient
        from candid.resources.pre_encounter.appointments.v_1 import (
            AppointmentStatus,
            AppointmentWorkQueue,
            MutableAppointment,
            Service,
            UniversalServiceIdentifier,
        )

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.pre_encounter.appointments.v_1.update(
            id="string",
            version="string",
            request=MutableAppointment(
                patient_id="string",
                start_timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                status=AppointmentStatus.PENDING,
                service_duration=1,
                services=[
                    Service(
                        universal_service_identifier=UniversalServiceIdentifier.MD_VISIT,
                        start_timestamp=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                    )
                ],
                placer_appointment_id="string",
                estimated_copay_cents=1,
                estimated_patient_responsibility_cents=1,
                patient_deposit_cents=1,
                checked_in_timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                notes="string",
                location_resource_id="string",
                automated_eligibility_check_complete=True,
                work_queue=AppointmentWorkQueue.EMERGENT_ISSUE,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"appointments/v1/{jsonable_encoder(id)}/{jsonable_encoder(version)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="PUT",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Appointment, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "VersionConflictError":
                raise VersionConflictError(
                    pydantic_v1.parse_obj_as(VersionConflictErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def deactivate(
        self, id: AppointmentId, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Sets an appointment as deactivated. The path must contain the most recent version to prevent race conditions. Deactivating historic versions is not supported. Subsequent updates via PUT to the appointment will "reactivate" the appointment and set the deactivated flag to false.

        Parameters
        ----------
        id : AppointmentId

        version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from candid.client import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.pre_encounter.appointments.v_1.deactivate(
            id="string",
            version="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"appointments/v1/{jsonable_encoder(id)}/{jsonable_encoder(version)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
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
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "VersionConflictError":
                raise VersionConflictError(
                    pydantic_v1.parse_obj_as(VersionConflictErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self, *, request: MutableAppointment, request_options: typing.Optional[RequestOptions] = None
    ) -> Appointment:
        """
        Adds an appointment. VersionConflictError is returned when the placer_appointment_id is already in use.

        Parameters
        ----------
        request : MutableAppointment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Appointment

        Examples
        --------
        import asyncio
        import datetime

        from candid.client import AsyncCandidApiClient
        from candid.resources.pre_encounter.appointments.v_1 import (
            AppointmentStatus,
            AppointmentWorkQueue,
            MutableAppointment,
            Service,
            UniversalServiceIdentifier,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.pre_encounter.appointments.v_1.create(
                request=MutableAppointment(
                    patient_id="string",
                    start_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    status=AppointmentStatus.PENDING,
                    service_duration=1,
                    services=[
                        Service(
                            universal_service_identifier=UniversalServiceIdentifier.MD_VISIT,
                            start_timestamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                        )
                    ],
                    placer_appointment_id="string",
                    estimated_copay_cents=1,
                    estimated_patient_responsibility_cents=1,
                    patient_deposit_cents=1,
                    checked_in_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    notes="string",
                    location_resource_id="string",
                    automated_eligibility_check_complete=True,
                    work_queue=AppointmentWorkQueue.EMERGENT_ISSUE,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "appointments/v1",
            base_url=self._client_wrapper.get_environment().pre_encounter,
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
            return pydantic_v1.parse_obj_as(Appointment, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "VersionConflictError":
                raise VersionConflictError(
                    pydantic_v1.parse_obj_as(VersionConflictErrorBody, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: AppointmentId, *, request_options: typing.Optional[RequestOptions] = None) -> Appointment:
        """
        Gets an appointment.

        Parameters
        ----------
        id : AppointmentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Appointment

        Examples
        --------
        import asyncio

        from candid.client import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.pre_encounter.appointments.v_1.get(
                id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"appointments/v1/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Appointment, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_history(
        self, id: AppointmentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Appointment]:
        """
        Gets an appointment along with it's full history. The return list is ordered by version ascending.

        Parameters
        ----------
        id : AppointmentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Appointment]

        Examples
        --------
        import asyncio

        from candid.client import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.pre_encounter.appointments.v_1.get_history(
                id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"appointments/v1/{jsonable_encoder(id)}/history",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="GET",
            request_options=request_options,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Appointment], _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: AppointmentId,
        version: str,
        *,
        request: MutableAppointment,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Appointment:
        """
        Updates an appointment. The path must contain the most recent version to prevent race conditions. Updating historic versions is not supported.

        Parameters
        ----------
        id : AppointmentId

        version : str

        request : MutableAppointment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Appointment

        Examples
        --------
        import asyncio
        import datetime

        from candid.client import AsyncCandidApiClient
        from candid.resources.pre_encounter.appointments.v_1 import (
            AppointmentStatus,
            AppointmentWorkQueue,
            MutableAppointment,
            Service,
            UniversalServiceIdentifier,
        )

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.pre_encounter.appointments.v_1.update(
                id="string",
                version="string",
                request=MutableAppointment(
                    patient_id="string",
                    start_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    status=AppointmentStatus.PENDING,
                    service_duration=1,
                    services=[
                        Service(
                            universal_service_identifier=UniversalServiceIdentifier.MD_VISIT,
                            start_timestamp=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                        )
                    ],
                    placer_appointment_id="string",
                    estimated_copay_cents=1,
                    estimated_patient_responsibility_cents=1,
                    patient_deposit_cents=1,
                    checked_in_timestamp=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    notes="string",
                    location_resource_id="string",
                    automated_eligibility_check_complete=True,
                    work_queue=AppointmentWorkQueue.EMERGENT_ISSUE,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"appointments/v1/{jsonable_encoder(id)}/{jsonable_encoder(version)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
            method="PUT",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Appointment, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "VersionConflictError":
                raise VersionConflictError(
                    pydantic_v1.parse_obj_as(VersionConflictErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def deactivate(
        self, id: AppointmentId, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Sets an appointment as deactivated. The path must contain the most recent version to prevent race conditions. Deactivating historic versions is not supported. Subsequent updates via PUT to the appointment will "reactivate" the appointment and set the deactivated flag to false.

        Parameters
        ----------
        id : AppointmentId

        version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from candid.client import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.pre_encounter.appointments.v_1.deactivate(
                id="string",
                version="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"appointments/v1/{jsonable_encoder(id)}/{jsonable_encoder(version)}",
            base_url=self._client_wrapper.get_environment().pre_encounter,
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
            if _response_json["errorName"] == "NotFoundError":
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(NotFoundErrorBody, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "VersionConflictError":
                raise VersionConflictError(
                    pydantic_v1.parse_obj_as(VersionConflictErrorBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
