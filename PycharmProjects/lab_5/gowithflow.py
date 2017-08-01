# -*- coding: utf-8 -*-


def sum_of_list(list_data):
    result = sum(list_data)
    return result


def merge_and_sort(list_data_a, list_data_b):
    result = list_data_a + list_data_b
    result.sort()
    return result


def delete_a_list_element(list_data, element_value):
    list_length = len(list_data)
    for i in range(list_length):
        if element_value == list_data[i]:
            list_data.remove(element_value)
            result = list_data
            break
        else:
            result = 0
    return result

def comparison_list_size(list_data_a, list_data_b):
    if len(list_data_a) > len(list_data_b):
        result = list_data_a
    else:
        result = list_data_b

    return result


def odd_even_check(a, b):
    if (a + b) % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    return result


def discount_price(price):
    if price < 100000:
        result = (price * 0.9)
    else:
        result = (price * 0.8)

    return result


def find_smallest_value(list_data):
    list_length = int(len(list_data))
    ind_num = 0
    for i in range(list_length):
        if i == ind_num:
            pass
        else:
            if list_data[ind_num] < list_data[i]:
                continue
            elif list_data[ind_num] > list_data[i]:
                ind_num = i
    result = list_data[ind_num]
    return result


def binary_converter(decimal_number):
    global result
    result = ''
    while (decimal_number > 0):
        remainder = decimal_number % 2
        decimal_number = decimal_number // 2
        result = str(remainder) + result
    return result


def number_of_cases(list_data):
    extract_list = []
    list_length = len(list_data)
    overlap_count = -1
    all_str_list = []
    for k in list_data:
        all_str_list+=str(k)
    for i in range(list_length):
        for j in range(list_length):
            extract_list.append(all_str_list[i] + all_str_list[j])
            overlap_count += 1
            if extract_list.count((all_str_list[j] + all_str_list[i])) >1:
                extract_list.pop(overlap_count)
                overlap_count -= 1
            if extract_list.count((all_str_list[i] + all_str_list[j])) >1:
                extract_list.pop(overlap_count)
                overlap_count -= 1
    result = extract_list

    return result

def main():
    print(odd_even_check(3.2,4.8))
    # ==================================


if __name__ == "__main__":
    main()
