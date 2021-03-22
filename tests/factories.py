from as_ws_wrapper.models.base import TransactionModel


def create_ted_transaction():
    return TransactionModel(
        document="12345678901234",
        document_type="CNPJ",
        name="foo bar da silva",
        bank_account_bank_name="12345678901234",
        bank_account_bank_code="001",
        bank_account_number="123123",
        bank_account_number_dv="4",
        bank_account_routing="123123",
        bank_account_routing_dv="4",
        bank_account_routing_number_dv="5",
        payment_type="03",
        number="1",
        payment_amount="12345",
        payment_date='22032021',
        expiration_date=None,
        code_line=None
    )


def create_invoice_transaction():
    return TransactionModel(
        document="12345678901234",
        document_type="CNPJ",
        name="foo bar da silva",
        bank_account_bank_name=None,
        bank_account_bank_code=None,
        bank_account_number=None,
        bank_account_number_dv=None,
        bank_account_routing=None,
        bank_account_routing_dv=None,
        bank_account_routing_number_dv=None,
        payment_type="31",
        number="1",
        payment_amount="12345",
        payment_date='22032021',
        expiration_date='25032021',
        code_line='12312312312312312312312312312312313123'
    )
