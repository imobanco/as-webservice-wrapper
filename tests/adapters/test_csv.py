from unittest import TestCase

from as_ws_wrapper.adapters.csv import PydanticCSVAdapter
from as_ws_wrapper.models.base import TransactionModel
from ..factories import create_transaction


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
        instance = create_transaction()

        result = PydanticCSVAdapter().pydantic_to_csv_string(
            [instance], TransactionModel
        )

        expected = "document;document_type;name;bank_account_bank_name;bank_account_bank_code;bank_account_number;bank_account_number_dv;bank_account_routing;bank_account_routing_dv;bank_account_routing_number_dv;transaction_type;number;expiration_date;payment_amount;code_line\r\n12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234\r\n"  # noqa

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
        csv_string = "document;document_type;name;bank_account_bank_name;bank_account_bank_code;bank_account_number;bank_account_number_dv;bank_account_routing;bank_account_routing_dv;bank_account_routing_number_dv;transaction_type;number;expiration_date;payment_amount;code_line\r\n12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234\r\n"  # noqa

        result = PydanticCSVAdapter().csv_string_to_pydantic(
            csv_string, TransactionModel
        )

        expected = [create_transaction()]

        for index, item in enumerate(result):
            with self.subTest(index):
                self.assertEqual(item.dict(), expected[index].dict())
