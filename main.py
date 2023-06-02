from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.utility import *
from secrets import choice
from screeninfo import get_monitors
import string


def generate_password() -> None:
    """
    Основная функция, генерирует пароль основываясь на 1 slider, 2 radiobuttons и 4 checkbuttons
    :return: Выводит резултат генерации на GUI по нажатию кнопки generate_password_button
    """
    checkbutton_sum = checkbutton_upper_var.get() + checkbutton_lower_var.get() + checkbutton_numbers_var.get() + \
                      checkbutton_symbols_var.get()
    if radiobutton_var.get() == 0:
        character_list = get_easy_to_read_tableset(checkbutton_sum)
    elif radiobutton_var.get() == 1:
        character_list = get_easy_to_say_tableset(checkbutton_sum)
    password = []
    for symbol in range(pass_len.get()):
        password.append(choice(character_list))
    password = ''.join(password)
    password_text.set(password)


def get_easy_to_read_tableset(value: int) -> str:
    """
    Создает кастомный набор легкоразлечимых символов
    :param value: Сумма 4 checkbuttons для получения всех комбинаций
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
            character_list = upper+lower
        case 100:
            character_list = numbers
        case 101:
            character_list = upper+numbers
        case 110:
            character_list = lower+numbers
        case 111:
            character_list = upper+lower+numbers
        case 1_000:
            character_list = symbols
        case 1_001:
            character_list = upper+symbols
        case 1_010:
            character_list = lower+symbols
        case 1_011:
            character_list = upper+lower+symbols
        case 1_100:
            character_list = numbers+symbols
        case 1_101:
            character_list = upper+numbers+symbols
        case 1_110:
            character_list = lower+numbers+symbols
        case 1_111:
            character_list = upper+lower+numbers+symbols
    return character_list


def get_easy_to_say_tableset(value: int) -> str:
    """
    Создает набор из заглавных и строчных букв
    :param value: Сумма 2 checkbuttons для получения всех комбинаций
    :return: Одна из 3 кобинаций символов для генерации пароля
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
def check_whether_password_len_is_valid(event=None) -> None:
    """
    Проверяет длинну пароля в Entry и не позволяет сделать его вне установленного диапазона
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


def change_entry_len_to_match_slider(event=None) -> None:
    """
    Изменяет значение в Entry на значение выбранное в Slider
    """
    password_length_entry.delete(0, END)
    password_length_entry.insert(0, pass_len.get())


def disable_checkboxes_on_radiobutton() -> None:
    """
    Делает неактивными 2 чекбокса про нажатию кнопки 'Easy to say'
    """
    checkbutton_numbers.config(state='disabled')
    checkbutton_numbers_var.set(0)
    checkbutton_symbols.config(state='disabled')
    checkbutton_symbols_var.set(0)
    checkbutton_upper_var.set(1)


def activate_checkboxes_on_radiobutton() -> None:
    """
    Делает активными 2 checkbox при нажании кнопки 'Easy to read'
    """
    checkbutton_numbers.config(state='active')
    checkbutton_symbols.config(state='active')


def make_1_checkbutton_active(checkbutton: object) -> None:
    """
    Проверяет состояние 4 4 checkbox и если остался только один, не даёт его выключить
    """
    checkbutton_sum = checkbutton_upper_var.get() + checkbutton_lower_var.get() + checkbutton_numbers_var.get() +\
                      checkbutton_symbols_var.get()
    if checkbutton_sum == 0:
        match str(checkbutton):
            case 'PY_VAR3': checkbutton.set(1)
            case 'PY_VAR4': checkbutton.set(10)
            case 'PY_VAR5': checkbutton.set(100)
            case 'PY_VAR6': checkbutton.set(1_000)


def copy_on_button(event=None) -> None:
    """
    Копирует значение Label 'generated_password' по нажатию кнопки 'Copy'
    """
    window.clipboard_clear()
    window.clipboard_append(password_text.get())


# Tk initialization
window = Tk()
window.title('Password Generator')
for monitor in get_monitors():
    if monitor.is_primary:
        width = monitor.width
        heigth = monitor.height
window.geometry(f'{round(width*0.2)}x{round(heigth*0.35)}+{round(width*0.1)}+{round(heigth*0.1)}')
for r in range(9): window.rowconfigure(index=r, weight=1)
for c in range(4): window.columnconfigure(index=c, weight=1)


# Style
style = ttk.Style('darkly')
style.configure('.', font=('Helvetica', 14), justify=CENTER)

# Vars
pass_len = IntVar()
pass_len.set(10)
pass_len_txt = StringVar()
pass_len_txt.set('10')
radiobutton_var = IntVar()
checkbutton_upper_var = IntVar(value=1)
checkbutton_lower_var = IntVar(value=10)
checkbutton_numbers_var = IntVar(value=100)
checkbutton_symbols_var = IntVar(value=1_000)
password_text = StringVar()
password_text.set('Your password will be here')

# Frames
window.configure(background='#141414', cursor='left_ptr')

length_label = ttk.Label(master=window, text='Password Length', style='success', font=('Helvetica', 14, 'bold'), anchor=CENTER)
password_length_entry = ttk.Entry(master=window, textvariable=pass_len_txt, font='Helvetica 14', justify=CENTER, width=11)
password_length_scale = ttk.Scale(master=window, from_=4, to=20, variable=pass_len, style='success')

radiobutton_easy_to_read = ttk.Radiobutton(master=window, text='Easy to read', variable=radiobutton_var,
                                       value=0, command=activate_checkboxes_on_radiobutton, style='success-toolbutton')
radiobutton_easy_to_say = ttk.Radiobutton(master=window, text='Easy to say', variable=radiobutton_var,
                                      value=1, command=disable_checkboxes_on_radiobutton, style='success-toolbutton')

checkbutton_upper = ttk.Checkbutton(master=window, text='Uppercase', variable=checkbutton_upper_var,
                                    command=lambda: make_1_checkbutton_active(checkbutton_upper_var),
                                    style='success-square-toggle')
checkbutton_lower = ttk.Checkbutton(master=window, text='Lowercase', variable=checkbutton_lower_var,
                                    onvalue=10, command=lambda: make_1_checkbutton_active(checkbutton_lower_var),
                                    style='success-square-toggle')
checkbutton_numbers = ttk.Checkbutton(master=window, text='Numbers', variable=checkbutton_numbers_var,
                                      onvalue=100, command=lambda: make_1_checkbutton_active(checkbutton_numbers_var),
                                      style='success-square-toggle')
checkbutton_symbols = ttk.Checkbutton(master=window, text='Symbols', variable=checkbutton_symbols_var,
                                      onvalue=1_000, command=lambda: make_1_checkbutton_active(checkbutton_symbols_var),
                                      style='success-square-toggle')

generated_password = ttk.Label(master=window, textvariable=password_text, style='success', anchor=CENTER)
generate_password_button = ttk.Button(master=window, text='Generate', command=generate_password, style='success-outline', width=10, padding=8)
copy_generated_password = ttk.Button(master=window, text='Copy', style='success-outline', width=10, padding=8)

# Binds
password_length_entry.bind('<KeyRelease>', check_whether_password_len_is_valid)
password_length_scale.bind('<ButtonRelease-1>', change_entry_len_to_match_slider)
copy_generated_password.bind('<ButtonRelease-1>', copy_on_button)


# Packing
length_label.grid(row=1, column=1, columnspan=2, ipadx=56, ipady=5)
password_length_entry.grid(row=2, column=1, pady=0, padx=(38, 0))
password_length_scale.grid(row=2, column=2, padx=(0, 42))
radiobutton_easy_to_read.grid(row=3, column=1, padx=(38, 0))
radiobutton_easy_to_say.grid(row=3, column=2, ipadx=4, padx=(0, 42))
checkbutton_upper.grid(row=4, column=1, ipadx=5, ipady=5, padx=(38, 0))
checkbutton_numbers.grid(row=4, column=2, ipadx=13, ipady=5, padx=(0, 42))
checkbutton_lower.grid(row=5, column=1, ipadx=5, ipady=5, padx=(38, 0))
checkbutton_symbols.grid(row=5, column=2, ipadx=14, ipady=5, padx=(0, 42))
generated_password.grid(row=6, column=1, columnspan=2, ipadx=10)
generate_password_button.grid(row=7, column=1, padx=(38, 0))
copy_generated_password.grid(row=7, column=2, padx=(0, 44))

scale_size(checkbutton_symbols, 1000)


if __name__ == '__main__':
    window.mainloop()
else:
    raise ImportError('Can\'t import this module')
