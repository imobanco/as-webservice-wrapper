from as_ws_wrapper.models.base import TransactionModel


def create_ted_transaction():
    return TransactionModel(
        document="12345678901234",
        document_type="CNPJ",
        name="foo bar da silva",
        bank_account_bank_name="Banco do Brasil",
        bank_account_bank_code="001",
        bank_account_number="123123",
        bank_account_number_dv="4",
        bank_account_routing="123123",
        bank_account_routing_dv="4",
        bank_account_routing_number_dv="",
        payment_type="03",
        number="1",
        payment_amount="12345",
        payment_date="22032021",
        expiration_date="",
        code_line="",
    )


def create_invoice_transaction():
    return TransactionModel(
        document="12345678901234",
        document_type="CNPJ",
        name="foo bar da silva",
        bank_account_bank_name="",
        bank_account_bank_code="",
        bank_account_number="",
        bank_account_number_dv="",
        bank_account_routing="",
        bank_account_routing_dv="",
        bank_account_routing_number_dv="",
        payment_type="31",
        number="1",
        payment_amount="12345",
        payment_date="22032021",
        expiration_date="25032021",
        code_line="12312312312312312312312312312312313123",
    )
