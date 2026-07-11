import types
import typing

from ruba.base import AsyncClientBase, SyncClientBase
from ruba.benefit_grants import BenefitGrantsAsync, BenefitGrantsSync
from ruba.benefits import BenefitsAsync, BenefitsSync
from ruba.checkout_links import CheckoutLinksAsync, CheckoutLinksSync
from ruba.checkouts import CheckoutsAsync, CheckoutsSync
from ruba.custom_fields import CustomFieldsAsync, CustomFieldsSync
from ruba.customer_meters import CustomerMetersAsync, CustomerMetersSync
from ruba.customer_portal import CustomerPortalAsync, CustomerPortalSync
from ruba.customer_seats import CustomerSeatsAsync, CustomerSeatsSync
from ruba.customer_sessions import CustomerSessionsAsync, CustomerSessionsSync
from ruba.customers import CustomersAsync, CustomersSync
from ruba.discounts import DiscountsAsync, DiscountsSync
from ruba.disputes import DisputesAsync, DisputesSync
from ruba.event_types import EventTypesAsync, EventTypesSync
from ruba.events import EventsAsync, EventsSync
from ruba.files import FilesAsync, FilesSync
from ruba.license_keys import LicenseKeysAsync, LicenseKeysSync
from ruba.members import MembersAsync, MembersSync
from ruba.meters import MetersAsync, MetersSync
from ruba.metrics import MetricsAsync, MetricsSync
from ruba.oauth2 import Oauth2Async, Oauth2Sync
from ruba.orders import OrdersAsync, OrdersSync
from ruba.organizations import OrganizationsAsync, OrganizationsSync
from ruba.payments import PaymentsAsync, PaymentsSync
from ruba.products import ProductsAsync, ProductsSync
from ruba.refunds import RefundsAsync, RefundsSync
from ruba.subscriptions import SubscriptionsAsync, SubscriptionsSync
from ruba.webhooks import WebhooksAsync, WebhooksSync

DEFAULT_BASE_URL = "https://api.getruba.com"
DEFAULT_API_VERSION = "2026-04"


class Ruba:
    def __init__(
        self,
        access_token: str,
        base_url: str = DEFAULT_BASE_URL,
        version: str = DEFAULT_API_VERSION,
    ) -> None:
        self._client = SyncClientBase(base_url, version, access_token)
        self.organizations = OrganizationsSync(self._client)
        self.subscriptions = SubscriptionsSync(self._client)
        self.oauth2 = Oauth2Sync(self._client)
        self.benefits = BenefitsSync(self._client)
        self.benefit_grants = BenefitGrantsSync(self._client)
        self.webhooks = WebhooksSync(self._client)
        self.products = ProductsSync(self._client)
        self.orders = OrdersSync(self._client)
        self.refunds = RefundsSync(self._client)
        self.disputes = DisputesSync(self._client)
        self.checkouts = CheckoutsSync(self._client)
        self.files = FilesSync(self._client)
        self.metrics = MetricsSync(self._client)
        self.license_keys = LicenseKeysSync(self._client)
        self.checkout_links = CheckoutLinksSync(self._client)
        self.custom_fields = CustomFieldsSync(self._client)
        self.discounts = DiscountsSync(self._client)
        self.customers = CustomersSync(self._client)
        self.members = MembersSync(self._client)
        self.customer_portal = CustomerPortalSync(self._client)
        self.customer_seats = CustomerSeatsSync(self._client)
        self.customer_sessions = CustomerSessionsSync(self._client)
        self.events = EventsSync(self._client)
        self.event_types = EventTypesSync(self._client)
        self.meters = MetersSync(self._client)
        self.customer_meters = CustomerMetersSync(self._client)
        self.payments = PaymentsSync(self._client)

    def __enter__(self) -> typing.Self:
        self._client.__enter__()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_val: BaseException | None = None,
        exc_tb: types.TracebackType | None = None,
    ) -> None:
        self._client.__exit__(exc_type, exc_val, exc_tb)


class RubaAsync:
    def __init__(
        self,
        access_token: str,
        base_url: str = DEFAULT_BASE_URL,
        version: str = DEFAULT_API_VERSION,
    ) -> None:
        self._client = AsyncClientBase(base_url, version, access_token)
        self.organizations = OrganizationsAsync(self._client)
        self.subscriptions = SubscriptionsAsync(self._client)
        self.oauth2 = Oauth2Async(self._client)
        self.benefits = BenefitsAsync(self._client)
        self.benefit_grants = BenefitGrantsAsync(self._client)
        self.webhooks = WebhooksAsync(self._client)
        self.products = ProductsAsync(self._client)
        self.orders = OrdersAsync(self._client)
        self.refunds = RefundsAsync(self._client)
        self.disputes = DisputesAsync(self._client)
        self.checkouts = CheckoutsAsync(self._client)
        self.files = FilesAsync(self._client)
        self.metrics = MetricsAsync(self._client)
        self.license_keys = LicenseKeysAsync(self._client)
        self.checkout_links = CheckoutLinksAsync(self._client)
        self.custom_fields = CustomFieldsAsync(self._client)
        self.discounts = DiscountsAsync(self._client)
        self.customers = CustomersAsync(self._client)
        self.members = MembersAsync(self._client)
        self.customer_portal = CustomerPortalAsync(self._client)
        self.customer_seats = CustomerSeatsAsync(self._client)
        self.customer_sessions = CustomerSessionsAsync(self._client)
        self.events = EventsAsync(self._client)
        self.event_types = EventTypesAsync(self._client)
        self.meters = MetersAsync(self._client)
        self.customer_meters = CustomerMetersAsync(self._client)
        self.payments = PaymentsAsync(self._client)

    async def __aenter__(self) -> typing.Self:
        await self._client.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_val: BaseException | None = None,
        exc_tb: types.TracebackType | None = None,
    ) -> None:
        await self._client.__aexit__(exc_type, exc_val, exc_tb)


__all__ = ["Ruba", "RubaAsync"]
