import json
from clean_csv_data import list_all_files


def read_json(json_folder_name, file):
    file_name = json_folder_name + "/" + file
    price_list = []
    print("File  name is: {}".format(file_name))
    with open(file_name) as f:
        file_data = json.load(f)
    for key, value in file_data.items():
        price_list.append(value)
        print("For Date {} Price value is {}".format(key, value))
    plot_price(price_list)
    print("_______________________________________________________________________________________________________")
    return

def plot_price(price_list):
    pass


if __name__ == "__main__":
    json_folder_name = "processed_data"
    file_list = list_all_files(json_folder_name)
    #print(file_list)
    for file in file_list:
        read_json(json_folder_name, file)


