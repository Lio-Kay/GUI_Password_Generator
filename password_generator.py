# def get_tableset_if_easy_to_read():
#     upper_option = checkbutton_upper_var
#     lower_option = checkbutton_lower_var
#     symbols_option = checkbutton_symbols_var
#     character_list = ''
#     allowed_numbers = '23456789'
#     allowed_upper_letters = 'ABCDEFGHJKMNPQRSTUVXYZ'
#     allowed_lower_letters = 'abcdefghjkmnpqrstuvxyz'
#     allowed_symbols = '!"#$%&()*+,-.:;<=>?@[\]^_{}~'
#     if sum(upper_option, lower_option, symbols_option) == 0:
#         character_list += allowed_numbers
#     elif sum(upper_option, lower_option, symbols_option) == 1:
#         character_list += allowed_numbers
#         character_list += allowed_upper_letters
#     elif sum(upper_option, lower_option, symbols_option) == 10:
#         character_list += allowed_numbers
#         character_list += allowed_lower_letters
#     elif sum(upper_option, lower_option, symbols_option) == 11:
#         character_list += allowed_numbers
#         character_list += allowed_upper_letters
#         character_list += string.ascii_lowercase
#     elif sum(upper_option, lower_option, symbols_option) == 100:
#         character_list += allowed_numbers
#         character_list += allowed_symbols
#     elif sum(upper_option, lower_option, symbols_option) == 101:
#         character_list += allowed_numbers
#         character_list += allowed_upper_letters
#         character_list += allowed_symbols
#     elif sum(upper_option, lower_option, symbols_option) == 110:
#         character_list += allowed_numbers
#         character_list += allowed_lower_letters
#         character_list += allowed_symbols
#     elif sum(upper_option, lower_option, symbols_option) == 111:
#         character_list += allowed_numbers
#         character_list += allowed_upper_letters
#         character_list += allowed_lower_letters
#         character_list += allowed_symbols
#
#
# def get_tableset_if_easy_to_say():
#     pass
#
#
# def get_tableset_if_no_radiobutton_options():
#     upper_option = checkbutton_upper_var
#     lower_option = checkbutton_lower_var
#     symbols_option = checkbutton_symbols_var
#     character_list = ''
#     if sum(upper_option, lower_option, symbols_option) == 0:
#         character_list += string.digits
#     elif sum(upper_option, lower_option, symbols_option) == 1:
#         character_list += string.digits
#         character_list += string.ascii_uppercase
#     elif sum(upper_option, lower_option, symbols_option) == 10:
#         character_list += string.digits
#         character_list += string.ascii_lowercase
#     elif sum(upper_option, lower_option, symbols_option) == 11:
#         character_list += string.digits
#         character_list += string.ascii_uppercase
#         character_list += string.ascii_lowercase
#     elif sum(upper_option, lower_option, symbols_option) == 100:
#         character_list += string.digits
#         character_list += string.punctuation
#     elif sum(upper_option, lower_option, symbols_option) == 101:
#         character_list += string.digits
#         character_list += string.ascii_uppercase
#         character_list += string.punctuation
#     elif sum(upper_option, lower_option, symbols_option) == 110:
#         character_list += string.digits
#         character_list += string.ascii_lowercase
#         character_list += string.punctuation
#     elif sum(upper_option, lower_option, symbols_option) == 111:
#         character_list += string.digits
#         character_list += string.ascii_uppercase
#         character_list += string.ascii_lowercase
#         character_list += string.punctuation