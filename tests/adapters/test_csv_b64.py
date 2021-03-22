from unittest import TestCase

from as_ws_wrapper.adapters.csv_b64 import PydanticBase64Adapter
from as_ws_wrapper.models.base import TransactionModel
from ..factories import create_ted_transaction


class PydanticBase64AdapterTestCase(TestCase):
    maxDiff = None

    def test_pydantic_to_b64_1(self):
        """
        Dado:
            -
        Quando:
            -
        Então:
            -
        """
        instance = create_ted_transaction()

        result = PydanticBase64Adapter().pydantic_to_b64([instance], TransactionModel)

        expected = b'ZG9jdW1lbnQ7ZG9jdW1lbnRfdHlwZTtuYW1lO2JhbmtfYWNjb3VudF9iYW5rX25hbWU7YmFua19hY2NvdW50X2JhbmtfY29kZTtiYW5rX2FjY291bnRfbnVtYmVyO2JhbmtfYWNjb3VudF9udW1iZXJfZHY7YmFua19hY2NvdW50X3JvdXRpbmc7YmFua19hY2NvdW50X3JvdXRpbmdfZHY7YmFua19hY2NvdW50X3JvdXRpbmdfbnVtYmVyX2R2O3BheW1lbnRfdHlwZTtudW1iZXI7cGF5bWVudF9hbW91bnQ7cGF5bWVudF9kYXRlO2NvZGVfbGluZTtleHBpcmF0aW9uX2RhdGUNCjEyMzQ1Njc4OTAxMjM0O0NOUEo7Zm9vIGJhciBkYSBzaWx2YTsxMjM0NTY3ODkwMTIzNDswMDE7MTIzMTIzOzQ7MTIzMTIzOzQ7NTswMzsxOzEyMzQ1OzIyMDMyMDIxOzsNCg=='  # noqa

        self.assertEqual(result, expected)

    def test_b64_to_pydantic_1(self):
        """
        Dado:
            -
        Quando:
            -
        Então:
            -
        """
        b64_string = b'ZG9jdW1lbnQ7ZG9jdW1lbnRfdHlwZTtuYW1lO2JhbmtfYWNjb3VudF9iYW5rX25hbWU7YmFua19hY2NvdW50X2JhbmtfY29kZTtiYW5rX2FjY291bnRfbnVtYmVyO2JhbmtfYWNjb3VudF9udW1iZXJfZHY7YmFua19hY2NvdW50X3JvdXRpbmc7YmFua19hY2NvdW50X3JvdXRpbmdfZHY7YmFua19hY2NvdW50X3JvdXRpbmdfbnVtYmVyX2R2O3BheW1lbnRfdHlwZTtudW1iZXI7cGF5bWVudF9hbW91bnQ7cGF5bWVudF9kYXRlO2NvZGVfbGluZTtleHBpcmF0aW9uX2RhdGUNCjEyMzQ1Njc4OTAxMjM0O0NOUEo7Zm9vIGJhciBkYSBzaWx2YTsxMjM0NTY3ODkwMTIzNDswMDE7MTIzMTIzOzQ7MTIzMTIzOzQ7NTswMzsxOzEyMzQ1OzIyMDMyMDIxOzsNCg=='  # noqa

        result = PydanticBase64Adapter().b64_to_pydantic(b64_string, TransactionModel)

        expected = [create_ted_transaction()]

        for index, item in enumerate(result):
            with self.subTest(index):
                self.assertEqual(item.dict(), expected[index].dict())
