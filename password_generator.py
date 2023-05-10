from secrets import choice
import string


def generate_password() -> str:
    from tkinter_structure import collect_data_to_generate_password
    data = collect_data_to_generate_password()
    if data['Radiobutton value'] == 0:
        character_list = get_easy_to_read_tableset(data['Checkbutton value'])
    elif data['Radiobutton value'] == 1:
        character_list = get_easy_to_say_tableset(data['Checkbutton Value'])
    password = []
    for symbol in range(data['Password len']):
        password.append(choice(character_list))
    return ''.join(password)


def get_easy_to_read_tableset(value:int) -> str:
    character_list = ''
    allowed_numbers = '23456789'
    allowed_upper_letters = 'ABCDEFGHJKMNPQRSTUVXYZ'
    allowed_lower_letters = 'abcdefghjkmnpqrstuvxyz'
    allowed_symbols = '!"#$%&()*+,-.:;<=>?@[\/]^_{}~'
    if value == 1:
        character_list += allowed_numbers
    elif value == 10:
        character_list += allowed_upper_letters
    elif value == 11:
        character_list += allowed_numbers
        character_list += allowed_upper_letters
    elif value == 100:
        character_list += allowed_lower_letters
    elif value == 101:
        character_list += allowed_numbers
        character_list += allowed_lower_letters
    elif value == 111:
        character_list += allowed_numbers
        character_list += allowed_upper_letters
        character_list += allowed_lower_letters
    elif value == 1_000:
        character_list += allowed_symbols
    elif value == 1_001:
        character_list += allowed_numbers
        character_list += allowed_symbols
    elif value == 1_010:
        character_list += allowed_upper_letters
        character_list += allowed_symbols
    elif value == 1_100:
        character_list += allowed_lower_letters
        character_list += allowed_symbols
    elif value == 1_011:
        character_list += allowed_numbers
        character_list += allowed_upper_letters
        character_list += allowed_symbols
    elif value == 1_111:
        character_list += allowed_numbers
        character_list += allowed_upper_letters
        character_list += allowed_lower_letters
        character_list += allowed_symbols
    return character_list


def get_easy_to_say_tableset(value:int) -> str:
    character_list = ''
    if value == 10:
        character_list += string.ascii_uppercase
    elif value == 100:
        character_list += string.ascii_lowercase
    elif value == 110:
        character_list += string.ascii_uppercase
        character_list += string.ascii_lowercase
    return character_list
