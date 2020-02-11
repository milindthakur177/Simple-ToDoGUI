# To-Do App

import tkinter as tk 
import webbrowser
import os

def todo(TODO):
	try:
		if TODO== 'pycharm':
			os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe")
		elif TODO== 'sublime':
			os.startfile("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
		elif any(ext in TODO for ext in ('.py', '.txt', '.csv', '.ppt')):
			os.open('{}'.format(TODO,os.O_RDWR|os.O_CREAT))
			os.startfile('{}'.format(TODO))
		elif 'search' in TODO:
			url='http://google.com/search?q='+TODO.replace('search','')
			webbrowser.open(url)
		elif 'facebook' in TODO:
			webbrowser.open('https://www.facebook.com/')
		elif 'instagram' in TODO:
			webbrowser.open('https://www.instagram.com/')
		elif 'github' in TODO:
			webbrowser.open('https://github.com/')
		else:
			pass
	except Exception as exc:
    		print('Exception occurred: {}'.format(exc))
    		pass

root= tk.Tk()
root.title('To-Do GUI')


entry = tk.Entry(root, font=40, width=35)
entry.grid(row=0,column=0)
entry.focus()

button = tk.Button(root, text="GO", font=40, command=lambda: todo(entry.get()))
button.grid(row=0 ,column=4)

root.mainloop()