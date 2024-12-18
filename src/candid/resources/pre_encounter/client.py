# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .resources.appointments.client import AppointmentsClient, AsyncAppointmentsClient
from .resources.coverages.client import AsyncCoveragesClient, CoveragesClient
from .resources.lists.client import AsyncListsClient, ListsClient
from .resources.notes.client import AsyncNotesClient, NotesClient
from .resources.patients.client import AsyncPatientsClient, PatientsClient
from .resources.tags.client import AsyncTagsClient, TagsClient


class PreEncounterClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.appointments = AppointmentsClient(client_wrapper=self._client_wrapper)
        self.coverages = CoveragesClient(client_wrapper=self._client_wrapper)
        self.lists = ListsClient(client_wrapper=self._client_wrapper)
        self.notes = NotesClient(client_wrapper=self._client_wrapper)
        self.patients = PatientsClient(client_wrapper=self._client_wrapper)
        self.tags = TagsClient(client_wrapper=self._client_wrapper)


class AsyncPreEncounterClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.appointments = AsyncAppointmentsClient(client_wrapper=self._client_wrapper)
        self.coverages = AsyncCoveragesClient(client_wrapper=self._client_wrapper)
        self.lists = AsyncListsClient(client_wrapper=self._client_wrapper)
        self.notes = AsyncNotesClient(client_wrapper=self._client_wrapper)
        self.patients = AsyncPatientsClient(client_wrapper=self._client_wrapper)
        self.tags = AsyncTagsClient(client_wrapper=self._client_wrapper)
