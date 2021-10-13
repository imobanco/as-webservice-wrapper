import os

from as_ws_wrapper.wrapper.as_ws import AccesstageSoapWrapper
from examples.utils import dump_response

r = AccesstageSoapWrapper().confirma_retirada("202108267888502", "Retirada")

dump_response(r.data, os.path.basename(__file__).split(".")[0])
