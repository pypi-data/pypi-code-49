import json


def create_json_file(json_file_path: str):
    """

    :param str, json_file_path: path to a json file
    :return:
    """
    if json_file_path[-4:] != '.json':
        json_file_path += '.json'

    with open(json_file_path, 'w+') as file:
        json.dump({}, file)

    return json_file_path


def load_json_file(json_file_path):
    json_file = open(json_file_path, "r")  # Open the JSON file for reading
    data = json.load(json_file)  # Read the JSON into the buffer
    json_file.close()  # Close the JSON file
    return data


def update_json_file(json_file_path: str,
                     data_to_update_with: dict):
    """
    update a json file with data. the data must be in the form of a dictionary.

    if the key of the dictionary value to add into the json file doesn't exist in the json file, create a new key
    value pair based on the data passed through.

    if the key of the dictionary value to add into the json file does exist in the json file and the value is a
    dictionary itself, update the current value to include the new dictionary value.

    if the key of the dictionary value to add into the json file does exist in the json file and the value is a
    list itself, update the current value to include the new list value.


    if the key of the dictionary value to add into the json file does exist in the json file and the value is a single
    value that isn't a dictionary or list, overwrite the value


    :param json_file_path:
    :param data_to_update_with:
    :return:
    """
    data_to_update_with_key = list(data_to_update_with.keys())[0]
    data_to_update_with_value = list(data_to_update_with.values())[0]
    data_to_update_with_value_type = type(data_to_update_with_value)

    data = load_json_file(json_file_path=json_file_path)

    existing_value_for_the_data_to_update_with_same_key = data.get(data_to_update_with_key)

    if existing_value_for_the_data_to_update_with_same_key is None:
        # if there is no existing value for the key you want to add to the json with, then just add it
        data[data_to_update_with_key] = data_to_update_with_value
    elif data_to_update_with_key is not None and data_to_update_with_value_type is dict:
        # if the key exists in the json but the value is  of the type dictionary, then add the new dictionary into
        #  the existing dictionary value
        existing_value_for_the_data_to_update_with_same_key.update(data_to_update_with_value)
    elif data_to_update_with_key is not None and data_to_update_with_value_type is list:
        # if the key exists in the json but the value is  of the type list, then add the new list values into
        #  the existing list value
        for item_in_list in data_to_update_with_value:
            existing_value_for_the_data_to_update_with_same_key.append(item_in_list)
    else:
        # if the key exists in the json, overwrite the value
        data[data_to_update_with_key] = data_to_update_with_value

    # Save changes to JSON file
    json_file = open(json_file_path, "w+")
    json_file.write(json.dumps(data))
    json_file.close()

    return json_file_path


