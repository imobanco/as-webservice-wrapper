from typing import List

from ..models.base import TransactionModel
from as_ws_wrapper.adapters.csv import PydanticCSVAdapter
from as_ws_wrapper.adapters.b64 import StringBase64Adapter


class PydanticBase64Adapter:
    """
    Adaptador

    BaseModel(pydantic) <===> string base 64
    """

    def pydantic_to_b64(
        self,
        instances: List[TransactionModel],
        pydantic_class=TransactionModel,
        delimiter=PydanticCSVAdapter.SEMICOLON,
    ):
        csv_string = PydanticCSVAdapter().pydantic_to_csv_string(
            instances, pydantic_class, delimiter
        )
        b64 = StringBase64Adapter().string_to_b64(csv_string)
        return b64

    def b64_to_pydantic(
        self,
        base64_string,
        pydantic_class=TransactionModel,
        delimiter=PydanticCSVAdapter.SEMICOLON,
    ):
        csv_string = StringBase64Adapter().b64_to_string(base64_string)
        instances = PydanticCSVAdapter().csv_string_to_pydantic(
            csv_string, pydantic_class, delimiter
        )
        return instances
