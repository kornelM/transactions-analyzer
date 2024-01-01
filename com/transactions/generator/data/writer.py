# Zapisanie do pliku JSON
import json

from com.transactions.properties import GENERATED_DATA_PATH


def write_to_json(name, data):
    data_size = len(data)
    full_file_name = GENERATED_DATA_PATH + name + ".json"
    print(f"Writing data (data size: {data_size}) to file: {full_file_name}.")

    with open(full_file_name, 'w') as file:
        json.dump(data, file, indent=2)
    print(f"Writing data has finished.")
