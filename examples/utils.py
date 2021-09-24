import json
import os


def dump_response(response, file_name):
    current_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_path, "data")

    file_path = os.path.join(data_path, f"{file_name}.json")
    with open(file_path, "w") as file:
        json.dump(response, file, indent=4)


def read_json(file_name):
    current_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_path, "data")

    file_path = os.path.join(data_path, f"{file_name}.json")
    with open(file_path, "r") as file:
        return json.load(file)


def dump_csv(csv_string, file_name):
    current_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(current_path, "data")

    file_path = os.path.join(data_path, f"{file_name}.csv")
    with open(file_path, "w") as file:
        file.write(csv_string)
