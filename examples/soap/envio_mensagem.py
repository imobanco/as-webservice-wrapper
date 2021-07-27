import os

from as_ws_wrapper.wrapper.as_ws import AccesstageSoapWrapper
from as_ws_wrapper.adapters.csv import PydanticCSVAdapter
from examples.utils import dump_response
from examples.csv.sample import transactions


data = PydanticCSVAdapter().pydantic_to_csv(transactions)
r = AccesstageSoapWrapper().envia_mensagem("1494574", False, data)

dump_response(r.data, os.path.basename(__file__).split(".")[0])
