from as_ws_wrapper.models.base import TransactionModel


def create_ted_transaction():
    return TransactionModel(
        payer_document="12345678901234",
        payer_document_type="CNPJ",
        payer_name="foo bar da silva",
        payer_bank_account_number="123123",
        payer_bank_account_number_dv="4",
        payer_bank_account_routing="123123",
        payer_bank_account_routing_dv="4",
        payer_convenio="123",
        receiver_document="12345678901234",
        receiver_document_type="CNPJ",
        receiver_name="foo bar da silva",
        receiver_bank_account_bank_name="Banco do Brasil",
        receiver_bank_account_bank_code="001",
        receiver_bank_account_number="123123",
        receiver_bank_account_number_dv="4",
        receiver_bank_account_routing="123123",
        receiver_bank_account_routing_dv="4",
        receiver_bank_account_routing_number_dv="",
        payment_type="03",
        number="1",
        payment_amount=12345,
        payment_date="22032021",
        expiration_date="",
        code_line="",
    )


def create_invoice_transaction():
    return TransactionModel(
        payer_document="12345678901234",
        payer_document_type="CNPJ",
        payer_name="foo bar da silva",
        payer_bank_account_number="123123",
        payer_bank_account_number_dv="4",
        payer_bank_account_routing="123123",
        payer_bank_account_routing_dv="4",
        payer_convenio="123",
        receiver_document="12345678901234",
        receiver_document_type="CNPJ",
        receiver_name="foo bar da silva",
        receiver_bank_account_bank_name="",
        receiver_bank_account_bank_code="",
        receiver_bank_account_number="",
        receiver_bank_account_number_dv="",
        receiver_bank_account_routing="",
        receiver_bank_account_routing_dv="",
        receiver_bank_account_routing_number_dv="",
        payment_type="31",
        number="1",
        payment_amount=12345,
        payment_date="22032021",
        expiration_date="25032021",
        code_line="12312312312312312312312312312312313123",
    )
