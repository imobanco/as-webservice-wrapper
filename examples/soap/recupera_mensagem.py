import os

from as_ws_wrapper.wrapper.as_ws import AccesstageSoapWrapper
from examples.utils import dump_response

r = AccesstageSoapWrapper().recupera_mensagem("202108308901467")

r.data["dscConteudoMensagem"] = r.data["dscConteudoMensagem"].decode("iso-8859-1")

dump_response(r.data, os.path.basename(__file__).split(".")[0])
