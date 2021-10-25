import os

from as_ws_wrapper.adapters.csv import PydanticCSVAdapter
from examples.utils import dump_response, read_json

try:
    mensagens_data = read_json("mensagens_do_dia")
except Exception:
    mensagens_data = []

mensagens_instances = []
invalid = []

for msg in mensagens_data:
    csv_data = msg["dscConteudoMensagem"]
    trk_id = msg["trkIdIn"]
    try:
        instances = PydanticCSVAdapter().csv_to_pydantic(csv_data, use_bytes=False)

        for instance in instances:
            instance.trk_id = trk_id

        mensagens_instances.extend(instances)
    except Exception as e:
        invalid.append((msg['trkIdIn'], str(e)))


instances_data = [instance.dict() for instance in mensagens_instances]

data = {
    "valid": list({instance.trk_id for instance in mensagens_instances}),
    "invalid": invalid,
    "invalid_msgs": [data for data in mensagens_data if data['trkIdIn'] in [item[0] for item in invalid]]
}

dump_response(data, os.path.basename(__file__).split(".")[0])
