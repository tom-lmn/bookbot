def get_num_words(string):
    word_list = string.split()
    return len(word_list)

def get_char_nums(string):
    string_lower = string.lower()
    char_nums = dict()
    for i in range(len(string_lower)):
        if not string_lower[i] in char_nums:
            char_nums[string_lower[i]] = 1
        else: 
            char_nums[string_lower[i]] += 1
    return char_nums

def sort_on(items):
    return items["num"]
 
def sort_char_dict(char_dict):
    dict_list = []
    for char in char_dict:
        d = dict()
        d["char"] = char
        d["num"] = char_dict[char]
        dict_list.append(d)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
                
