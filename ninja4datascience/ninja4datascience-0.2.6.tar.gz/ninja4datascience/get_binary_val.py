def get_binary_val(data, start_index, end_index):
    binary_val = bin(data)
    extracted_binary_val = int(bin(binary_val), 2)
    extracted_binary_str_val = str(extracted_binary_val)
    extracted_binary_val = int(extracted_binary_str_val[start_index:end_index])
    data_len = int(extracted_binary_val)
    return data_len
