# This file was auto-generated by Fern from our API Definition.

from ....core.api_error import ApiError
from ..types.era_not_fully_processed_error_message import EraNotFullyProcessedErrorMessage


class EraNotFullyProcessedError(ApiError):
    def __init__(self, body: EraNotFullyProcessedErrorMessage):
        super().__init__(status_code=409, body=body)
