from unittest import TestCase

from as_ws_wrapper.adapters.b64 import StringBase64Adapter


class StringBase64AdapterTestCase(TestCase):
    maxDiff = None

    def test_string_to_b64_1(self):
        """
        Dado:
            - um arquivo 'file' de exemplo csv
        Quando:
            - for chamado Base64Service().string_to_b64(file.read())
        Então:
            - o resultado deve ser ¯\_(ツ)_/¯  # noqa
        """
        with open("tests/data/sample.csv") as file:
            result = StringBase64Adapter().string_to_b64(
                file.read(), result_as_string=True
            )

        expected = "aWQsdHlwZSxjb2RlX2xpbmUscGF5bWVudF9kYXRlLHBheWVyX2RvY3VtZW50LHBheWVyX25hbWUsYmFua19hY2NvdW50X251bWJlcixiYW5rX2FjY291bnRfcm91dGluZyxiYW5rX2FjY291bnRfYmFua19uYW1lLGJhbmtfYWNjb3VudF9iYW5rX2NvZGUKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEK"  # noqa

        self.assertIsInstance(result, str)
        self.assertEqual(result, expected)

    def test_string_to_b64_2(self):
        """
        Dado:
            - um arquivo 'file' de exemplo csv
        Quando:
            - for chamado Base64Service().string_to_b64(file.read(), result_as_string=False)
        Então:
            - o resultado deve ser ¯\_(ツ)_/¯  # noqa
        """
        with open("tests/data/sample.csv") as file:
            result = StringBase64Adapter().string_to_b64(
                file.read(), result_as_string=False
            )

        expected = b"aWQsdHlwZSxjb2RlX2xpbmUscGF5bWVudF9kYXRlLHBheWVyX2RvY3VtZW50LHBheWVyX25hbWUsYmFua19hY2NvdW50X251bWJlcixiYW5rX2FjY291bnRfcm91dGluZyxiYW5rX2FjY291bnRfYmFua19uYW1lLGJhbmtfYWNjb3VudF9iYW5rX2NvZGUKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEK"  # noqa

        self.assertIsInstance(result, bytes)
        self.assertEqual(result, expected)

    def test_b64_to_string_1(self):
        """
        Dado:
            - uma string 'b64' base64
        Quando:
            - for chamado Base64Service().b64_to_string(b64)
        Então:
            - o resultado deve ser ¯\_(ツ)_/¯  # noqa
        """
        b64 = "aWQsdHlwZSxjb2RlX2xpbmUscGF5bWVudF9kYXRlLHBheWVyX2RvY3VtZW50LHBheWVyX25hbWUsYmFua19hY2NvdW50X251bWJlcixiYW5rX2FjY291bnRfcm91dGluZyxiYW5rX2FjY291bnRfYmFua19uYW1lLGJhbmtfYWNjb3VudF9iYW5rX2NvZGUKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEK"  # noqa

        result = StringBase64Adapter().b64_to_string(b64)

        with open("tests/data/sample.csv") as file:
            expected = file.read()

        self.assertIsInstance(result, str)
        self.assertEqual(result, expected)

    def test_b64_to_string_2(self):
        """
        Dado:
            - uma string bytes 'b64' base64
        Quando:
            - for chamado Base64Service().b64_to_string(b64)
        Então:
            - o resultado deve ser ¯\_(ツ)_/¯  # noqa
        """
        b64 = b"aWQsdHlwZSxjb2RlX2xpbmUscGF5bWVudF9kYXRlLHBheWVyX2RvY3VtZW50LHBheWVyX25hbWUsYmFua19hY2NvdW50X251bWJlcixiYW5rX2FjY291bnRfcm91dGluZyxiYW5rX2FjY291bnRfYmFua19uYW1lLGJhbmtfYWNjb3VudF9iYW5rX2NvZGUKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEKMWU4NGE5YTMtY2M0NC00NzRmLWE1MmEtZjZhN2RmNWFhMWY2LGludm9pY2VfcGF5bWVudCwwMDE5MDAwMDA5MDMxMjg1NTc5OTI5OTk5OTk5NDE3MzI4NDk4MDAwMDAwMDMwMCwyMDIxLTAyLTI2LDY3NDQ1NTcwNjgzLFNoYW5ub24gU3Ryb25nLDgyNDQ2Mzg4ODU3MjQwNDAsOTU5MjE2LEJBTkNPIERPIEJSQVNJTCwwMDEK"  # noqa

        result = StringBase64Adapter().b64_to_string(b64)

        with open("tests/data/sample.csv") as file:
            expected = file.read()

        self.assertIsInstance(result, str)
        self.assertEqual(result, expected)
