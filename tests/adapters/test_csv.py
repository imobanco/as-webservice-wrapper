from unittest import TestCase

from as_ws_wrapper.adapters.csv import PydanticCSVAdapter
from as_ws_wrapper.models.base import TransactionModel
from ..factories import create_ted_transaction, create_invoice_transaction


class PydanticCSVAdapterTestCase(TestCase):
    maxDiff = None

    def test_pydantic_to_csv_string_1(self):
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

        result = PydanticCSVAdapter().pydantic_to_csv_string(
            instances, TransactionModel
        )

        expected = "payer_document;payer_document_type;payer_name;payer_bank_account_number;payer_bank_account_number_dv;payer_bank_account_routing;payer_bank_account_routing_dv;payer_convenio;receiver_document;receiver_document_type;receiver_name;receiver_bank_account_bank_name;receiver_bank_account_bank_code;receiver_bank_account_number;receiver_bank_account_number_dv;receiver_bank_account_routing;receiver_bank_account_routing_dv;receiver_bank_account_routing_number_dv;payment_type;number;payment_amount;payment_date;code_line;expiration_date\r\n12345678901234;CNPJ;foo bar da silva;123123;4;123123;4;123;12345678901234;CNPJ;foo bar da silva;Banco do Brasil;001;123123;4;123123;4;;03;1;12345;22032021;;\r\n12345678901234;CNPJ;foo bar da silva;123123;4;123123;4;123;12345678901234;CNPJ;foo bar da silva;;;;;;;;31;1;12345;22032021;12312312312312312312312312312312313123;25032021\r\n"  # noqa

        self.assertEqual(result, expected)

    def test_csv_string_to_pydantic_1(self):
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
        csv_string = "payer_document;payer_document_type;payer_name;payer_bank_account_number;payer_bank_account_number_dv;payer_bank_account_routing;payer_bank_account_routing_dv;payer_convenio;receiver_document;receiver_document_type;receiver_name;receiver_bank_account_bank_name;receiver_bank_account_bank_code;receiver_bank_account_number;receiver_bank_account_number_dv;receiver_bank_account_routing;receiver_bank_account_routing_dv;receiver_bank_account_routing_number_dv;payment_type;number;payment_amount;payment_date;code_line;expiration_date\r\n12345678901234;CNPJ;foo bar da silva;123123;4;123123;4;123;12345678901234;CNPJ;foo bar da silva;Banco do Brasil;001;123123;4;123123;4;;03;1;12345;22032021;;\r\n12345678901234;CNPJ;foo bar da silva;123123;4;123123;4;123;12345678901234;CNPJ;foo bar da silva;;;;;;;;31;1;12345;22032021;12312312312312312312312312312312313123;25032021\r\n"  # noqa

        result = PydanticCSVAdapter().csv_string_to_pydantic(
            csv_string, TransactionModel
        )

        expected = [create_ted_transaction(), create_invoice_transaction()]

        for index, item in enumerate(result):
            with self.subTest(index):
                self.assertEqual(item.dict(), expected[index].dict())
