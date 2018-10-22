import sys
import os
import json
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from requests.exceptions import ConnectionError


root = Tk()
top_frame = Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=2)

middle_frame = Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=2, width=100, height=100, bd= 0)

bottom_frame = Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=2, width=100, height=100, bd= 0)

root.title("Map Tokens to Adam ID's")

root.resizable(False, False)

token_list = []

api_token_test1 = ''
api_token_test2 = ''
api_token_test3 = ''

# token_list.append(api_token_test1)
# token_list.append(api_token_test2)
# token_list.append(api_token_test3)

adam_id_list = []

adam_id1 = "524297631"
adam_id2 = "1246284741"
adam_id3 = "586542460"
adam_id4 = "360593530"

# adam_id_list.append(adam_id1)
# adam_id_list.append(adam_id2)
# adam_id_list.append(adam_id3)
# adam_id_list.append(adam_id4)


def get_adam_id_filename(entry):
    file_name = entry.get()
    if not os.access(file_name, os.W_OK):
        file_name = filedialog.askopenfilename()
        entry.delete(0, END)
        entry.insert(0, file_name)
        return file_name
    else:
        return file_name


def get_token_filename(scroll):
    file_name = scroll.get('1.0', END)
    if not os.access(file_name, os.W_OK):
        file_name = filedialog.askopenfilename()
        scroll.insert('1.0', file_name)
        return file_name
    else:
        return file_name


def save_filename(entry):
    file_name = entry.get()
    if not os.access(file_name, os.W_OK):
        file_name = filedialog.asksaveasfile().name
        entry.delete(0, END)
        entry.insert(0, file_name)
        return file_name
    else:
        return file_name


def append_token_list(token_in, scroll):
    token_list.append(token_in)
    scroll.delete('1.0', END)


def append_adam_id_list(adam_id_in, entry):
    adam_id_list.append(adam_id_in)
    entry.delete


def clear_list(list_to_clear, label):
    label.configure(text="Cleared list.\n")
    del list_to_clear[:]


def get_count_info(token_in, adam_id_in):
    try:
        api_url = 'https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/getVPPAssetsSrv?sToken=' + token_in + \
              '&includeLicenseCounts=' + adam_id_in
        response = requests.get(api_url)
        json_response = response.json()
        if response.status_code == 200:
            for all_assets in range(len(json_response['assets'])):
                adam_id_search = json_response['assets'][all_assets]['adamIdStr']
                if adam_id_search == adam_id_in:
                    total_count = json_response['assets'][all_assets]['totalCount']
                    return total_count
                else:
                    return None
        else:
            messagebox.showerror("Error Connecting", "There was an error connecting to the iTunes URL.\n "
                                                     "Please check your internet connection.")
    except ConnectionError:
        messagebox.showerror("Error Connecting", "There was an error connecting to the iTunes URL.\n Please check your"
                                                 "internet connection.")


def destroy():
    root.destroy()


adamIdEntryLabel = Label(top_frame, text="Please enter adam ids or the file path to a file with adam ids to add.",
                         fg="black", font="Helvetica 12 bold", wraplength=300)

adamIdEntry = Entry(top_frame, width=35)

adamIdListButton = Button(top_frame, text="Add to Adam ID List", command=root.destroy, bg="seashell3", highlightbackground="black",
                          fg="black", font="Helvetica 7 bold", underline=1)

adamIdFilepathButton = Button(top_frame, text="Set path to Adam ID file", command=lambda: get_adam_id_filename(adamIdEntry), bg="seashell3",
                              highlightbackground="black", fg="black", font="Helvetica 7 bold", underline=1)

clearAdamIDListButton = Button(top_frame, text="Clear Adam ID list", command=lambda: clear_list(adam_id_list, adamIdEntryLabel), bg="seashell3",
                               highlightbackground="black", fg="black", font="Helvetica 7 bold", underline=1)


tokenEntryLabel = Label(middle_frame, text="Paste the tokens in here or set the filepath for a token to add. ",
                        fg="black", font="Helvetica 12 bold", wraplength=300)

tokenBox = ScrolledText(middle_frame, width=25, height=15)

addToTokenListButton = Button(middle_frame, text="Add to Token List", command=root.destroy, bg="seashell3", highlightbackground="black",
                              fg="black", font="Helvetica 7 bold", underline=1)

setTokenFilepathButton = Button(middle_frame, text="Set Path to VPP token",
                                command=lambda: get_token_filename(tokenBox), bg="seashell3",
                                highlightbackground="black", fg="black", font="Helvetica 7 bold", underline=1)

clearTokenListButton = Button(middle_frame, text="Clear Token list", command=lambda: clear_list(token_list, tokenEntryLabel), bg="seashell3",
                              highlightbackground="black", fg="black", font="Helvetica 7 bold", underline=1)


outputFileNameEntryLabel = Label(bottom_frame, text="Enter the path desired for the file output or use the button to fill in"
                                                    " the path.", fg="black", font="Helvetica 12 bold",
                                 wraplength=300)

outputFileName = Entry(bottom_frame, width=35)

buildListButton = Button(bottom_frame, text="Build the list", command=get_count_info, bg="seashell3", highlightbackground="black",
                         fg="black", font="Helvetica 7 bold", underline=1)

setFilepathButton = Button(bottom_frame, text="Set output file name", command=lambda: save_filename(outputFileName),
                            bg="seashell3", highlightbackground="black", fg="black",
                           font="Helvetica 7 bold", underline=0)

exitButton = Button(bottom_frame, text=" Exit Program ", command=root.destroy, bg="seashell3", highlightbackground="black", fg="black",
                    font="Helvetica 7 bold", underline=1)

top_frame.pack(padx=5, pady=5, fill="both", expand="yes")
adamIdEntryLabel.pack(padx=5, pady=5)
adamIdEntry.pack(padx=5, pady=5)
adamIdListButton.pack(side=LEFT, padx=5, pady=5)
clearAdamIDListButton.pack(side=LEFT, padx=5, pady=5)
adamIdFilepathButton.pack(side=LEFT, padx=5, pady=5)

middle_frame.pack(padx=5, pady=5, fill="both", expand="yes")
tokenEntryLabel.pack(padx=5, pady=5)
tokenBox.pack(padx=5, pady=5)
addToTokenListButton.pack(side=LEFT, padx=5, pady=5)
clearTokenListButton.pack(side=LEFT, padx=25, pady=5)
setTokenFilepathButton.pack(side=LEFT, padx=5, pady=5)

bottom_frame.pack(padx=5, pady=5,  fill="both")
outputFileNameEntryLabel.pack(padx=5, pady=5)
outputFileName.pack(padx=5, pady=5)
buildListButton.pack(side=LEFT, padx=5, pady=5)
setFilepathButton.pack(side=LEFT, padx=35, pady=5)
exitButton.pack(side=LEFT, padx=5, pady=5)
# adamIdEntryLabel.grid(row=0, column=2, columnspan=3, padx=5, pady=5)
# adamIdEntry.grid(row=1, column=2, columnspan=3, padx=5, pady=5)
# adamIdListButton.grid(row=2, column=2, columnspan=1, pady=5, sticky=W)
# clearAdamIDListButton.grid(row=2, column=2, columnspan=2, pady=5)
# adamIdFilepathButton.grid(row=2, column=3, columnspan=3, padx=5, pady=5, sticky=W)
#
#
# tokenEntryLabel.grid(row=3, column=2, columnspan=3, padx=5, pady=5)
# tokenBox.grid(row=4, padx=5, column=2, columnspan=3, pady=5)
# addToTokenListButton.grid(row=5,  column=2, columnspan=1, pady=5, sticky=W)
# clearTokenListButton.grid(row=5, column=2, columnspan=2, pady=5)
# setTokenFilepathButton.grid(row=5, column=3, columnspan=3, padx=5, pady=5, sticky=W)
#
# outputFileNameEntryLabel.grid(row=6,  column=2, columnspan=3, padx=5, pady=5)
# outputFileName.grid(row=7,  column=2, columnspan=3, pady=5)
# buildListButton.grid(row=8, column=1, columnspan=1, pady=5, sticky=W)
# setFilepathButton.grid(row=8, column=2, pady=5)
# exitButton.grid(row=8, column=3, columnspan=3, padx=5, pady=5, sticky=E)


for token in range(len(token_list)):
    print(f"Token: {token + 1}")
    for adam_id in range(len(adam_id_list)):
        print(adam_id_list[adam_id])
        print(get_count_info(token_list[token], adam_id_list[adam_id]))

root.bind('<Alt_L><A>', lambda e: append_token_list())
root.bind('<Alt_L><a>', lambda e: append_token_list())
root.bind('<Alt_L><G>', lambda f: get_count_info())
root.bind('<Alt_L><g>', lambda f: get_count_info())
root.bind('<Alt_L><X>', lambda g: destroy())
root.bind('<Alt_L><x>', lambda g: destroy())

root.mainloop()
