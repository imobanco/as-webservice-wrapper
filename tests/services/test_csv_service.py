from unittest import TestCase

from as_ws_wrapper.services.csv import CSVService
from ..factories import create_transaction


class Base64ServiceTestCase(TestCase):
    maxDiff = None

    def test_parse_to_csv_1(self):
        """
        Dado:
            -
        Quando:
            -
        Então:
            -
        """
        instance = create_transaction()

        result = CSVService().parse_transactions_to_csv_string([instance])

        expected = "document;document_type;name;bank_account_bank_name;bank_account_bank_code;bank_account_number;bank_account_number_dv;bank_account_routing;bank_account_routing_dv;bank_account_routing_number_dv;transaction_type;number;expiration_date;payment_amount;code_line\r\n12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234\r\n"  # noqa

        self.assertEqual(result, expected)

    def test_parse_to_transaction(self):
        """
        Dado:
            -
        Quando:
            -
        Então:
            -
        """
        csv_string = "document;document_type;name;bank_account_bank_name;bank_account_bank_code;bank_account_number;bank_account_number_dv;bank_account_routing;bank_account_routing_dv;bank_account_routing_number_dv;transaction_type;number;expiration_date;payment_amount;code_line\r\n12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234;12345678901234\r\n"  # noqa

        result = CSVService().parse_csv_string_to_transactions(csv_string)

        expected = [
            create_transaction()
        ]

        for index, item in enumerate(result):
            with self.subTest(index):
                self.assertEqual(
                    item.dict(),
                    expected[index].dict()
                )
