def word_counter(file_contents):
    num_words = 0
    words = file_contents.split()
    for word in words:
        num_words += 1
    return num_words


def character_count(text):
    characters = {

        }
    for character in text:
        lower_case = character.lower()
        if lower_case not in characters:
            characters[lower_case] = 1
        else:
            characters[lower_case] += 1
    return characters

def chars_dict_to_sorted_list(num_characters):
    chars_list = []
    for char, count in num_characters.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    def sort_on(dict):
        return dict['count']
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
    






