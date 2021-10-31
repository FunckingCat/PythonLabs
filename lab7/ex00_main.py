from tkinter import *
from ex00_note import Note

def list_notes(fr: Frame) -> None:
	for widget in fr.winfo_children():
		widget.destroy()
	notes.sort(key=lambda x: x.days_past())
	for note in notes:
		lb = Label(fr, text=note.pretty())
		lb.pack()

def clear_notes() -> None:
	fr = notes_frame
	notes.clear()
	for widget in fr.winfo_children():
		widget.destroy()

def clear() -> None:
	fr = notes_frame
	list_notes(fr)

def make_file():
	fr = notes_frame
	path = fr.winfo_children()[0].get()
	for widget in fr.winfo_children():
		widget.destroy()
	try:
		with open(path, 'w', encoding='utf-8') as g:
			for note in notes:
				g.write(note.pretty() + '\n')
		lb = Label(fr, text="Sucssess")
		lb.pack()
	except:
		lb = Label(fr, text="Falid to write a text")
		lb.pack()


def write_file():
	fr = notes_frame
	for widget in fr.winfo_children():
		widget.destroy()

	path = Entry(fr)
	path.insert(0, './output.txt')
	path.pack(pady=5)

	write_btn = Button(fr, text='Write', command=make_file, width=10, height=1)
	write_btn.pack(padx=3)

def	find_notes():
	fr = notes_frame
	tel = fr.winfo_children()[0].get()
	for widget in fr.winfo_children():
		widget.destroy()
	for note in notes:
		if tel == note.tel:
			lb = Label(fr, text=note.pretty())
			lb.pack()
	if len(fr.winfo_children()) == 0:
		lb = Label(fr, text="No notes with same phone number")
		lb.pack()

def serch():
	fr = notes_frame
	for widget in fr.winfo_children():
		widget.destroy()

	tl = Entry(fr)
	tl.insert(0, 'Tel')
	tl.pack(pady=5)

	sch_btn = Button(fr, text='Search', command=find_notes, width=10, height=1)
	sch_btn.pack(padx=3)

def add_note():
	fr = notes_frame
	vl = []
	for widget in fr.winfo_children():
		if widget.winfo_class() == 'Entry':
			vl.append(widget.get())
		if widget.winfo_class() == 'Frame':
			date = []
			for item in widget.winfo_children():
				date.append(item.get())
			vl.append(date)
	new_note = Note(vl[1], vl[0], vl[2], vl[3])
	notes.append(new_note)
	list_notes(notes_frame)

def add():
	fr = notes_frame
	for widget in fr.winfo_children():
		widget.destroy()

	nm = Entry(fr)
	nm.insert(0, 'Name')
	nm.pack(pady=5)

	sr = Entry(fr)
	sr.insert(0, 'Surname')
	sr.pack(pady=5)

	tl = Entry(fr)
	tl.insert(0, 'Tel')
	tl.pack(pady=5)

	bd_frame = Frame(fr, width=230, height=30)
	bd_frame.pack(pady=5)

	day = Spinbox(bd_frame, from_=1, to=31, width=5)
	day.pack(side='left', padx=3)

	month = Spinbox(bd_frame, from_=1, to=12, width=5)
	month.pack(side='left', padx=3)

	year = Spinbox(bd_frame, from_=1920, to=2021, width=5)
	year.pack(side='left', padx=3)

	add_btn = Button(fr, text='Save', command=add_note, width=10, height=1)
	add_btn.pack(padx=3)

root = Tk()
notes = []
try:
	with open('ex00_data.txt ', 'r', encoding='utf-8') as g:
		while True:
			line = g.readline()
			if not line:
				break
			new_note = Note.init_from_str(line[:-1])
			notes.append(new_note)
except:
	pass

root.geometry('600x300')

canvass = Canvas(root, bg="#263D42")
canvass.place(relwidth=1, relheight=1)

notes_frame = Frame(root, bg="lightgrey")
notes_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.6)

buttons_frame = Frame(root, bg="#263D42")
buttons_frame.place(relx=0.05, rely=0.75, relwidth=0.9, relheight=0.15)

list_notes(notes_frame)

add_button = Button(buttons_frame, text='Add note', command=add)
add_button.pack(side='left', padx=5, expand=1)

clear_button = Button(buttons_frame, text='Del notes', command=clear_notes)
clear_button.pack(side='left', padx=5, expand=1)

clear_button = Button(buttons_frame, text='Search', command=serch)
clear_button.pack(side='left', padx=5, expand=1)

write_button = Button(buttons_frame, text='Write to file', command=write_file)
write_button.pack(side='left', padx=5, expand=1)

clear_button = Button(buttons_frame, text='Clear', command=clear)
clear_button.pack(side='left', padx=5, expand=1)

root.mainloop()

with open('ex00_data.txt ', 'w', encoding='utf-8') as g:
	for note in notes:
		g.write(note.to_string() + '\n')