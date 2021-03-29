import os
import datetime

from as_ws_wrapper.wrapper.as_ws import AccesstageSoapWrapper
from examples.utils import dump_response

r = AccesstageSoapWrapper().confirma_retirada("202103298168513", datetime.datetime.now().isoformat(), "qwe")

dump_response(r.data, os.path.basename(__file__).split(".")[0])
