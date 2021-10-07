import os

from as_ws_wrapper.adapters.csv import PydanticCSVAdapter
from examples.utils import dump_response, read_json

try:
    mensagens_data = read_json('mensagens_do_dia')
except Exception:
    mensagens_data = []

mensagens_instances = []

for msg in mensagens_data:
    csv_data = msg["dscConteudoMensagem"]
    trk_id = msg["trkIdIn"]
    try:
        instances = PydanticCSVAdapter().csv_to_pydantic(csv_data, use_bytes=False)

        for instance in instances:
            instance.trk_id = trk_id

        mensagens_instances.extend(instances)
    except Exception as e:
        pass


instances_data = [instance.dict() for instance in mensagens_instances]


dump_response(instances_data, os.path.basename(__file__).split(".")[0])
