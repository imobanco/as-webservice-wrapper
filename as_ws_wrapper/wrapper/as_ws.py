from .soap import BaseSoapWrapper


class AccesstageSoapWrapper(BaseSoapWrapper):
    def lista_servicos(self):
        client = self.get_client(
            wsdl="https://www.accesstage.com.br/ASTrafegoWS/ProxyServices/ListaServicosDisponiveisProxy?wsdl"
        )
        client.wsdl.dump()

        r = client.service.process()

        return r

    def lista_mensagens(self):
        client = self.get_client(
            wsdl="https://www.accesstage.com.br/ASTrafegoWS/ProxyServices/ListaMsgDisponiveisProxy?wsdl"
        )
        client.wsdl.dump()

        r = client.service.process()

        return r

    def envia_mensagem(self):
        client = self.get_client(
            wsdl="https://www.accesstage.com.br/ASTrafegoWS/ProxyServices/EnvioMensagemProxy?wsdl"
        )
        client.wsdl.dump()

        r = client.service.process()

        return r

    def recupera_mensagem(self):
        client = self.get_client(
            wsdl="https://www.accesstage.com.br/ASTrafegoWS/ProxyServices/RecuperacaoMensagemProxy?wsdl"
        )
        client.wsdl.dump()

        r = client.service.process()

        return r

    def confirma_retirada(self):
        client = self.get_client(
            wsdl="https://www.accesstage.com.br/ASTrafegoWS/ProxyServices/ConfirmacaoRetiradaProxy?wsdl"
        )
        client.wsdl.dump()

        r = client.service.process()

        return r
