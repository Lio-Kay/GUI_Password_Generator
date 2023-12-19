from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from screeninfo import get_monitors

from logic_functions import (generate_password, get_easy_to_read_table_set,
                             get_easy_to_say_table_set,
                             check_whether_password_len_is_valid,
                             change_entry_len_to_match_slider,
                             activate_checkboxes_on_radiobutton,
                             disable_checkboxes_on_radiobutton,
                             make_1_checkbutton_active,
                             copy_on_button)


# Tk initialization
window = Tk()
window.title('Password Generator')
width = 1920
height = 1080
for monitor in get_monitors():
    if monitor.is_primary:
        width = monitor.width
        height = monitor.height

# Grid
window.geometry(f'{round(width * 0.2)}x{round(height * 0.35)}+'
                f'{round(width * 0.1)}+{round(height * 0.1)}')
for r in range(9): window.rowconfigure(index=r, weight=1)
for c in range(4): window.columnconfigure(index=c, weight=1)
window.minsize(round(width * 0.2), round(height * 0.35))

# Style
style = ttk.Style('darkly')
style.configure('.', font=('Helvetica', 14), justify=CENTER)

# Vars
pass_len = IntVar(value=10)
pass_len_txt = StringVar(value='10')
radiobutton_var = IntVar()
checkbutton_upper_var = IntVar(value=1)
checkbutton_lower_var = IntVar(value=10)
checkbutton_numbers_var = IntVar(value=100)
checkbutton_symbols_var = IntVar(value=1_000)
password_text = StringVar(value='Your password will be here')

# Frames
window.configure(background='#141414', cursor='left_ptr')

length_label = ttk.Label(master=window, text='Password Length',
                         style='success', font=('Helvetica', 14, 'bold'), anchor=CENTER)
password_length_entry = ttk.Entry(master=window, textvariable=pass_len_txt, width=11,
                                  justify=CENTER, cursor='arrow', style='dark')
password_length_scale = ttk.Scale(master=window, from_=4, to=20, variable=pass_len,
                                  cursor='hand2', style='success')

radiobutton_easy_to_read = ttk.Radiobutton\
    (master=window, text='Easy to read', variable=radiobutton_var, value=0,
     command=lambda: activate_checkboxes_on_radiobutton
     (checkbutton_numbers, checkbutton_numbers_var, checkbutton_symbols, checkbutton_symbols_var),
     cursor='arrow', style='success-toolbutton')
radiobutton_easy_to_say = ttk.Radiobutton\
    (master=window, text='Easy to say', variable=radiobutton_var, value=1,
     command=lambda: disable_checkboxes_on_radiobutton
     (checkbutton_numbers, checkbutton_numbers_var, checkbutton_symbols, checkbutton_symbols_var),
     cursor='arrow', style='success-toolbutton')

checkbutton_upper = ttk.Checkbutton \
    (master=window, text='Uppercase', variable=checkbutton_upper_var,
     command=lambda: make_1_checkbutton_active
     (checkbutton_upper_var, checkbutton_lower_var, checkbutton_numbers_var,
      checkbutton_symbols_var, checkbutton), cursor='arrow', style='success-square-toggle')
checkbutton_lower = ttk.Checkbutton \
    (master=window, text='Lowercase', variable=checkbutton_lower_var, onvalue=10,
     command=lambda: make_1_checkbutton_active
     (checkbutton_upper_var, checkbutton_lower_var, checkbutton_numbers_var,
      checkbutton_symbols_var, checkbutton), cursor='arrow', style='success-square-toggle')
checkbutton_numbers = ttk.Checkbutton \
    (master=window, text='Numbers', variable=checkbutton_numbers_var, onvalue=100,
     command=lambda: make_1_checkbutton_active
     (checkbutton_upper_var, checkbutton_lower_var, checkbutton_numbers_var,
      checkbutton_symbols_var, checkbutton), cursor='arrow', style='success-square-toggle')
checkbutton_symbols = ttk.Checkbutton \
    (master=window, text='Symbols', variable=checkbutton_symbols_var, onvalue=1_000,
     command=lambda: make_1_checkbutton_active
     (checkbutton_upper_var, checkbutton_lower_var, checkbutton_numbers_var,
      checkbutton_symbols_var, checkbutton), cursor='arrow', style='success-square-toggle')

generated_password = ttk.Label(master=window, textvariable=password_text,
                               style='light', anchor=CENTER, font=('Helvetica', 13))
generate_password_button = ttk.Button \
    (master=window, text='Generate', command=lambda: generate_password
    (checkbutton_upper_var, checkbutton_lower_var, checkbutton_numbers_var,
     checkbutton_symbols_var, radiobutton_var, pass_len, password_text),
     width=10, padding=8, cursor='arrow', style='success-outline')
copy_generated_password = ttk.Button(master=window, text='Copy', width=10, padding=8,
                                     cursor='arrow', style='success-outline')

# Binds
password_length_entry.bind('<KeyRelease>',
                           lambda x: check_whether_password_len_is_valid
                           (password_length_entry, pass_len_txt, pass_len))
password_length_scale.bind('<ButtonRelease-1>',
                           lambda x: change_entry_len_to_match_slider
                           (password_length_entry, pass_len))
copy_generated_password.bind('<ButtonRelease-1>',
                             lambda x: copy_on_button
                             (window, password_text))

# Packing
length_label.grid(row=1, column=1,
                  columnspan=2, ipadx=56, ipady=5)
password_length_entry.grid(row=2, column=1,
                           pady=0, padx=(38, 0))
password_length_scale.grid(row=2, column=2,
                           padx=(0, 42))
radiobutton_easy_to_read.grid(row=3, column=1,
                              padx=(38, 0))
radiobutton_easy_to_say.grid(row=3, column=2,
                             ipadx=4, padx=(0, 42))
checkbutton_upper.grid(row=4, column=1,
                       ipadx=5, ipady=5, padx=(38, 0))
checkbutton_numbers.grid(row=4, column=2,
                         ipadx=13, ipady=5, padx=(0, 42))
checkbutton_lower.grid(row=5, column=1,
                       ipadx=5, ipady=5, padx=(38, 0))
checkbutton_symbols.grid(row=5, column=2,
                         ipadx=14, ipady=5, padx=(0, 42))
generated_password.grid(row=6, column=1,
                        columnspan=2, padx=(44, 48), sticky="nsew")
generate_password_button.grid(row=7,
                              column=1, padx=(38, 0))
copy_generated_password.grid(row=7, column=2,
                             padx=(0, 44))

if __name__ == '__main__':
    window.mainloop()
else:
    raise ImportError('Can\'t import this module')
