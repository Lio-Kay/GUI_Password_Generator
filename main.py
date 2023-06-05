from tkinter import *
from logic_functions import *

# Tk initialization
window = Tk()
window.title('Password Generator')
window.geometry('330x310+100+100')

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
length_frame = Frame(master=window, background='#141414', pady=8)
length_subframe_1 = Frame(master=length_frame)
length_subframe_2 = Frame(master=length_frame)
radiobutton_frame = Frame(master=window, background='#141414')
checkbutton_frame = Frame(master=window, background='#141414')
checkbutton_subframe_1 = Frame(master=checkbutton_frame, background='#141414', border=5)
checkbutton_subframe_2 = Frame(master=checkbutton_frame, background='#141414', border=5)
password_frame = Frame(master=window, background='#141414', border=5)

# Elements
length_label = Label(master=length_frame, text='Password Length', font='Verdana 11 bold', fg='#141414', bg='#0C7489',
                     bd=3, padx=80, relief=FLAT)
password_length_entry = Entry(master=length_subframe_1, textvariable=pass_len_txt, width=13, font='Verdana',
                              justify=CENTER, background='#119DA4', bd=0, relief=FLAT, cursor='arrow',
                              selectborderwidth=0, selectforeground='#141414', selectbackground='white')
password_length_scale = Scale(master=length_subframe_2, from_=4, to=20, variable=pass_len, length=130,
                              highlightthickness=0, orient='horizontal', sliderlength=15, font='Verdana', fg='#141414',
                              background='#119DA4', bd=0, relief=FLAT, sliderrelief=GROOVE, troughcolor='#BAEBEE',
                              cursor='arrow')

radiobutton_easy_to_read = Radiobutton \
    (master=radiobutton_frame, text='Easy to read', variable=radiobutton_var, value=0,
     command=lambda: activate_checkboxes_on_radiobutton
     (checkbutton_numbers, checkbutton_numbers_var, checkbutton_symbols, checkbutton_symbols_var),
     font='Verdana', fg='#141414', activeforeground='white', bg='#0C7489',
     activebackground='#119DA4', borderwidth=4, cursor='arrow')
radiobutton_easy_to_say = Radiobutton \
    (master=radiobutton_frame, text='Easy to say', variable=radiobutton_var, value=1,
     command=lambda: disable_checkboxes_on_radiobutton
     (checkbutton_numbers, checkbutton_numbers_var, checkbutton_symbols, checkbutton_symbols_var),
     font='Verdana', fg='#141414', activeforeground='white', bg='#119DA4', activebackground='#119DA4', borderwidth=4,
     background='#0C7489', cursor='arrow')


    # TODO Fix NameError: name 'checkbutton' is not defined in lambda expr

checkbutton_upper = Checkbutton \
    (master=checkbutton_subframe_1, text='Uppercase', variable=checkbutton_upper_var,
     command=lambda: make_1_checkbutton_active
     (checkbutton_upper_var, checkbutton_lower_var, checkbutton_numbers_var,
      checkbutton_symbols_var, checkbutton),
     font='Verdana', fg='#141414', activeforeground='white', bg='#119DA4', activebackground='#119DA4', borderwidth=4,
     background='#0C7489', cursor='arrow')
checkbutton_lower = Checkbutton \
    (master=checkbutton_subframe_1, text='Lowercase', variable=checkbutton_lower_var, onvalue=10,
     command=lambda: make_1_checkbutton_active
     (checkbutton_upper_var, checkbutton_lower_var, checkbutton_numbers_var, \
      checkbutton_symbols_var, checkbutton),
     font='Verdana', fg='#141414', activeforeground='white', bg='#119DA4', activebackground='#119DA4', borderwidth=4,
     background='#0C7489', cursor='arrow')
checkbutton_numbers = Checkbutton \
    (master=checkbutton_subframe_2, text='Numbers', variable=checkbutton_numbers_var, onvalue=100,
     command=lambda: make_1_checkbutton_active
     (checkbutton_upper_var, checkbutton_lower_var, checkbutton_numbers_var,
      checkbutton_symbols_var, checkbutton),
     font='Verdana', fg='#141414', activeforeground='white', bg='#119DA4',
     activebackground='#119DA4', borderwidth=4, background='#0C7489', cursor='arrow')
checkbutton_symbols = Checkbutton \
    (master=checkbutton_subframe_2, text='Symbols', variable=checkbutton_symbols_var, onvalue=1_000,
     command=lambda: make_1_checkbutton_active
     (checkbutton_upper_var, checkbutton_lower_var, checkbutton_numbers_var,
      checkbutton_symbols_var, checkbutton), font='Verdana', justify=LEFT, padx=3, fg='#141414',
     activeforeground='white', bg='#119DA4', activebackground='#119DA4', borderwidth=4, background='#0C7489',
     cursor='arrow')

generated_password = Label \
    (master=password_frame, textvariable=password_text, font='Verdana 13 bold', width=24, pady=4, fg='#141414',
     bg='#BAEBEE', bd=4, relief=FLAT, highlightthickness=0, highlightbackground='#141414')
generate_password_button = Button \
    (master=password_frame, text='Generate', command=lambda: generate_password
    (checkbutton_upper_var, checkbutton_lower_var, checkbutton_numbers_var, checkbutton_symbols_var,
     radiobutton_var, pass_len, password_text),
     font='Verdana', width=11, fg='#141414', bg='#0C7489', activebackground='#119DA4', activeforeground='white', bd=1,
     relief=FLAT)
copy_generated_password = Button(master=password_frame, text='Copy', font='Verdana', width=10, fg='#141414',
                                 bg='#0C7489', activebackground='#119DA4', activeforeground='white', bd=1, relief=FLAT)

# Binds
password_length_entry.bind('<KeyRelease>',
                           lambda x: check_whether_password_len_is_valid(password_length_entry, pass_len_txt, pass_len))
password_length_scale.bind('<ButtonRelease-1>',
                           lambda x: change_entry_len_to_match_slider(password_length_entry, pass_len))
copy_generated_password.bind('<ButtonRelease-1>', lambda x: copy_on_button(window, password_text))

# Packing
length_frame.pack()
radiobutton_frame.pack(pady=(7, 5))
checkbutton_frame.pack(pady=(0, 5))
checkbutton_subframe_1.pack(side=LEFT)
checkbutton_subframe_2.pack()
password_frame.pack()
length_label.pack()
length_subframe_1.pack(side=LEFT, padx=(16, 8), pady=(8, 0), anchor='n')
length_subframe_2.pack(pady=(8, 0))
password_length_entry.pack()
password_length_scale.pack()
radiobutton_easy_to_read.pack(side=LEFT, padx=(4, 12))
radiobutton_easy_to_say.pack(side=RIGHT, padx=0)
checkbutton_upper.pack(pady=5)
checkbutton_lower.pack()
checkbutton_numbers.pack(pady=5)
checkbutton_symbols.pack()
generated_password.pack(pady=(0, 4))
generate_password_button.pack(side=LEFT, padx=(30, 0))
copy_generated_password.pack(anchor='e', padx=(0, 30))


if __name__ == '__main__':
    window.mainloop()
else:
    raise ImportError('Can\'t import this module')
