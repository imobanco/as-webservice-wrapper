import os

from as_ws_wrapper.wrapper.as_ws import AccesstageSoapWrapper
from examples.utils import dump_response

r = AccesstageSoapWrapper().lista_servicos()

dump_response(r.data, os.path.basename(__file__).split(".")[0])
