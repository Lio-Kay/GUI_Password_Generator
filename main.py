from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from secrets import choice
from screeninfo import get_monitors
import logging
import string


class Main_window(Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.wm_title('Password Generator')
        width = 1920
        height = 1080
        for monitor in get_monitors():
            if monitor.is_primary:
                width = monitor.width
                height = monitor.height
        self.wm_geometry(f'{round(width*0.2)}x{round(height * 0.35)}+{round(width * 0.1)}+{round(height * 0.1)}')
        for r in range(9): self.rowconfigure(index=r, weight=1)
        for c in range(4): self.columnconfigure(index=c, weight=1)
        self.wm_minsize(round(width*0.2), round(height * 0.35))

        self.style = ttk.Style('darkly')
        self.style.configure('.', font=('Helvetica', 14), justify=CENTER)

        self.set_vars()
        self.

        self.configure(background='#141414', cursor='left_ptr')


class Variables(Tk):


    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.set_vars()

    def set_vars(self):
        self.pass_len = IntVar(value=10)
        self.pass_len_txt = StringVar(value='10')
        self.radiobutton_var = IntVar()
        self.checkbutton_upper_var = IntVar(value=1)
        self.checkbutton_lower_var = IntVar(value=10)
        self.checkbutton_numbers_var = IntVar(value=100)
        self.checkbutton_symbols_var = IntVar(value=1_000)
        self.password_text = StringVar(value='Your password will be here')


class Frames(Main_window):



class Elements(Main_window):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.length_label = ttk.Label(master=self, text='Password Length',
                                 style='success', font=('Helvetica', 14, 'bold'), anchor=CENTER)
        self.password_length_entry = ttk.Entry(master=self, textvariable=self.pass_len_txt, width=11,
                                          justify=CENTER, cursor='arrow', style='dark')
        self.password_length_scale = ttk.Scale(master=self, from_=4, to=20, variable=self.pass_len,
                                          cursor='hand2', style='success')

        self.radiobutton_easy_to_read = ttk.Radiobutton(master=self, text='Easy to read', variable=self.radiobutton_var,
                                                   value=0, command=activate_checkboxes_on_radiobutton,
                                                   cursor='arrow', style='success-toolbutton')
        self.radiobutton_easy_to_say = ttk.Radiobutton(master=self, text='Easy to say', variable=self.radiobutton_var,
                                                  value=1, command=disable_checkboxes_on_radiobutton,
                                                  cursor='arrow', style='success-toolbutton')

        self.checkbutton_upper = ttk.Checkbutton(master=self, text='Uppercase', variable=self.checkbutton_upper_var,
                                            command=lambda: make_1_checkbutton_active(self.checkbutton_upper_var),
                                            cursor='arrow', style='success-square-toggle')
        self.checkbutton_lower = ttk.Checkbutton(master=self, text='Lowercase', variable=self.checkbutton_lower_var,
                                            onvalue=10,
                                            command=lambda: make_1_checkbutton_active(self.checkbutton_lower_var),
                                            cursor='arrow', style='success-square-toggle')
        self.checkbutton_numbers = ttk.Checkbutton(master=self, text='Numbers', variable=self.checkbutton_numbers_var,
                                              onvalue=100,
                                              command=lambda: make_1_checkbutton_active(self.checkbutton_numbers_var),
                                              cursor='arrow', style='success-square-toggle')
        self.checkbutton_symbols = ttk.Checkbutton(master=self, text='Symbols', variable=self.checkbutton_symbols_var,
                                              onvalue=1_000,
                                              command=lambda: make_1_checkbutton_active(self.checkbutton_symbols_var),
                                              cursor='arrow', style='success-square-toggle')

        self.generated_password = ttk.Label(master=self, textvariable=self.password_text,
                                       style='light', anchor=CENTER, font=('Helvetica', 13))
        self.generate_password_button = ttk.Button(master=self, text='Generate', command=generate_password, width=10,
                                              padding=8,
                                              cursor='arrow', style='success-outline')
        self.copy_generated_password = ttk.Button(master=self, text='Copy', width=10, padding=8,
                                             cursor='arrow', style='success-outline')

        self.length_label.grid(row=1, column=1, columnspan=2, ipadx=56, ipady=5)
        self.password_length_entry.grid(row=2, column=1, pady=0, padx=(38, 0))
        self.password_length_scale.grid(row=2, column=2, padx=(0, 42))
        self.radiobutton_easy_to_read.grid(row=3, column=1, padx=(38, 0))
        self.radiobutton_easy_to_say.grid(row=3, column=2, ipadx=4, padx=(0, 42))
        self.checkbutton_upper.grid(row=4, column=1, ipadx=5, ipady=5, padx=(38, 0))
        self.checkbutton_numbers.grid(row=4, column=2, ipadx=13, ipady=5, padx=(0, 42))
        self.checkbutton_lower.grid(row=5, column=1, ipadx=5, ipady=5, padx=(38, 0))
        self.checkbutton_symbols.grid(row=5, column=2, ipadx=14, ipady=5, padx=(0, 42))
        self.generated_password.grid(row=6, column=1, columnspan=2, padx=(44, 48), sticky="nsew")
        self.generate_password_button.grid(row=7, column=1, padx=(38, 0))
        self.copy_generated_password.grid(row=7, column=2, padx=(0, 44))


class Functions(Main_window, Elements):

    def __init__(self):
        super().__init__()

    def generate_password(self) -> None:
        """
        Основная функция, генерирует пароль основываясь на 1 slider, 2 radio buttons и 4 check buttons
        :return: Выводит результат генерации на GUI по нажатию кнопки generate_password_button
        """
        checkbutton_sum = self.checkbutton_upper_var.get() + self.checkbutton_lower_var.get() + self.checkbutton_numbers_var.get() + \
                          self.checkbutton_symbols_var.get()
        if self.radiobutton_var.get() == 0:
            character_list = self.get_easy_to_read_table_set(checkbutton_sum)
        elif self.radiobutton_var.get() == 1:
            character_list = self.get_easy_to_say_table_set(checkbutton_sum)
        password = []
        for symbol in range(self.pass_len.get()):
            password.append(choice(character_list))
        password = ''.join(password)
        self.password_text.set(password)

    def get_easy_to_read_table_set(self, value: int) -> str:
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

    def get_easy_to_say_table_set(self, value: int) -> str:
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
    def check_whether_password_len_is_valid(self, event=None) -> None:
        """
        Проверяет длину пароля в Entry и не позволяет сделать его вне установленного диапазона
        :param event: Затычка для bind
        """
        try:
            int(self.password_length_entry.get())
            if int(self.password_length_entry.get()) < 4:
                self.pass_len_txt.set('4')
                self.pass_len.set(4)
            elif int(self.password_length_entry.get()) > 20:
                self.pass_len_txt.set('20')
                self.pass_len.set(20)
        except ValueError:
            self.pass_len_txt.set('4')

    def change_entry_len_to_match_slider(self, event=None) -> None:
        """
        Изменяет значение в Entry на значение выбранное в Slider
        :param event: Затычка для bind
        """
        self.password_length_entry.delete(0, END)
        self.password_length_entry.insert(0, self.pass_len.get())

    def activate_checkboxes_on_radiobutton() -> None:
        """
        Делает активными 2 checkbox при нажатии кнопки 'Easy to read'
        """
        checkbutton_numbers.config(state='active')
        checkbutton_numbers_var.set(100)
        checkbutton_symbols.config(state='active')
        checkbutton_symbols_var.set(1_000)

    def disable_checkboxes_on_radiobutton() -> None:
        """
        Делает неактивными 2 checkbox при нажатии кнопки 'Easy to say'
        """
        checkbutton_numbers.config(state='disabled')
        checkbutton_numbers_var.set(0)
        checkbutton_symbols.config(state='disabled')
        checkbutton_symbols_var.set(0)
        checkbutton_upper_var.set(1)

    def make_1_checkbutton_active(checkbutton: object) -> None:
        """
        Проверяет состояние всех checkbox и если остался только один, не даёт его выключить
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

    def copy_on_button(event=None) -> None:
        """
        Копирует значение Label 'generated_password' по нажатию кнопки 'Copy'
        :param event: Затычка для bind
        """
        window.clipboard_clear()
        window.clipboard_append(password_text.get())

    self.password_length_entry.bind('<KeyRelease>', check_whether_password_len_is_valid)
    self.password_length_scale.bind('<ButtonRelease-1>', change_entry_len_to_match_slider)
    self.copy_generated_password.bind('<ButtonRelease-1>', copy_on_button)




# from tkinter import *
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
# from secrets import choice
# from screeninfo import get_monitors
# import logging
# import string
#
#
# def generate_password() -> None:
#     """
#     Основная функция, генерирует пароль основываясь на 1 slider, 2 radio buttons и 4 check buttons
#     :return: Выводит результат генерации на GUI по нажатию кнопки generate_password_button
#     """
#     checkbutton_sum = checkbutton_upper_var.get() + checkbutton_lower_var.get() + checkbutton_numbers_var.get() + \
#                       checkbutton_symbols_var.get()
#     if radiobutton_var.get() == 0:
#         character_list = get_easy_to_read_table_set(checkbutton_sum)
#     elif radiobutton_var.get() == 1:
#         character_list = get_easy_to_say_table_set(checkbutton_sum)
#     password = []
#     for symbol in range(pass_len.get()):
#         password.append(choice(character_list))
#     password = ''.join(password)
#     password_text.set(password)
#
#
# def get_easy_to_read_table_set(value: int) -> str:
#     """
#     Создает кастомный набор легкоразличимых символов
#     :param value: Сумма 4 check buttons для получения всех комбинаций
#     :return: Одна из 15 комбинаций символов для генерации пароля
#     """
#     character_list = ''
#     upper = 'ABCDEFGHJKMNPQRSTUVXYZ'
#     lower = 'abcdefghjkmnpqrstuvxyz'
#     numbers = '23456789'
#     symbols = '!"#$%&\'()*+,-./:;<=>?@[\]_{}~'
#     match value:
#         case 1:
#             character_list = upper
#         case 10:
#             character_list = lower
#         case 11:
#             character_list = upper+lower
#         case 100:
#             character_list = numbers
#         case 101:
#             character_list = upper+numbers
#         case 110:
#             character_list = lower+numbers
#         case 111:
#             character_list = upper+lower+numbers
#         case 1_000:
#             character_list = symbols
#         case 1_001:
#             character_list = upper+symbols
#         case 1_010:
#             character_list = lower+symbols
#         case 1_011:
#             character_list = upper+lower+symbols
#         case 1_100:
#             character_list = numbers+symbols
#         case 1_101:
#             character_list = upper+numbers+symbols
#         case 1_110:
#             character_list = lower+numbers+symbols
#         case 1_111:
#             character_list = upper+lower+numbers+symbols
#     return character_list
#
#
# def get_easy_to_say_table_set(value: int) -> str:
#     """
#     Создает набор из заглавных и строчных букв
#     :param value: Сумма 2 checkbuttons для получения всех комбинаций
#     :return: Одна из 3 кобинаций символов для генерации пароля
#     """
#     character_list = ''
#     if value == 1:
#         character_list += string.ascii_uppercase
#     elif value == 10:
#         character_list += string.ascii_lowercase
#     elif value == 11:
#         character_list += string.ascii_letters
#     return character_list
#
#
# # Скрипты элементов tkinter
# def check_whether_password_len_is_valid(event=None) -> None:
#     """
#     Проверяет длину пароля в Entry и не позволяет сделать его вне установленного диапазона
#     :param event: Затычка для bind
#     """
#     try:
#         int(password_length_entry.get())
#         if int(password_length_entry.get()) < 4:
#             pass_len_txt.set('4')
#             pass_len.set(4)
#         elif int(password_length_entry.get()) > 20:
#             pass_len_txt.set('20')
#             pass_len.set(20)
#     except ValueError:
#         pass_len_txt.set('4')
#
#
# def change_entry_len_to_match_slider(event=None) -> None:
#     """
#     Изменяет значение в Entry на значение выбранное в Slider
#     :param event: Затычка для bind
#     """
#     password_length_entry.delete(0, END)
#     password_length_entry.insert(0, pass_len.get())
#
#
# def activate_checkboxes_on_radiobutton() -> None:
#     """
#     Делает активными 2 checkbox при нажатии кнопки 'Easy to read'
#     """
#     checkbutton_numbers.config(state='active')
#     checkbutton_numbers_var.set(100)
#     checkbutton_symbols.config(state='active')
#     checkbutton_symbols_var.set(1_000)
#
#
# def disable_checkboxes_on_radiobutton() -> None:
#     """
#     Делает неактивными 2 checkbox при нажатии кнопки 'Easy to say'
#     """
#     checkbutton_numbers.config(state='disabled')
#     checkbutton_numbers_var.set(0)
#     checkbutton_symbols.config(state='disabled')
#     checkbutton_symbols_var.set(0)
#     checkbutton_upper_var.set(1)
#
#
# def make_1_checkbutton_active(checkbutton: object) -> None:
#     """
#     Проверяет состояние всех checkbox и если остался только один, не даёт его выключить
#     """
#     checkbutton_sum = checkbutton_upper_var.get() + checkbutton_lower_var.get() + checkbutton_numbers_var.get() +\
#                       checkbutton_symbols_var.get()
#     if checkbutton_sum == 0:
#         match str(checkbutton):
#             case 'PY_VAR3': checkbutton.set(1)
#             case 'PY_VAR4': checkbutton.set(10)
#             case 'PY_VAR5': checkbutton.set(100)
#             case 'PY_VAR6': checkbutton.set(1_000)
#
#
# def copy_on_button(event=None) -> None:
#     """
#     Копирует значение Label 'generated_password' по нажатию кнопки 'Copy'
#     :param event: Затычка для bind
#     """
#     window.clipboard_clear()
#     window.clipboard_append(password_text.get())
#
#
# # Tk initialization
# window = Tk()
# window.title('Password Generator')
# width = 1920
# height = 1080
# for monitor in get_monitors():
#     if monitor.is_primary:
#         width = monitor.width
#         height = monitor.height
#
# window.geometry(f'{round(width*0.2)}x{round(height * 0.35)}+{round(width * 0.1)}+{round(height * 0.1)}')
# for r in range(9): window.rowconfigure(index=r, weight=1)
# for c in range(4): window.columnconfigure(index=c, weight=1)
# window.minsize(round(width*0.2), round(height * 0.35))
#
# # Style
# style = ttk.Style('darkly')
# style.configure('.', font=('Helvetica', 14), justify=CENTER)
#
# # Vars
# pass_len = IntVar(value=10)
# pass_len_txt = StringVar(value='10')
# radiobutton_var = IntVar()
# checkbutton_upper_var = IntVar(value=1)
# checkbutton_lower_var = IntVar(value=10)
# checkbutton_numbers_var = IntVar(value=100)
# checkbutton_symbols_var = IntVar(value=1_000)
# password_text = StringVar(value='Your password will be here')
#
# # Frames
# window.configure(background='#141414', cursor='left_ptr')
#
# length_label = ttk.Label(master=window, text='Password Length',
#                          style='success', font=('Helvetica', 14, 'bold'), anchor=CENTER)
# password_length_entry = ttk.Entry(master=window, textvariable=pass_len_txt, width=11,
#                                   justify=CENTER, cursor='arrow', style='dark')
# password_length_scale = ttk.Scale(master=window, from_=4, to=20, variable=pass_len,
#                                   cursor='hand2', style='success')
#
# radiobutton_easy_to_read = ttk.Radiobutton(master=window, text='Easy to read', variable=radiobutton_var,
#                                            value=0, command=activate_checkboxes_on_radiobutton,
#                                            cursor='arrow', style='success-toolbutton')
# radiobutton_easy_to_say = ttk.Radiobutton(master=window, text='Easy to say', variable=radiobutton_var,
#                                           value=1, command=disable_checkboxes_on_radiobutton,
#                                           cursor='arrow', style='success-toolbutton')
#
# checkbutton_upper = ttk.Checkbutton(master=window, text='Uppercase', variable=checkbutton_upper_var,
#                                     command=lambda: make_1_checkbutton_active(checkbutton_upper_var),
#                                     cursor='arrow', style='success-square-toggle')
# checkbutton_lower = ttk.Checkbutton(master=window, text='Lowercase', variable=checkbutton_lower_var,
#                                     onvalue=10, command=lambda: make_1_checkbutton_active(checkbutton_lower_var),
#                                     cursor='arrow', style='success-square-toggle')
# checkbutton_numbers = ttk.Checkbutton(master=window, text='Numbers', variable=checkbutton_numbers_var,
#                                       onvalue=100, command=lambda: make_1_checkbutton_active(checkbutton_numbers_var),
#                                       cursor='arrow', style='success-square-toggle')
# checkbutton_symbols = ttk.Checkbutton(master=window, text='Symbols', variable=checkbutton_symbols_var,
#                                       onvalue=1_000, command=lambda: make_1_checkbutton_active(checkbutton_symbols_var),
#                                       cursor='arrow', style='success-square-toggle')
#
# generated_password = ttk.Label(master=window, textvariable=password_text,
#                                style='light', anchor=CENTER, font=('Helvetica', 13))
# generate_password_button = ttk.Button(master=window, text='Generate', command=generate_password, width=10, padding=8,
#                                       cursor='arrow', style='success-outline')
# copy_generated_password = ttk.Button(master=window, text='Copy', width=10, padding=8,
#                                      cursor='arrow', style='success-outline')
#
#
# # Binds
# password_length_entry.bind('<KeyRelease>', check_whether_password_len_is_valid)
# password_length_scale.bind('<ButtonRelease-1>', change_entry_len_to_match_slider)
# copy_generated_password.bind('<ButtonRelease-1>', copy_on_button)
#
#
# # Packing
# length_label.grid(row=1, column=1, columnspan=2, ipadx=56, ipady=5)
# password_length_entry.grid(row=2, column=1, pady=0, padx=(38, 0))
# password_length_scale.grid(row=2, column=2, padx=(0, 42))
# radiobutton_easy_to_read.grid(row=3, column=1, padx=(38, 0))
# radiobutton_easy_to_say.grid(row=3, column=2, ipadx=4, padx=(0, 42))
# checkbutton_upper.grid(row=4, column=1, ipadx=5, ipady=5, padx=(38, 0))
# checkbutton_numbers.grid(row=4, column=2, ipadx=13, ipady=5, padx=(0, 42))
# checkbutton_lower.grid(row=5, column=1, ipadx=5, ipady=5, padx=(38, 0))
# checkbutton_symbols.grid(row=5, column=2, ipadx=14, ipady=5, padx=(0, 42))
# generated_password.grid(row=6, column=1, columnspan=2, padx=(44, 48), sticky="nsew")
# generate_password_button.grid(row=7, column=1, padx=(38, 0))
# copy_generated_password.grid(row=7, column=2, padx=(0, 44))
#
#
# if __name__ == '__main__':
#     window.mainloop()
# else:
#     raise ImportError('Can\'t import this module')
