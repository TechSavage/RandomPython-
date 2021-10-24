###################################################################
# Takes a csv list and allows you to select
# A random sample of your choosing
# 
# Run this program in the same folder as your csv, 
# Update the filename in line #19
# This outputs the sample to a file "Results.txt"
###################################################################
import random
from tkinter import *
import tkinter as tk

List_Generator = tk.Tk()
List_Generator.title('Random Sample Generator')
List_Generator.geometry("400x70")

def submit():
	size = int(SampleSize.get())
	list=open('List.csv').read().split(',')
	listRand = random.sample(list,size)
	file = open('Results.txt', 'w')
	file.write('\n'.join(listRand))
	file.close()

###################################################################
# Output Window (unfinished)
#   x = '\n'.join(listRand)
#	results = Toplevel()
#	results.title('Results')
#	resultsLabel = Label(results, text = x)
#	resultsLabel.pack()
###################################################################


listLabel = tk.Label(List_Generator, text="Random Sample of List: ")
SampleSize = tk.Entry(List_Generator)
submit_button = tk.Button(
	List_Generator, 
	text="Submit",
	font=('Bookman',10,'bold'),
	width=20,
	height=2,
	fg="Black",
	bg="Silver",
	justify='center',
	command = submit
	)
listLabel.grid(row=0,column=0)
SampleSize.grid(row=0,column=1)
submit_button.grid(row=1,column=1)	

List_Generator.mainloop()