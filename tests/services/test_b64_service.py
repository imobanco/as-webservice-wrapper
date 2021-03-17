from unittest import TestCase

from as_ws_wrapper.services.b64 import Base64Service


class Base64ServiceTestCase(TestCase):
    maxDiff = None

    def test_encode_1(self):
        """
        Dado:
            - um arquivo 'file' de exemplo csv
        Quando:
            - for chamado Base64Service().encode(file.read())
        Então:
            - o resultado deve ser ¯\_(ツ)_/¯  # noqa
        """
        with open("tests/data/sample.csv") as file:
            result = Base64Service().encode(file.read())

        expected = "aWQsdHlwZSxjb2RlX2xpbmUscGF5bWVudF9kYXRlLHBheWVyX2RvY3VtZW50LHBheWVyX25hbWUsYmFua19hY2NvdW50X251bWJlcixiYW5rX2FjY291bnRfcm91dGluZyxiYW5rX2FjY291bnRfYmFua19uYW1lLGJhbmtfYWNjb3VudF9iYW5rX2NvZGUKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEK"  # noqa

        self.assertEqual(result, expected)

    def test_decode_1(self):
        """
        Dado:
            - uma string 'b64' base64
        Quando:
            - for chamado Base64Service().decode(b64)
        Então:
            - o resultado deve ser ¯\_(ツ)_/¯  # noqa
        """
        b64 = "aWQsdHlwZSxjb2RlX2xpbmUscGF5bWVudF9kYXRlLHBheWVyX2RvY3VtZW50LHBheWVyX25hbWUsYmFua19hY2NvdW50X251bWJlcixiYW5rX2FjY291bnRfcm91dGluZyxiYW5rX2FjY291bnRfYmFua19uYW1lLGJhbmtfYWNjb3VudF9iYW5rX2NvZGUKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEK"  # noqa

        result = Base64Service().decode(b64)

        with open("tests/data/sample.csv") as file:
            expected = file.read()

        self.assertEqual(result, expected)
