import os

from as_ws_wrapper.wrapper.as_ws import AccesstageSoapWrapper
from examples.utils import dump_response


r = AccesstageSoapWrapper().recupera_mensagem("202103298171334")

r.data['dscConteudoMensagem'] = r.data['dscConteudoMensagem'].decode()


dump_response(r.data, os.path.basename(__file__).split(".")[0])
