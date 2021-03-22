from typing import Optional, Union

from pydantic import BaseModel, constr


class IndividualInfo(BaseModel):
    document: constr(min_length=14, max_length=14)  # CPF/CNPJ do individuo
    document_type: str  # tipo do documento 'CPF' ou 'CNPJ'
    name: str  # nome do individuo

    bank_account_bank_name: str  # nome do banco da conta bancária
    bank_account_bank_code: str  # código do banco da conta bancária
    bank_account_number: str  # número da conta bancária
    bank_account_number_dv: str  # dv do númerp da conta bancária
    bank_account_routing: str  # agência da conta bancária
    bank_account_routing_dv: str  # dv da agência da conta bancária
    bank_account_routing_number_dv: Optional[
        Union[str, None]
    ]  # dv do agência/número da conta bancária


class TransactionModel(IndividualInfo, BaseModel):
    """ HEADER DO LOTE """

    transaction_type: str  # identificador do tipo de transação

    """ SEGMENTO A + B (DOC/TED) + J + J52 (boleto) """
    number: str  # O que é o número do título para DOC/TED ?!?!?!?!
    expiration_date: str  # data do vencimento
    payment_amount: str  # quantia paga
    code_line: str  # linha digitável do boleto
