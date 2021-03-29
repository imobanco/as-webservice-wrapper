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

        expected = b"cGF5ZXJfZG9jdW1lbnQ7cGF5ZXJfZG9jdW1lbnRfdHlwZTtwYXllcl9uYW1lO3BheWVyX2JhbmtfYWNjb3VudF9udW1iZXI7cGF5ZXJfYmFua19hY2NvdW50X251bWJlcl9kdjtwYXllcl9iYW5rX2FjY291bnRfcm91dGluZztwYXllcl9iYW5rX2FjY291bnRfcm91dGluZ19kdjtwYXllcl9jb252ZW5pbztyZWNlaXZlcl9kb2N1bWVudDtyZWNlaXZlcl9kb2N1bWVudF90eXBlO3JlY2VpdmVyX25hbWU7cmVjZWl2ZXJfYmFua19hY2NvdW50X2JhbmtfbmFtZTtyZWNlaXZlcl9iYW5rX2FjY291bnRfYmFua19jb2RlO3JlY2VpdmVyX2JhbmtfYWNjb3VudF9udW1iZXI7cmVjZWl2ZXJfYmFua19hY2NvdW50X251bWJlcl9kdjtyZWNlaXZlcl9iYW5rX2FjY291bnRfcm91dGluZztyZWNlaXZlcl9iYW5rX2FjY291bnRfcm91dGluZ19kdjtyZWNlaXZlcl9iYW5rX2FjY291bnRfcm91dGluZ19udW1iZXJfZHY7cGF5bWVudF90eXBlO251bWJlcjtwYXltZW50X2Ftb3VudDtwYXltZW50X2RhdGU7Y29kZV9saW5lO2V4cGlyYXRpb25fZGF0ZQ0KMTIzNDU2Nzg5MDEyMzQ7Q05QSjtmb28gYmFyIGRhIHNpbHZhOzEyMzEyMzs0OzEyMzEyMzs0OzEyMzsxMjM0NTY3ODkwMTIzNDtDTlBKO2ZvbyBiYXIgZGEgc2lsdmE7QmFuY28gZG8gQnJhc2lsOzAwMTsxMjMxMjM7NDsxMjMxMjM7NDs7MDM7MTsxMjM0NTsyMjAzMjAyMTs7DQoxMjM0NTY3ODkwMTIzNDtDTlBKO2ZvbyBiYXIgZGEgc2lsdmE7MTIzMTIzOzQ7MTIzMTIzOzQ7MTIzOzEyMzQ1Njc4OTAxMjM0O0NOUEo7Zm9vIGJhciBkYSBzaWx2YTs7Ozs7Ozs7MzE7MTsxMjM0NTsyMjAzMjAyMTsxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMzEyMzsyNTAzMjAyMQ0K"  # noqa

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
        b64_string = b"cGF5ZXJfZG9jdW1lbnQ7cGF5ZXJfZG9jdW1lbnRfdHlwZTtwYXllcl9uYW1lO3BheWVyX2JhbmtfYWNjb3VudF9udW1iZXI7cGF5ZXJfYmFua19hY2NvdW50X251bWJlcl9kdjtwYXllcl9iYW5rX2FjY291bnRfcm91dGluZztwYXllcl9iYW5rX2FjY291bnRfcm91dGluZ19kdjtwYXllcl9jb252ZW5pbztyZWNlaXZlcl9kb2N1bWVudDtyZWNlaXZlcl9kb2N1bWVudF90eXBlO3JlY2VpdmVyX25hbWU7cmVjZWl2ZXJfYmFua19hY2NvdW50X2JhbmtfbmFtZTtyZWNlaXZlcl9iYW5rX2FjY291bnRfYmFua19jb2RlO3JlY2VpdmVyX2JhbmtfYWNjb3VudF9udW1iZXI7cmVjZWl2ZXJfYmFua19hY2NvdW50X251bWJlcl9kdjtyZWNlaXZlcl9iYW5rX2FjY291bnRfcm91dGluZztyZWNlaXZlcl9iYW5rX2FjY291bnRfcm91dGluZ19kdjtyZWNlaXZlcl9iYW5rX2FjY291bnRfcm91dGluZ19udW1iZXJfZHY7cGF5bWVudF90eXBlO251bWJlcjtwYXltZW50X2Ftb3VudDtwYXltZW50X2RhdGU7Y29kZV9saW5lO2V4cGlyYXRpb25fZGF0ZQ0KMTIzNDU2Nzg5MDEyMzQ7Q05QSjtmb28gYmFyIGRhIHNpbHZhOzEyMzEyMzs0OzEyMzEyMzs0OzEyMzsxMjM0NTY3ODkwMTIzNDtDTlBKO2ZvbyBiYXIgZGEgc2lsdmE7QmFuY28gZG8gQnJhc2lsOzAwMTsxMjMxMjM7NDsxMjMxMjM7NDs7MDM7MTsxMjM0NTsyMjAzMjAyMTs7DQoxMjM0NTY3ODkwMTIzNDtDTlBKO2ZvbyBiYXIgZGEgc2lsdmE7MTIzMTIzOzQ7MTIzMTIzOzQ7MTIzOzEyMzQ1Njc4OTAxMjM0O0NOUEo7Zm9vIGJhciBkYSBzaWx2YTs7Ozs7Ozs7MzE7MTsxMjM0NTsyMjAzMjAyMTsxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMjMxMzEyMzsyNTAzMjAyMQ0K"  # noqa

        result = PydanticBase64Adapter().b64_to_pydantic(b64_string, TransactionModel)

        expected = [create_ted_transaction(), create_invoice_transaction()]

        for index, item in enumerate(result):
            with self.subTest(index):
                self.assertEqual(item.dict(), expected[index].dict())
