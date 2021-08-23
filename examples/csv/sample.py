import os

from as_ws_wrapper.adapters.csv import PydanticCSVAdapter
from examples.utils import dump_csv
from tests.factories import create_invoice_transaction, create_ted_transaction

transactions = [
    create_invoice_transaction(),
    create_ted_transaction(),
]

csv_string = PydanticCSVAdapter().pydantic_to_csv(transactions, use_bytes=False)

dump_csv(csv_string, os.path.basename(__file__).split(".")[0])
