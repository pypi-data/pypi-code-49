# -*- coding: utf-8 -*-


def list_split_by_length(data_list, length_interval):
    list_final = []
    data_len = len(data_list)
    times = data_len / length_interval
    for index in range(0, times+1):
        begin = index * length_interval
        end = begin + length_interval
        if end > data_len:
            end = data_len
        list_final.append(data_list[begin:end])
    return list_final
