from __future__ import annotations

from ruba.base import RubaClientError
from ruba.outputs import (
    AlreadyCanceledSubscription as AlreadyCanceledSubscriptionModel,
)
from ruba.outputs import (
    CheckoutForbiddenError as CheckoutForbiddenErrorModel,
)
from ruba.outputs import (
    CustomerNotReady as CustomerNotReadyModel,
)
from ruba.outputs import (
    ExpiredCheckoutError as ExpiredCheckoutErrorModel,
)
from ruba.outputs import (
    HTTPValidationError as HTTPValidationErrorModel,
)
from ruba.outputs import (
    ManualRetryLimitExceeded as ManualRetryLimitExceededModel,
)
from ruba.outputs import (
    MissingInvoiceBillingDetails as MissingInvoiceBillingDetailsModel,
)
from ruba.outputs import (
    NotPermitted as NotPermittedModel,
)
from ruba.outputs import (
    OffSessionChargesNotEnabled as OffSessionChargesNotEnabledModel,
)
from ruba.outputs import (
    OrderNotDraft as OrderNotDraftModel,
)
from ruba.outputs import (
    OrderNotEligibleForRetry as OrderNotEligibleForRetryModel,
)
from ruba.outputs import (
    OrganizationNotReadyForPayments as OrganizationNotReadyForPaymentsModel,
)
from ruba.outputs import (
    PaymentActionRequired as PaymentActionRequiredModel,
)
from ruba.outputs import (
    PaymentAlreadyInProgress as PaymentAlreadyInProgressModel,
)
from ruba.outputs import (
    PaymentError as PaymentErrorModel,
)
from ruba.outputs import (
    PaymentFailed as PaymentFailedModel,
)
from ruba.outputs import (
    PaymentMethodInUseByActiveSubscription as PaymentMethodInUseByActiveSubscriptionModel,
)
from ruba.outputs import (
    PaymentMethodSetupFailed as PaymentMethodSetupFailedModel,
)
from ruba.outputs import (
    RefundedAlready as RefundedAlreadyModel,
)
from ruba.outputs import (
    ResourceNotFound as ResourceNotFoundModel,
)
from ruba.outputs import (
    SubscriptionLocked as SubscriptionLockedModel,
)
from ruba.outputs import (
    Unauthorized as UnauthorizedModel,
)


class HTTPValidationError(RubaClientError):
    error_type = HTTPValidationErrorModel
    error: HTTPValidationErrorModel

    def __init__(self, status_code: int, error: HTTPValidationErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class ResourceNotFound(RubaClientError):
    error_type = ResourceNotFoundModel
    error: ResourceNotFoundModel

    def __init__(self, status_code: int, error: ResourceNotFoundModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class NotPermitted(RubaClientError):
    error_type = NotPermittedModel
    error: NotPermittedModel

    def __init__(self, status_code: int, error: NotPermittedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class AlreadyCanceledSubscription(RubaClientError):
    error_type = AlreadyCanceledSubscriptionModel
    error: AlreadyCanceledSubscriptionModel

    def __init__(
        self, status_code: int, error: AlreadyCanceledSubscriptionModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class SubscriptionLocked(RubaClientError):
    error_type = SubscriptionLockedModel
    error: SubscriptionLockedModel

    def __init__(self, status_code: int, error: SubscriptionLockedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentFailed(RubaClientError):
    error_type = PaymentFailedModel
    error: PaymentFailedModel

    def __init__(self, status_code: int, error: PaymentFailedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class Finalize402Error(RubaClientError):
    error_type = PaymentFailedModel | PaymentActionRequiredModel
    error: PaymentFailedModel | PaymentActionRequiredModel

    def __init__(
        self, status_code: int, error: PaymentFailedModel | PaymentActionRequiredModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class Finalize403Error(RubaClientError):
    error_type = OffSessionChargesNotEnabledModel | OrganizationNotReadyForPaymentsModel
    error: OffSessionChargesNotEnabledModel | OrganizationNotReadyForPaymentsModel

    def __init__(
        self,
        status_code: int,
        error: OffSessionChargesNotEnabledModel | OrganizationNotReadyForPaymentsModel,
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class OrderNotDraft(RubaClientError):
    error_type = OrderNotDraftModel
    error: OrderNotDraftModel

    def __init__(self, status_code: int, error: OrderNotDraftModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class MissingInvoiceBillingDetails(RubaClientError):
    error_type = MissingInvoiceBillingDetailsModel
    error: MissingInvoiceBillingDetailsModel

    def __init__(
        self, status_code: int, error: MissingInvoiceBillingDetailsModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class RefundedAlready(RubaClientError):
    error_type = RefundedAlreadyModel
    error: RefundedAlreadyModel

    def __init__(self, status_code: int, error: RefundedAlreadyModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class Update403Error(RubaClientError):
    error_type = CheckoutForbiddenErrorModel
    error: CheckoutForbiddenErrorModel

    def __init__(self, status_code: int, error: CheckoutForbiddenErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class ExpiredCheckoutError(RubaClientError):
    error_type = ExpiredCheckoutErrorModel
    error: ExpiredCheckoutErrorModel

    def __init__(self, status_code: int, error: ExpiredCheckoutErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class ClientUpdate403Error(RubaClientError):
    error_type = CheckoutForbiddenErrorModel
    error: CheckoutForbiddenErrorModel

    def __init__(self, status_code: int, error: CheckoutForbiddenErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentError(RubaClientError):
    error_type = PaymentErrorModel
    error: PaymentErrorModel

    def __init__(self, status_code: int, error: PaymentErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class ClientConfirm403Error(RubaClientError):
    error_type = CheckoutForbiddenErrorModel
    error: CheckoutForbiddenErrorModel

    def __init__(self, status_code: int, error: CheckoutForbiddenErrorModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class Unauthorized(RubaClientError):
    error_type = UnauthorizedModel
    error: UnauthorizedModel

    def __init__(self, status_code: int, error: UnauthorizedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CreateMember403Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentMethodSetupFailed(RubaClientError):
    error_type = PaymentMethodSetupFailedModel
    error: PaymentMethodSetupFailedModel

    def __init__(self, status_code: int, error: PaymentMethodSetupFailedModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class CustomerNotReady(RubaClientError):
    error_type = CustomerNotReadyModel
    error: CustomerNotReadyModel

    def __init__(self, status_code: int, error: CustomerNotReadyModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentMethodInUseByActiveSubscription(RubaClientError):
    error_type = PaymentMethodInUseByActiveSubscriptionModel
    error: PaymentMethodInUseByActiveSubscriptionModel

    def __init__(
        self, status_code: int, error: PaymentMethodInUseByActiveSubscriptionModel
    ) -> None:
        self.error = error
        super().__init__(status_code, error)


class CheckEmailUpdate401Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class VerifyEmailUpdate401Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class VerifyEmailUpdate422Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ListSeats401Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ListSeats403Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ListSeats404Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AssignSeat400Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AssignSeat401Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AssignSeat403Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AssignSeat404Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RevokeSeat401Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RevokeSeat403Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RevokeSeat404Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ResendInvitation400Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ResendInvitation401Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ResendInvitation403Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ResendInvitation404Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ListClaimedSubscriptions401Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ListMembers401Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ListMembers403Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AddMember400Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AddMember401Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class AddMember403Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RemoveMember400Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RemoveMember401Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RemoveMember403Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class RemoveMember404Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class UpdateMember400Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class UpdateMember401Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class UpdateMember403Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class UpdateMember404Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class PaymentAlreadyInProgress(RubaClientError):
    error_type = PaymentAlreadyInProgressModel
    error: PaymentAlreadyInProgressModel

    def __init__(self, status_code: int, error: PaymentAlreadyInProgressModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class OrderNotEligibleForRetry(RubaClientError):
    error_type = OrderNotEligibleForRetryModel
    error: OrderNotEligibleForRetryModel

    def __init__(self, status_code: int, error: OrderNotEligibleForRetryModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class ManualRetryLimitExceeded(RubaClientError):
    error_type = ManualRetryLimitExceededModel
    error: ManualRetryLimitExceededModel

    def __init__(self, status_code: int, error: ManualRetryLimitExceededModel) -> None:
        self.error = error
        super().__init__(status_code, error)


class GetClaimInfo400Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class GetClaimInfo403Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class GetClaimInfo404Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ClaimSeat400Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class ClaimSeat403Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)


class Update404Error(RubaClientError):
    error_type = None
    error: None

    def __init__(self, status_code: int, error: None) -> None:
        self.error = error
        super().__init__(status_code, error)
