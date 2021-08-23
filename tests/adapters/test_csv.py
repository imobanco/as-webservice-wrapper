from unittest import TestCase

from as_ws_wrapper.adapters.csv import PydanticCSVAdapter
from as_ws_wrapper.models.base import TransactionModel

from ..factories import create_invoice_transaction, create_ted_transaction


class PydanticCSVAdapterTestCase(TestCase):
    maxDiff = None

    def test_pydantic_to_csv_1(self):
        """
        Dado:
            - uma lista de instâncias TransactionModel
        Quando:
            - for chamado PydanticCSVAdapter().pydantic_to_csv_string(
                instances, TransactionModel
            )
        Então:
            - o resultado deve ser o csv string correto
        """
        instances = [create_ted_transaction(), create_invoice_transaction()]

        result = PydanticCSVAdapter().pydantic_to_csv(instances, TransactionModel)

        expected = b'payer_document;payer_document_type;payer_name;payer_bank_account_number;payer_bank_account_number_dv;payer_bank_account_routing;payer_bank_account_routing_dv;payer_convenio;receiver_document;receiver_document_type;receiver_name;receiver_bank_account_bank_name;receiver_bank_account_bank_code;receiver_bank_account_number;receiver_bank_account_number_dv;receiver_bank_account_routing;receiver_bank_account_routing_dv;receiver_bank_account_routing_number_dv;payment_type;number;payment_amount;payment_date;code_line;expiration_date\r\n24103314000188;CNPJ;Imobanco Banco de Cobran\xc3\xa7as SA;70466;0;2035;4;276470;24103314000188;CNPJ;Imobanco Banco de Cobran\xc3\xa7as SA;Banco Santander;033;13002806;5;4667;0;;03;1;1004;19082021;;\r\n24103314000188;CNPJ;Imobanco Banco de Cobran\xc3\xa7as SA;70466;0;2035;4;276470;00001998545432;CPF;Fula da Silva;;;;;;;;31;1;2003;20082021;23791872100000020003381260065699433000006330;23082021\r\n'  # noqa

        self.assertEqual(result, expected)

    def test_csv_to_pydantic_1(self):
        """
        Dado:
            - um csv string válido
        Quando:
            - for chamado PydanticCSVAdapter().csv_string_to_pydantic(
                csv_string, TransactionModel
            )
        Então:
            - o resultado deve ter a lista de instâncias corretas
        """
        csv_string = b'payer_document;payer_document_type;payer_name;payer_bank_account_number;payer_bank_account_number_dv;payer_bank_account_routing;payer_bank_account_routing_dv;payer_convenio;receiver_document;receiver_document_type;receiver_name;receiver_bank_account_bank_name;receiver_bank_account_bank_code;receiver_bank_account_number;receiver_bank_account_number_dv;receiver_bank_account_routing;receiver_bank_account_routing_dv;receiver_bank_account_routing_number_dv;payment_type;number;payment_amount;payment_date;code_line;expiration_date\r\n24103314000188;CNPJ;Imobanco Banco de Cobran\xc3\xa7as SA;70466;0;2035;4;276470;24103314000188;CNPJ;Imobanco Banco de Cobran\xc3\xa7as SA;Banco Santander;033;13002806;5;4667;0;;03;1;1004;19082021;;\r\n24103314000188;CNPJ;Imobanco Banco de Cobran\xc3\xa7as SA;70466;0;2035;4;276470;00001998545432;CPF;Fula da Silva;;;;;;;;31;1;2003;20082021;23791872100000020003381260065699433000006330;23082021\r\n'  # noqa

        result = PydanticCSVAdapter().csv_to_pydantic(csv_string, TransactionModel)

        expected = [create_ted_transaction(), create_invoice_transaction()]

        for index, item in enumerate(result):
            with self.subTest(index):
                self.assertEqual(item.dict(), expected[index].dict())
