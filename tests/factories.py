from as_ws_wrapper.models.base import TransactionModel


def create_transaction():
    return TransactionModel(
            document="12345678901234",
            document_type="12345678901234",
            name="12345678901234",
            bank_account_bank_name="12345678901234",
            bank_account_bank_code="12345678901234",
            bank_account_number="12345678901234",
            bank_account_number_dv="12345678901234",
            bank_account_routing="12345678901234",
            bank_account_routing_dv="12345678901234",
            bank_account_routing_number_dv="12345678901234",
            transaction_type="12345678901234",
            number="12345678901234",
            expiration_date="12345678901234",
            payment_amount="12345678901234",
            code_line="12345678901234",
        )

