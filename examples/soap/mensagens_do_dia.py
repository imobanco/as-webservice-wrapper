import os

from as_ws_wrapper.wrapper.as_ws import AccesstageSoapWrapper

from examples.utils import dump_response, read_json

try:
    mensagens_data = read_json(os.path.basename(__file__).split('.')[0])
except Exception:
    mensagens_data = []

mensagens_data_trkIdIn = [
    msg['trkIdIn'] for msg in mensagens_data
]

r = AccesstageSoapWrapper().lista_mensagens('1628267')

mensagens = []

for msg in r.data:
    if msg['tipoDocumento'] in ['PAGAMENTO', 'OUTROS '] and msg['trkIdIn'] not in mensagens_data_trkIdIn:
        mensagens.append(msg)

for msg in mensagens:
    mensagem = AccesstageSoapWrapper().recupera_mensagem(f"{msg['trkIdIn']}")
    mensagem.data["dscConteudoMensagem"] = mensagem.data["dscConteudoMensagem"].decode('iso-8859-1')
    mensagem.data['trkIdIn'] = msg['trkIdIn']
    mensagem.data['tipoDocumento'] = msg['tipoDocumento']
    mensagens_data.append(mensagem.data)


dump_response(mensagens_data, os.path.basename(__file__).split(".")[0])
