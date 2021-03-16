import os

from as_ws_wrapper.wrapper.as_ws import AccesstageSoapWrapper
from examples.utils import dump_response


r = AccesstageSoapWrapper().recupera_mensagem()

dump_response(r, os.path.basename(__file__).split(".")[0])
