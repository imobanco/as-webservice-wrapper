import os

from as_ws_wrapper.adapters.csv import PydanticCSVAdapter
from as_ws_wrapper.wrapper.as_ws import AccesstageSoapWrapper
from examples.csv.sample import transactions
from examples.utils import dump_response

data = PydanticCSVAdapter().pydantic_to_csv(transactions)
r = AccesstageSoapWrapper().envia_mensagem("1606224", False, data)

dump_response(r.data, os.path.basename(__file__).split(".")[0])
