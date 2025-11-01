def get_num_words(contents: str) -> int:
    list_words = []
    list_words = contents.split()
    return len(list_words)


def get_num_chars(contents: str):
    dict_char_nums = {" ": 0}

    contents = contents.lower()
    for char in contents:
        # if key doesn't exit, init it first
        if char not in dict_char_nums:
            dict_char_nums[char] = 1
            continue
        dict_char_nums[char] += 1
    return dict_char_nums


def sort_on(dict):
    return dict["num"]


def get_sorted_dict(dict):
    sorted_list = []

    for key in dict:
        dict_entry = {"char": key, "num": dict[key]}
        sorted_list.append(dict_entry)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
