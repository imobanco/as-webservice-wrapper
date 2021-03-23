from unittest import TestCase

from as_ws_wrapper.adapters.csv_b64 import PydanticBase64Adapter
from as_ws_wrapper.models.base import TransactionModel
from ..factories import create_ted_transaction, create_invoice_transaction


class PydanticBase64AdapterTestCase(TestCase):
    maxDiff = None

    def test_pydantic_to_b64_1(self):
        """
        Dado:
            - uma lista de instâncias TransactionModel
        Quando:
            - for chamdao PydanticBase64Adapter().pydantic_to_b64(instances, TransactionModel)  # noqa
        Então:
            - o resultado deve ser o base 64 em bytes correto
        """
        instances = [create_ted_transaction(), create_invoice_transaction()]

        result = PydanticBase64Adapter().pydantic_to_b64(instances, TransactionModel)

        expected = b"ZG9jdW1lbnQ7ZG9jdW1lbnRfdHlwZTtuYW1lO2JhbmtfYWNjb3VudF9iYW5rX25hbWU7YmFua19hY2NvdW50X2JhbmtfY29kZTtiYW5rX2FjY291bnRfbnVtYmVyO2JhbmtfYWNjb3VudF9udW1iZXJfZHY7YmFua19hY2NvdW50X3JvdXRpbmc7YmFua19hY2NvdW50X3JvdXRpbmdfZHY7YmFua19hY2NvdW50X3JvdXRpbmdfbnVtYmVyX2R2O3BheW1lbnRfdHlwZTtudW1iZXI7cGF5bWVudF9hbW91bnQ7cGF5bWVudF9kYXRlO2NvZGVfbGluZTtleHBpcmF0aW9uX2RhdGUNCjEyMzQ1Njc4OTAxMjM0O0NOUEo7Zm9vIGJhciBkYSBzaWx2YTtCYW5jbyBkbyBCcmFzaWw7MDAxOzEyMzEyMzs0OzEyMzEyMzs0OzswMzsxOzEyMzQ1OzIyMDMyMDIxOzsNCjEyMzQ1Njc4OTAxMjM0O0NOUEo7Zm9vIGJhciBkYSBzaWx2YTs7Ozs7Ozs7MzE7MTsxMjM0NTsyMjAzMjAyMTsxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMzEyMzsyNTAzMjAyMQ0K"  # noqa

        self.assertEqual(result, expected)

    def test_b64_to_pydantic_1(self):
        """
        Dado:
            - um base64 em bytes válido
        Quando:
            - for chamdo PydanticBase64Adapter().b64_to_pydantic(b64_string, TransactionModel)  # noqa
        Então:
            - o resultado deve ter a lista de instâncias corretas
        """
        b64_string = b"ZG9jdW1lbnQ7ZG9jdW1lbnRfdHlwZTtuYW1lO2JhbmtfYWNjb3VudF9iYW5rX25hbWU7YmFua19hY2NvdW50X2JhbmtfY29kZTtiYW5rX2FjY291bnRfbnVtYmVyO2JhbmtfYWNjb3VudF9udW1iZXJfZHY7YmFua19hY2NvdW50X3JvdXRpbmc7YmFua19hY2NvdW50X3JvdXRpbmdfZHY7YmFua19hY2NvdW50X3JvdXRpbmdfbnVtYmVyX2R2O3BheW1lbnRfdHlwZTtudW1iZXI7cGF5bWVudF9hbW91bnQ7cGF5bWVudF9kYXRlO2NvZGVfbGluZTtleHBpcmF0aW9uX2RhdGUNCjEyMzQ1Njc4OTAxMjM0O0NOUEo7Zm9vIGJhciBkYSBzaWx2YTtCYW5jbyBkbyBCcmFzaWw7MDAxOzEyMzEyMzs0OzEyMzEyMzs0OzswMzsxOzEyMzQ1OzIyMDMyMDIxOzsNCjEyMzQ1Njc4OTAxMjM0O0NOUEo7Zm9vIGJhciBkYSBzaWx2YTs7Ozs7Ozs7MzE7MTsxMjM0NTsyMjAzMjAyMTsxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMzEyMzsyNTAzMjAyMQ0K"  # noqa

        result = PydanticBase64Adapter().b64_to_pydantic(b64_string, TransactionModel)

        expected = [create_ted_transaction(), create_invoice_transaction()]

        for index, item in enumerate(result):
            with self.subTest(index):
                self.assertEqual(item.dict(), expected[index].dict())
