from zeep.exceptions import TransportError
from zeep.xsd.valueobjects import CompoundValue

from .soap import BaseSoapWrapper
from ..response import ProcessedResponse


class AccesstageSoapWrapper(BaseSoapWrapper):
    ACCESSTAGE_BASE_WSL = "https://www.accesstage.com.br/ASTrafegoWS/ProxyServices/"

    def _process_response(self, response):
        try:
            if isinstance(response, CompoundValue) and response['dscErroEnvio']:
                raise TransportError(message=response["dscErroEnvio"], content=response)
        except KeyError:
            pass
        try:
            if isinstance(response, CompoundValue):
                if any(value in response["dscStatusRetirada"] for value in ["Erro", 'invalidVariables']):
                    raise TransportError(
                        message=response["dscStatusRetirada"], content=response
                    )
        except KeyError:
            pass

        processed_response = ProcessedResponse(response)
        return processed_response

    def _get_wsl(self, service):
        """
        Método para retornar o 'url' do webservice a ser utilizado.

        :param service: webservice a ser utilizado
        :return: string do wsl
        """
        return f"{self.ACCESSTAGE_BASE_WSL}{service}?wsdl"

    def lista_servicos(self):
        client = self.get_client(wsdl=self._get_wsl("ListaServicosDisponiveisProxy"))

        r = client.service.process()

        r = self._process_response(r)

        return r

    def lista_mensagens(self):
        client = self.get_client(wsdl=self._get_wsl("ListaMsgDisponiveisProxy"))

        r = client.service.process()

        r = self._process_response(r)

        return r

    def envia_mensagem(
        self, cod_intercambio: str, flag_compactacao: bool, msg_b64_bytes: bytes
    ):
        client = self.get_client(wsdl=self._get_wsl("EnvioMensagemProxy"))

        data = dict(
            codIntercambio=cod_intercambio,
            flgCompactacao=flag_compactacao,
            dscConteudoMensagem=msg_b64_bytes,
        )

        r = client.service.process(**data)

        r = self._process_response(r)

        return r

    def recupera_mensagem(self, identifier):
        client = self.get_client(wsdl=self._get_wsl("RecuperacaoMensagemProxy"))

        data = dict(trackingId=identifier)

        r = client.service.process(**data)

        r = self._process_response(r)

        return r

    def confirma_retirada(self, identifier, data_retirada, file_name):
        client = self.get_client(wsdl=self._get_wsl("ConfirmacaoRetiradaProxy"))

        data = dict(
            trackingID=identifier, dataRetirada=data_retirada, nmeArquivo=file_name
        )

        r = client.service.process(**data)

        r = self._process_response(r)

        return r
