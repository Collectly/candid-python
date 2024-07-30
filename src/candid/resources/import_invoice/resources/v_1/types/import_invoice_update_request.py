# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....invoices.resources.v_2.types.invoice_status import InvoiceStatus
from .invoice_item_info_update import InvoiceItemInfoUpdate


class ImportInvoiceUpdateRequest(pydantic.BaseModel):
    customer_invoice_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the patient view of the invoice in the third-party service
    """

    status: typing.Optional[InvoiceStatus] = None
    note: typing.Optional[str] = None
    due_date: typing.Optional[dt.date] = None
    items: typing.Optional[InvoiceItemInfoUpdate] = pydantic.Field(default=None)
    """
    None here represents there is no update to the invoice items
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}