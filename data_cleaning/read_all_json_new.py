import json
from clean_csv_data import list_all_files


def read_json(file_name):
    with open(file_name) as f:
        file_data = json.load(f)
    print("_______________________ For file {} Data are following".format(file_name))

    for k, v in file_data.items():
        print("For Date {}, Price is {}".format(k, v))


if __name__ == "__main__":
    folder_name = "processed_data"
    file_list = list_all_files(folder_name)
    print("File list is {}".format(file_list))
    for file in file_list:
        file_name = folder_name + "/" + file
        read_json(file_name)
