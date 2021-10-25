import logging
import threading
import os

from as_ws_wrapper.wrapper.as_ws import AccesstageSoapWrapper
from examples.utils import dump_response

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)-15s| %(threadName)-10s| %(levelname)-5s| %(message)s",
)

r = AccesstageSoapWrapper().lista_mensagens("1628267")

mensagens = []

for msg in r.data:
    if (
        msg["tipoDocumento"] in ["PAGAMENTO", "OUTROS "]
    ):
        mensagens.append(msg)


number_of_threads = 8
total_items = len(mensagens)
per_thread = int(total_items/number_of_threads)

correct_map = "payer_document;payer_document_type;payer_name;payer_bank_account_number;payer_bank_account_number_dv;payer_bank_account_routing;payer_bank_account_routing_dv;payer_convenio;receiver_document"  # noqa

invalid_msgs = []

def retirar_de_slice(i):
    logger = logging.getLogger(__name__)

    start_index = i * per_thread
    end_index = (i *per_thread ) + per_thread

    for index in range(start_index, end_index):
        msg = mensagens[index]
        mensagem = AccesstageSoapWrapper().recupera_mensagem(f"{msg['trkIdIn']}")
        mensagem.data["dscConteudoMensagem"] = mensagem.data["dscConteudoMensagem"].decode(
            "iso-8859-1"
        )
        mensagem.data.update(**msg)

        if correct_map in mensagem.data["dscConteudoMensagem"]:
            logger.info(f"{index} CSV mapa correto ++")
        elif ";" in mensagem.data["dscConteudoMensagem"]:
            logger.info(f"{index} CSV mapa incorreto --")
            invalid_msgs.append(mensagem.data)
        else:
            logger.info(f"{index} CNAB")


threads = []

for i in range(number_of_threads):
    start_index = i
    thread = threading.Thread(
        target=retirar_de_slice, name=f"thread-{i}", args=[i]
    )
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
