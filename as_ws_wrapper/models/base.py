from typing import Optional, Union, Literal

from pydantic import BaseModel, constr


class IndividualInfo(BaseModel):
    """
    Informações do favorecido/beneficiário
    """

    document: constr(min_length=14, max_length=14)  # CPF/CNPJ do individuo
    document_type: Literal["CPF", "CNPJ"]  # tipo do documento 'CPF' ou 'CNPJ'
    name: str  # nome do individuo

    bank_account_bank_name: Optional[
        str
    ]  # nome do banco da conta bancária  | TED/DOC apenas
    bank_account_bank_code: Optional[
        Union[constr(min_length=3, max_length=3), constr(min_length=0, max_length=0)]
    ]  # código do banco da conta bancária  | TED/DOC apenas
    bank_account_number: Optional[str]  # número da conta bancária  | TED/DOC apenas
    bank_account_number_dv: Optional[
        str
    ]  # dv do númerp da conta bancária  | TED/DOC apenas
    bank_account_routing: Optional[str]  # agência da conta bancária  | TED/DOC apenas
    bank_account_routing_dv: Optional[
        str
    ]  # dv da agência da conta bancária  | TED/DOC apenas
    bank_account_routing_number_dv: Optional[
        Union[str, None]
    ]  # dv do agência/número da conta bancária  | TED/DOC apenas


class TransactionModel(IndividualInfo, BaseModel):
    """
    Informações da transação de pagamento
    """

    """ HEADER DO LOTE """

    payment_type: Literal[
        "01", "03", "41", "43", "30", "31"
    ]  # código do tipo de pagamento

    """ SEGMENTO A + B (DOC/TED) + J + J52 (boleto) """
    number: str  # Seu número, alfanumérico
    payment_amount: str  # quantia paga
    payment_date: str  # data de pagamento (formato DDMMAAAA)
    code_line: Optional[str]  # linha digitável do boleto  | boleto apenas
    expiration_date: Optional[
        str
    ]  # data do vencimento (formato DDMMAAAA)  | boleto apenas
