from tkinter import *
import logging
import re

root = Tk()
root.title("Pig Latin Translator")
root.configure(background='black')
root.geometry("425x150")


def alpha_to_igpay(alpha_input):
    word_split = re.split("(\W)", alpha_input)
    print(word_split)
    sentence = map(lambda z: z if not re.search('\w', z) else z.lower() + 'ay', word_split)
    return ''.join(sentence)


def callback():
    try:
        user_input = english_entry.get()
        sentence_split = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", user_input)
        final_sentence_list = []
        for sentences in sentence_split:
            print(sentences)
            latin = alpha_to_igpay(sentences).capitalize()
            final_sentence_list.append(latin)
    except TypeError:
        pig_latin_output.configure(text='Wrong type entered error!')

    final_sentence = ' '.join(map(str, final_sentence_list))
    pig_latin_output.configure(text=final_sentence)


def destroy():
    root.destroy()


pig_latin_output = Label(root, text="Enter a phrase to translate.", bg="black", fg="cyan",
                     font="Helvetica 12")

english_entry = Entry(root, bg="white")

translate_button = Button(root, text=" Translate! ", command=callback, bg="seashell3", highlightbackground="black", fg="blue",
                          font="Helvetica 7 bold", underline=1)

exit_button = Button(root, text="Exit", command=root.destroy, bg="seashell3", highlightbackground="black", fg="blue",
                     font="Helvetica 7 bold", underline=0)

pig_latin_output.pack(padx=5, pady=15)
english_entry.pack(padx=5, pady=5)
translate_button.pack(padx=5, pady=5)
exit_button.pack(padx=5, pady=5)

root.bind('<Alt_L><t>', lambda e: callback())
root.bind('<Alt_L><T>', lambda e: callback())
root.bind('<Alt_L><x>', lambda f: destroy())
root.bind('<Alt_L><X>', lambda f: destroy())

root.mainloop()
