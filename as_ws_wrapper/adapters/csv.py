from csv import DictWriter, DictReader
from io import StringIO
from typing import List

from pydantic import BaseModel


class PydanticCSVAdapter:
    """
    Adaptador

    BaseModel(pydantic) <===> csv string
    """

    COMMA = ","
    SEMICOLON = ";"
    SPACE = " "
    TAB = "\t"
    PIPE = "|"

    def pydantic_to_csv_string(
        self,
        instances: List[BaseModel],
        pydantic_class: BaseModel.__class__,
        delimiter=SEMICOLON,
    ):
        instances_data = [instance.dict() for instance in instances]

        buffer = StringIO()

        writer = DictWriter(
            buffer, list(pydantic_class.__fields__.keys()), delimiter=delimiter
        )
        writer.writeheader()
        writer.writerows(instances_data)
        return buffer.getvalue()

    def csv_string_to_pydantic(
        self, csv_string: str, pydantic_class: BaseModel.__class__, delimiter=SEMICOLON
    ):
        buffer = StringIO(csv_string)
        reader = DictReader(
            buffer, list(pydantic_class.__fields__.keys()), delimiter=delimiter
        )
        instances = []
        for index, row in enumerate(reader):
            if index == 0:
                continue
            instances.append(pydantic_class(**row))
        return instances
