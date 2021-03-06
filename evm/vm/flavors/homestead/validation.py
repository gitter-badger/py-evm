from evm.constants import (
    SECPK1_N,
)
from evm.exceptions import (
    InvalidTransaction,
)

from evm.vm.flavors.frontier.validation import (
    validate_frontier_transaction,
)


def validate_homestead_transaction(evm, transaction):
    if transaction.s > SECPK1_N // 2 or transaction.s == 0:
        raise InvalidTransaction("Invalid signature S value")

    validate_frontier_transaction(evm, transaction)
