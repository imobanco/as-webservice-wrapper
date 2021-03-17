import base64


class Base64Service:
    def _decode_or_encode(self, message: str, action: callable, result_as_string=True):
        """
        Método para codificar/decodificar uma mensagem string.

        :param message: string a ser codificada/decodificada
        :param action: método de codificação ou decodificão
        :param result_as_string: flag indicadora se deve ser retornado bytes ou string
        :return: string ou bytes resultado da operação
        """
        message_bytes = message.encode()
        result_bytes = action(message_bytes)
        if result_as_string:
            result_string = result_bytes.decode()
            return result_string
        return result_bytes

    def encode(self, message_string, result_as_string=True):
        """
        Método para codificar uma string em string base64.

        :param message_string: string a ser codificada
        :param result_as_string: flag indicadora se deve ser retornado bytes ou string
        :return: string ou bytes base64
        """
        return self._decode_or_encode(
            message_string, base64.b64encode, result_as_string=result_as_string
        )

    def decode(self, base64_string, result_as_string=True):
        """
        Método para decodificar uma string base64 em string.

        :param base64_string: string base64 a ser decodificada
        :param result_as_string: flag indicadora se deve ser retornado bytes ou string
        :return: string ou bytes
        """
        return self._decode_or_encode(
            base64_string, base64.b64decode, result_as_string=result_as_string
        )
