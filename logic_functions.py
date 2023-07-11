from secrets import choice
import string
import tkinter as tk


def generate_password(checkbutton_upper_var: tk.IntVar, checkbutton_lower_var: tk.IntVar,
                      checkbutton_numbers_var: tk.IntVar, checkbutton_symbols_var: tk.IntVar,
                      radiobutton_var: tk.IntVar, pass_len: tk.IntVar, password_text: tk.StringVar) \
        -> None:
    """
    :param checkbutton_upper_var: IntVar для кнопки checkbutton_upper
    :param checkbutton_lower_var: IntVar для кнопки checkbutton_lower
    :param checkbutton_numbers_var: IntVar для кнопки checkbutton_numbers
    :param checkbutton_symbols_var: IntVar для кнопки checkbutton_symbols
    :param radiobutton_var: IntVar для кнопок radiobutton
    :param pass_len:  IntVar длинны пароля
    :param password_text: StringVar сгенерированного пароля
    :return: Выводит результат генерации на GUI по нажатию кнопки generate_password_button

    Основная функция, генерирует пароль основываясь на 1 slider, 2 radio buttons и 4 check buttons
    """
    checkbutton_sum = checkbutton_upper_var.get() + checkbutton_lower_var.get() + checkbutton_numbers_var.get() + \
                      checkbutton_symbols_var.get()
    if radiobutton_var.get() == 0:
        character_list = get_easy_to_read_table_set(checkbutton_sum)
    elif radiobutton_var.get() == 1:
        character_list = get_easy_to_say_table_set(checkbutton_sum)
    password = []
    for symbol in range(pass_len.get()):
        password.append(choice(character_list))
    password = ''.join(password)
    password_text.set(password)


def get_easy_to_read_table_set(value: int) -> str:
    """
    Создает кастомный набор легкоразличимых символов
    :param value: Сумма 4 check buttons для получения всех комбинаций
    :return: Одна из 15 комбинаций символов для генерации пароля
    """
    character_list = ''
    upper = 'ABCDEFGHJKMNPQRSTUVXYZ'
    lower = 'abcdefghjkmnpqrstuvxyz'
    numbers = '23456789'
    symbols = '!"#$%&\'()*+,-./:;<=>?@[\]_{}~'
    match value:
        case 1:
            character_list = upper
        case 10:
            character_list = lower
        case 11:
            character_list = upper + lower
        case 100:
            character_list = numbers
        case 101:
            character_list = upper + numbers
        case 110:
            character_list = lower + numbers
        case 111:
            character_list = upper + lower + numbers
        case 1_000:
            character_list = symbols
        case 1_001:
            character_list = upper + symbols
        case 1_010:
            character_list = lower + symbols
        case 1_011:
            character_list = upper + lower + symbols
        case 1_100:
            character_list = numbers + symbols
        case 1_101:
            character_list = upper + numbers + symbols
        case 1_110:
            character_list = lower + numbers + symbols
        case 1_111:
            character_list = upper + lower + numbers + symbols
    return character_list


def get_easy_to_say_table_set(value: int) -> str:
    """
    Создает набор из заглавных и строчных букв
    :param value: Сумма 2 check buttons для получения всех комбинаций
    :return: Одна из 3 комбинаций символов для генерации пароля
    """
    character_list = ''
    if value == 1:
        character_list += string.ascii_uppercase
    elif value == 10:
        character_list += string.ascii_lowercase
    elif value == 11:
        character_list += string.ascii_letters
    return character_list


# Скрипты элементов tkinter
def check_whether_password_len_is_valid(password_length_entry: tk.Entry, pass_len_txt: tk.StringVar,
                                        pass_len: tk.IntVar, event=None) \
        -> None:
    """
    :param password_length_entry: Форма ввода (tk.Entry) password_length_entry
    :param pass_len_txt: StringVar длинны сгенерированного пароля
    :param pass_len: IntVar длинны пароля
    :param event: Затычка для bind

    Проверяет длину пароля в Entry и не позволяет сделать его вне установленного диапазона
    """
    try:
        int(password_length_entry.get())
        if int(password_length_entry.get()) < 4:
            pass_len_txt.set('4')
            pass_len.set(4)
        elif int(password_length_entry.get()) > 20:
            pass_len_txt.set('20')
            pass_len.set(20)
    except ValueError:
        pass_len_txt.set('4')


def change_entry_len_to_match_slider(password_length_entry: tk.Entry, pass_len: tk.IntVar, event=None) \
        -> None:
    """
    :param password_length_entry: Форма ввода (tk.Entry) password_length_entry
    :param pass_len: IntVar длинны пароля
    :param event: Затычка для bind

    Изменяет значение в Entry на значение выбранное в Slider
    """
    password_length_entry.delete(0, tk.END)
    password_length_entry.insert(0, pass_len.get())


def activate_checkboxes_on_radiobutton(checkbutton_numbers: tk.Checkbutton, checkbutton_numbers_var: tk.IntVar,
                                       checkbutton_symbols: tk.Checkbutton, checkbutton_symbols_var: tk.IntVar) \
        -> None:
    """
    :param checkbutton_numbers: Объект tk.Checkbutton
    :param checkbutton_numbers_var: IntVar для кнопки checkbutton_numbers
    :param checkbutton_symbols_var: IntVar для кнопки checkbutton_symbols
    :param checkbutton_symbols: Объект tk.Checkbutton

    Делает активными 2 checkbox при нажатии кнопки 'Easy to read'
    """
    checkbutton_numbers.config(state='active')
    checkbutton_numbers_var.set(100)
    checkbutton_symbols.config(state='active')
    checkbutton_symbols_var.set(1_000)


def disable_checkboxes_on_radiobutton(checkbutton_numbers: tk.Checkbutton, checkbutton_numbers_var: tk.IntVar,
                                      checkbutton_symbols: tk.Checkbutton, checkbutton_symbols_var: tk.IntVar) \
        -> None:
    """
    :param checkbutton_numbers: Объект tk.Checkbutton
    :param checkbutton_numbers_var: IntVar для кнопки checkbutton_numbers
    :param checkbutton_symbols_var: IntVar для кнопки checkbutton_symbols
    :param checkbutton_symbols: Объект tk.Checkbutton

    Делает неактивными 2 чекбокса при нажатии кнопки 'Easy to say'
    """
    checkbutton_numbers.config(state='disabled')
    checkbutton_numbers_var.set(0)
    checkbutton_symbols.config(state='disabled')
    checkbutton_symbols_var.set(0)


def make_1_checkbutton_active(checkbutton_upper_var: tk.IntVar, checkbutton_lower_var: tk.IntVar,
                              checkbutton_numbers_var: tk.IntVar, checkbutton_symbols_var: tk.IntVar,
                              checkbutton: tk.Checkbutton) \
        -> None:
    """
    :param checkbutton_upper_var: IntVar для кнопки checkbutton_upper
    :param checkbutton_lower_var: IntVar для кнопки checkbutton_lower
    :param checkbutton_numbers_var: IntVar для кнопки checkbutton_numbers
    :param checkbutton_symbols_var: IntVar для кнопки checkbutton_symbols
    :param checkbutton: Один из 4-ех объектов tk.Checkbutton, который был нажат

    Проверяет состояние четырех checkbox и если остался только один, не даёт его выключить
    """
    checkbutton_sum = checkbutton_upper_var.get() + checkbutton_lower_var.get() + checkbutton_numbers_var.get() + \
                      checkbutton_symbols_var.get()
    if checkbutton_sum == 0:
        match str(checkbutton):
            case 'PY_VAR3':
                checkbutton.set(1)
            case 'PY_VAR4':
                checkbutton.set(10)
            case 'PY_VAR5':
                checkbutton.set(100)
            case 'PY_VAR6':
                checkbutton.set(1_000)


def copy_on_button(window: object, password_text: tk.StringVar, event=None) -> None:
    """
    :param window: Основное окно объекта tk.Tk()
    :param password_text: StringVar сгенерированного пароля
    :param event: Затычка для bind

    Копирует значение Label 'generated_password' по нажатию кнопки 'Copy'
    """
    window.clipboard_clear()
    window.clipboard_append(password_text.get())
