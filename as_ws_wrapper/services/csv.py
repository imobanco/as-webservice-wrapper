from csv import DictWriter, DictReader
from io import StringIO
from typing import List

from ..models.base import TransactionModel


class CSVService:
    COMMA = ','
    SEMICOLON = ';'
    SPACE = ' '
    TAB = '\t'
    PIPE = '|'

    def parse_transactions_to_csv_string(
        self, instances: List[TransactionModel], delimiter=SEMICOLON
    ):
        instances_data = [instance.dict() for instance in instances]

        buffer = StringIO()

        writer = DictWriter(buffer, list(TransactionModel.__fields__.keys()), delimiter=delimiter)
        writer.writeheader()
        writer.writerows(instances_data)
        return buffer.getvalue()

    def parse_csv_string_to_transactions(self, csv_string: str, delimiter=SEMICOLON):
        buffer = StringIO(csv_string)
        reader = DictReader(buffer, list(TransactionModel.__fields__.keys()), delimiter=delimiter)
        instances = []
        for index, row in enumerate(reader):
            if index == 0:
                continue
            instances.append(
                TransactionModel(**row)
            )
        return instances
