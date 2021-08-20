from as_ws_wrapper.models.base import TransactionModel


def create_ted_transaction():
    return TransactionModel(
        payer_document="24103314000188",
        payer_document_type="CNPJ",
        payer_name="Imobanco Banco de Cobranças SA",
        payer_bank_account_number="70466",
        payer_bank_account_number_dv="0",
        payer_bank_account_routing="2035",
        payer_bank_account_routing_dv="4",
        payer_convenio="276470",
        receiver_document="24103314000188",
        receiver_document_type="CNPJ",
        receiver_name="Imobanco Banco de Cobranças SA",
        receiver_bank_account_bank_name="Banco Santander",
        receiver_bank_account_bank_code="033",
        receiver_bank_account_number="13002806",
        receiver_bank_account_number_dv="5",
        receiver_bank_account_routing="4667",
        receiver_bank_account_routing_dv="0",
        receiver_bank_account_routing_number_dv="",
        payment_type="03",
        number="1",
        payment_amount=1004,
        payment_date="19082021",
        expiration_date="",
        code_line="",
    )


def create_invoice_transaction():
    return TransactionModel(
        payer_document="24103314000188",
        payer_document_type="CNPJ",
        payer_name="Imobanco Banco de Cobranças SA",
        payer_bank_account_number="70466",
        payer_bank_account_number_dv="0",
        payer_bank_account_routing="2035",
        payer_bank_account_routing_dv="4",
        payer_convenio="276470",
        receiver_document="00001688745475",
        receiver_document_type="CPF",
        receiver_name="Rodrigo Nunes de Castro",
        receiver_bank_account_bank_name="",
        receiver_bank_account_bank_code="",
        receiver_bank_account_number="",
        receiver_bank_account_number_dv="",
        receiver_bank_account_routing="",
        receiver_bank_account_routing_dv="",
        receiver_bank_account_routing_number_dv="",
        payment_type="31",
        number="1",
        payment_amount=2003,
        payment_date="20082021",
        expiration_date="23082021",
        code_line="23791872100000020003381260065699433000006330",
    )
