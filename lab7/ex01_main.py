from tkinter import *
from tkinter import scrolledtext
from ex00_note import Note

def list_text(fr: Frame) -> None:
	for widget in fr.winfo_children():
		widget.destroy()
	txt = scrolledtext.ScrolledText(fr)
	txt.insert(INSERT, " ".join(text))	
	txt.place( relwidth=1, relheight=0.9)
	save_button = Button(fr, text='Save text', command=lambda: save_text(fr, text))
	save_button.place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.1)

def save_text(fr: Frame, text) -> None:
	temp = fr.winfo_children()[0]
	res = temp.winfo_children()[1].get(1.0, END).split(' ')
	text.clear()
	for word in res:
		text.append(word)

def add():
	pass

def add_descr(fr: Frame) -> None:
	for widget in fr.winfo_children():
		widget.destroy()

	word = Entry(fr)
	word.insert(0, 'Слово')
	word.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.1)

	txt = scrolledtext.ScrolledText(fr)
	txt.insert(INSERT, "Описание")
	txt.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

	save_button = Button(fr, text='Save description', command=lambda: save_descr(fr))
	save_button.place(relx=0.3, rely=0.9, relwidth=0.4, relheight=0.1)

def save_descr(fr):
	word = fr.winfo_children()[0].get()
	temp = fr.winfo_children()[1]
	d = temp.winfo_children()[1].get(1.0, END)

	for widget in fr.winfo_children():
		widget.destroy()
	descr[word] = d
	list_text(fr)

def search_word(fr: Frame) -> None:
	for widget in fr.winfo_children():
		widget.destroy()

	word = Entry(fr)
	word.insert(0, 'Слово')
	word.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.1)

	search_button = Button(fr, text='Search', command=lambda: search(fr))
	search_button.place(relx=0.1, rely=0.3, relwidth=0.4, relheight=0.1)

def search(fr: Frame) -> None:
	word = fr.winfo_children()[0].get()

	for widget in fr.winfo_children():
		widget.destroy()
	
	if word in descr:
		txt = scrolledtext.ScrolledText(fr)
		txt.insert(INSERT, word + '\n\n')
		txt.insert(END, descr[word])
		txt.place(relx=0, rely=0, relwidth=1, relheight=1)

def list_all_words(fr: Frame) -> None:
	for widget in fr.winfo_children():
		widget.destroy()
	
	txt = scrolledtext.ScrolledText(fr)
	for word in descr.keys():		
		txt.insert(END, word + '\n\n')
		txt.insert(END, descr[word])
		txt.insert(END, "-------------------------------\n")
	txt.place(relx=0, rely=0, relwidth=1, relheight=1)

root = Tk()
text = []
descr = {}

try:
	with open('ex01_text_data.txt', 'r', encoding='utf-8') as g:
		while True:
			line = g.readline()
			if not line:
				break
			words = line.split(' ')
			for word in words:
				text.append(word)
except:
	pass

try:
	with open('ex01_descr_data.txt', 'r', encoding='utf-8') as g:
		while True:
			line = g.readline()
			if not line:
				break
			words = line.split('|')
			descr[words[0]] = words[1].replace('###n', '\n')
except:
	pass

root.geometry('600x600')

canvass = Canvas(root, bg="#263D42")
canvass.place(relwidth=1, relheight=1)

text_frame = Frame(root, bg="lightgrey")
text_frame .place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

buttons_frame = Frame(root, bg="#263D42")
buttons_frame.place(relx=0.05, rely=0.85, relwidth=0.9, relheight=0.1)

list_text(text_frame)

open_button = Button(buttons_frame, text='Open manual', command=lambda: list_text(text_frame))
open_button.pack(side='left', padx=5, expand=1)

search_button = Button(buttons_frame, text='Search word', command=lambda: search_word(text_frame))
search_button.pack(side='left', padx=5, expand=1)

descr_button = Button(buttons_frame, text='Add description', command=lambda: add_descr(text_frame))
descr_button.pack(side='left', padx=5, expand=1)

all_button = Button(buttons_frame, text='All words', command=lambda: list_all_words(text_frame))
all_button.pack(side='left', padx=5, expand=1)

root.mainloop()

with open('ex01_text_data.txt', 'w', encoding='utf-8') as g:
	g.write(' '.join(text).replace('  ', ''))

with open('ex01_descr_data.txt', 'w', encoding='utf-8') as g:
	for key in descr.keys():
		g.write("{}|{}".format(key, descr[key].replace('\n', '###n') + '\n'))