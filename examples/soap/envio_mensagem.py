import os

from as_ws_wrapper.wrapper.as_ws import AccesstageSoapWrapper
from as_ws_wrapper.adapters.csv_b64 import PydanticBase64Adapter
from examples.utils import dump_response
from examples.csv.sample import transactions


data = PydanticBase64Adapter().pydantic_to_b64(transactions)
r = AccesstageSoapWrapper().envia_mensagem("1491486", False, data)

dump_response(r.data, os.path.basename(__file__).split(".")[0])
