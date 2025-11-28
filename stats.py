def count_words(src):
    return len(src.split())

def character_counts(text):
    char_map = {}

    for char in text:
        lowercase_char = char.lower()
        if lowercase_char not in char_map:
            char_map[lowercase_char] = 1
        else:
            char_map[lowercase_char] += 1
    
    return char_map

def convert_char_map_to_list(char_map):
    character_count_list = []
    for k,v in char_map.items():
        character_count_list.append({'char': k , 'num': v})
    
    return character_count_list

def sort_character_list(character_count_list):
    def sort_on(items):
        return items["num"]

    character_count_list.sort(reverse=True, key=sort_on)

    return character_count_list

def sort_character_map(char_map):
    character_count_list = convert_char_map_to_list(char_map)

    return sort_character_list(character_count_list)


