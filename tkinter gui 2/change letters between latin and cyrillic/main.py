import tkinter as tk
from tkinter import messagebox
from transliterate import to_latin, to_cyrillic


def to_version_func():
    text = text_entry.get()
    if len(text) == 0:
        messagebox.showwarning('warming', 'enter words to convert!')
    else:
        text_version = to_version.get()

        if text_version == 'to latin':
            res = to_latin(text)
        else:
            res = to_cyrillic(text)
        list_box.insert(tk.END, res)
        text_entry.delete(0, tk.END)


window = tk.Tk()
window.title('Latin and Kiril')
window.geometry('500x350')
version = {'L': 'to latin', 'K': 'to kiril'}

# Text entry in list box
list_box_label = tk.Label(window, text='enter words')
list_box_label.pack()
list_box = tk.Listbox(window)
text_entry = tk.Entry(window)
text_entry.pack()

list_box.pack()

# Version radio button

version_button = tk.Radiobutton(window)
to_version = tk.StringVar()
version_label = tk.Label(window)
version_label.pack()
latin_radio_button = tk.Radiobutton(window, text=version.get("L"), value='to latin', variable=to_version)
latin_radio_button.pack()
kiril_radio_button = tk.Radiobutton(window, text=version.get("K"), value='to kiril', variable=to_version)
kiril_radio_button.pack()

# To version button
to_version_button = tk.Button(window, text='To convert', command=to_version_func)
to_version_button.pack()

if __name__ == '__main__':
    window.mainloop()
