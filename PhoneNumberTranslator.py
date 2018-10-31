from tkinter import *
import logging

root = Tk()
root.title("Alphabetic Telephone Number Translator")
root.configure(background='black')
root.geometry("425x150")

phone_letters = {'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3', 'F': "3", 'G': '4', 'H': '4', 'I': '4', 'J': '5',
                 'K': '5', 'L': '5', 'M': '6', 'N': '6', 'O': '6', 'P': '7', 'Q': '7', 'R': '7', 'S': '7', 'T': '8',
                 'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9', 'Z': '9'}


def int_to_alpha(int_input):

    phone_number_result = []

    for numbers in int_input:
        if numbers.isdigit():
            str(phone_number_result.append(numbers))
        if numbers.isalpha():
            value = phone_letters.get(numbers.capitalize())
            phone_number_result.append(value)

    for final_number in phone_number_result:
        return ''.join(map(str, phone_number_result))


def callback():
    try:
        phone_table = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                    '2223334445556667777888999922233344455566677778889999')
        phone_number = phone_number_entry.get().translate(phone_table)

        # phone_number = str(int_to_alpha(phone_number_entry.get()))
    except Exception as nex:
        numberOutput.configure(text='Exception Error!')
        logging.exception("User tried to enter a value that is not present." + nex)
    numberOutput.configure(text=phone_number)


def destroy():
    root.destroy()


numberOutput = Label(root, text="Enter an Alphabetic Phone Number to translate.", bg="black", fg="cyan",
                     font="Helvetica 12")

phone_number_entry = Entry(root, bg="white")

translate_button = Button(root, text=" Translate! ", command=callback, bg="seashell3", highlightbackground="black", fg="blue",
                          font="Helvetica 7 bold", underline=1)

exit_button = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                     font="Helvetica 7 bold", underline=0)

phone_number_entry.pack(padx=5, pady=15)
numberOutput.pack(padx=5, pady=5)
translate_button.pack(padx=5, pady=5)
exit_button.pack(padx=5, pady=5)

root.bind('<Alt_L><t>', lambda e: callback())
root.bind('<Alt_L><T>', lambda e: callback())
root.bind('<Alt_L><x>', lambda f: destroy())
root.bind('<Alt_L><X>', lambda f: destroy())

root.mainloop()
