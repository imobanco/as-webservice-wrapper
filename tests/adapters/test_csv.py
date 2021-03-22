from unittest import TestCase

from as_ws_wrapper.adapters.csv import PydanticCSVAdapter
from as_ws_wrapper.models.base import TransactionModel
from ..factories import create_ted_transaction


class PydanticCSVAdapterTestCase(TestCase):
    maxDiff = None

    def test_pydantic_to_csv_string_1(self):
        """
        Dado:
            -
        Quando:
            -
        Então:
            -
        """
        instance = create_ted_transaction()

        result = PydanticCSVAdapter().pydantic_to_csv_string(
            [instance], TransactionModel
        )

        expected = """document;document_type;name;bank_account_bank_name;bank_account_bank_code;bank_account_number;bank_account_number_dv;bank_account_routing;bank_account_routing_dv;bank_account_routing_number_dv;payment_type;number;payment_amount;payment_date;code_line;expiration_date\r\n12345678901234;CNPJ;foo bar da silva;12345678901234;001;123123;4;123123;4;5;03;1;12345;22032021;;\r\n"""  # noqa

        self.assertEqual(result, expected)

    def test_csv_string_to_pydantic_1(self):
        """
        Dado:
            -
        Quando:
            -
        Então:
            -
        """
        csv_string = """document;document_type;name;bank_account_bank_name;bank_account_bank_code;bank_account_number;bank_account_number_dv;bank_account_routing;bank_account_routing_dv;bank_account_routing_number_dv;payment_type;number;payment_amount;payment_date;code_line;expiration_date\r\n12345678901234;CNPJ;foo bar da silva;12345678901234;001;123123;4;123123;4;5;03;1;12345;22032021;;\r\n"""  # noqa

        result = PydanticCSVAdapter().csv_string_to_pydantic(
            csv_string, TransactionModel
        )

        expected = [create_ted_transaction()]

        for index, item in enumerate(result):
            with self.subTest(index):
                self.assertEqual(item.dict(), expected[index].dict())
