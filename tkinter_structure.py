from tkinter import *
from password_generator import generate_password

window = Tk()
window.title('Password Generator')
window.geometry('800x200')


def check_whether_password_len_is_valid(event):
    try:
        int(password_length_entry.get())
        if int(password_length_entry.get()) < 4:
            pass_len_txt.set('4')
            pass_len.set(4)
        elif int(password_length_entry.get()) > 25:
            pass_len_txt.set('25')
            pass_len.set(25)
    except ValueError:
        pass_len_txt.set('4')


def change_entry_len_to_match_slider(event):
    password_length_entry.delete(0, END)
    password_length_entry.insert(0, pass_len.get())


def disable_checkboxes_on_radiobutton():
    checkbutton_numbers.config(state='disabled')
    checkbutton_numbers_var.set(0)
    checkbutton_symbols.config(state='disabled')
    checkbutton_symbols_var.set(0)
    checkbutton_upper_var.set(1)


def activate_checkboxes_on_radiobutton():
    checkbutton_numbers.config(state='active')
    checkbutton_symbols.config(state='active')


def make_1_checkbutton_always_active(checkbutton):
    if checkbutton_upper_var.get() + checkbutton_lower_var.get() + checkbutton_numbers_var.get() + checkbutton_symbols_var.get() == 0:
        if str(checkbutton) == 'PY_VAR3':
            checkbutton.set(1)
        elif str(checkbutton) == 'PY_VAR4':
            checkbutton.set(10)
        elif str(checkbutton) == 'PY_VAR5':
            checkbutton.set(100)
        elif str(checkbutton) == 'PY_VAR6':
            checkbutton.set(1_000)


def collect_data_to_generate_password():
    checkbutton_sum = checkbutton_upper_var.get() + checkbutton_lower_var.get() + checkbutton_numbers_var.get() + checkbutton_symbols_var.get()
    data = {'Password len': pass_len.get(),
            'Radiobutton value': radiobutton_var.get(),
            'Checkbutton value': checkbutton_sum}
    return data


# Vars
pass_len = IntVar()
pass_len.set(4)
pass_len_txt = StringVar()
pass_len_txt.set('4')
radiobutton_var = IntVar()
checkbutton_upper_var = IntVar(value=1)
checkbutton_lower_var = IntVar(value=10)
checkbutton_numbers_var = IntVar(value=100)
checkbutton_symbols_var = IntVar(value=1_000)
left_frame = Frame(master=window)

# Frames
left_subframe_top = Label(master=left_frame, text='Password Length')
left_subframe_bottom = Frame(master=left_frame)
middle_frame = Frame(master=window)
right_frame = Frame(master=window)
bottom_frame = Frame(master=window)
password_length_entry = Entry(master=left_subframe_bottom, textvariable=pass_len_txt)
password_length_scale = Scale(master=left_subframe_bottom, from_=4, to=25, variable=pass_len,
                              orient='horizontal')
radiobutton_easy_to_read = Radiobutton(master=middle_frame, text='Easy to read', variable=radiobutton_var, value=0, command=activate_checkboxes_on_radiobutton)
radiobutton_easy_to_say = Radiobutton(master=middle_frame, text='Easy to say', variable=radiobutton_var, value=1, command=disable_checkboxes_on_radiobutton)
checkbutton_upper = Checkbutton(master=right_frame, text='Uppercase', variable=checkbutton_upper_var, onvalue=1, command=lambda: make_1_checkbutton_always_active(checkbutton_upper_var))
checkbutton_lower = Checkbutton(master=right_frame, text='Lowercase', variable=checkbutton_lower_var, onvalue=10, command=lambda: make_1_checkbutton_always_active(checkbutton_lower_var))
checkbutton_numbers = Checkbutton(master=right_frame, text='Numbers', variable=checkbutton_numbers_var, onvalue=100, command=lambda: make_1_checkbutton_always_active(checkbutton_numbers_var))
checkbutton_symbols = Checkbutton(master=right_frame, text='Symbols', variable=checkbutton_symbols_var, onvalue=1_000, command=lambda: make_1_checkbutton_always_active(checkbutton_symbols_var))
generated_password = Label(master=bottom_frame, text='Your password will be here')

# Binds
# password_length_entry.bind('<KeyRelease>', change_slider_value)
password_length_entry.bind('<KeyRelease>', check_whether_password_len_is_valid)
password_length_scale.bind('<ButtonRelease-1>', change_entry_len_to_match_slider)

# Packing
password_length_entry.pack(side=LEFT)
password_length_scale.pack(side=RIGHT)
middle_frame.pack()
radiobutton_easy_to_read.pack()
radiobutton_easy_to_say.pack()
right_frame.pack(side=RIGHT)
left_frame.pack(side=LEFT)
left_subframe_top.pack()
left_subframe_bottom.pack()
checkbutton_upper.pack()
checkbutton_lower.pack()
checkbutton_numbers.pack()
checkbutton_symbols.pack()
bottom_frame.pack()
generated_password.pack()

window.mainloop()
