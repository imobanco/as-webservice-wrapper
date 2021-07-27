import os

from examples.utils import dump_csv
from as_ws_wrapper.adapters.csv import PydanticCSVAdapter
from tests.factories import create_ted_transaction, create_invoice_transaction


transactions = [
    create_invoice_transaction(),
    create_ted_transaction(),
]

csv_string = PydanticCSVAdapter().pydantic_to_csv(
    transactions, return_as_bytes=False
)

dump_csv(csv_string, os.path.basename(__file__).split(".")[0])
