import os

from as_ws_wrapper.wrapper.as_ws import AccesstageSoapWrapper
from as_ws_wrapper.adapters.csv import PydanticCSVAdapter

from examples.utils import dump_response

r = AccesstageSoapWrapper().lista_mensagens('1628267')

mensagens = []

for msg in r.data:
    if msg['tipoDocumento'] in ['PAGAMENTO', 'OUTOS ']:
        mensagens.append(msg)

mensagens_data = []

for msg in mensagens:
    mensagem = AccesstageSoapWrapper().recupera_mensagem(f"{msg['trkIdIn']}")
    mensagem.data["dscConteudoMensagem"] = mensagem.data["dscConteudoMensagem"].decode('iso-8859-1')
    mensagem.data['trkIdIn'] = msg['trkIdIn']
    mensagem.data['tipoDocumento'] = msg['tipoDocumento']
    if 'payer_document' in mensagem.data["dscConteudoMensagem"]:
        mensagens_data.append(mensagem.data)


mensagens_instances = []

for msg in mensagens_data:
    csv_data = msg['dscConteudoMensagem']
    trk_id = msg['trkIdIn']
    try:
        instances = PydanticCSVAdapter().csv_to_pydantic(csv_data, use_bytes=False)

        for instance in instances:
            instance.trk_id = trk_id

        mensagens_instances.extend(instances)
    except Exception as e:
        print(e)


instances_data = [
    instance.dict() for instance in mensagens_instances
]


dump_response(mensagens_instances, os.path.basename(__file__).split(".")[0])
