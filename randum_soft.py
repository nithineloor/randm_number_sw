import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox



import pandas as pd
import numpy as np

import random
import string

import os
import shutil  # to move files



root = tk.Tk() # main window 
root.title('Random Code Generator')

root.geometry("550x200")
info_for_entry = Label(root, text= "Enter the required number of codes")
info_for_entry.grid(row = 0, column = 0, sticky = W, padx = (2,20), pady = (10,5)) 

nos = tk.Entry() # entry field
nos.grid(row = 0, column = 2, sticky = W, pady = (10,5)) 

#************************premium features*******************************#

info_code_length = Label(root, text= "Enter the code length *")
info_code_length.grid(row = 5, column = 0, sticky = W, padx = (2,20), pady = 2) 

length_entry = tk.Entry(root, state = 'disabled') # entry field
length_entry.grid(row = 5, column = 2, sticky = W, pady = 2) 

info_code_suffix = Label(root, text= "Enter Suffix *")
info_code_suffix.grid(row = 7, column = 0, sticky = W, padx = (2,20), pady = 2) 

suffix_entry = tk.Entry(root, state = 'disabled') # entry field
suffix_entry.grid(row = 7, column = 2, sticky = W, pady = 2) 

info_code_prefix = Label(root, text= "Enter prefix *")
info_code_prefix.grid(row = 9, column = 0, sticky = W, padx = (2,20), pady = 2) 

prefix_entry = tk.Entry(root, state = 'disabled') # entry field
prefix_entry.grid(row = 9, column = 2, sticky = W, pady = 2) 

contact_label = Label(root, text= "*contact to enable all features:")
contact_label.grid(row = 12, column = 0, sticky = W, padx = (2,20), pady = (35,0)) 


#***********************************************************************#

global n #global variable for number of codes input
n = 0

# Function to generate random codes

def get_random_alphanumeric_string(letters_count, digits_count):
	
    sample_letters = 'ABCDEFGHJKMNPQRTUVWXYZacdefhjkmnprtuvwxyz'
    sample_digit = '234678'
    sample_str = ''.join((random.choice(sample_letters) for i in range(letters_count)))
    sample_str += ''.join((random.choice(sample_digit) for i in range(digits_count)))
    # Convert string to list and shuffle it to mix letters and digits
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string

# fuction to take user input
#(number of required codes)

def getnum():
	global n

	try: 
		nums = int(nos.get())
		n=nums
		generate()
	except ValueError: 
		messagebox.showinfo("Alert !", "Enter a valid digit")
		nos.delete(0, END) # Clearing the entry widget

	# log any other error to a file
	except Exception as Argument: 
  
	# creating/opening a file 
		f = open("logfile.txt", "a") 
  
	# writing in the file 
		f.write(str(Argument)) 
       
	# closing the file 
		f.close()  


# Function to add created random number into a list,
# to create a excel file, 
# and checks for duplication
# then saves file into a new location
	
def generate():
	rndmlist=[]
	global n
	while (n!=0):
		#passing the number of digit and letter required in the code
		rnd = get_random_alphanumeric_string(5, 3)
		if rnd not in rndmlist:
			rndmlist.append(rnd)
			n = n-1
			
	# creating a data frame from the gerated list of codes
	rndmxl = pd.DataFrame(rndmlist)
	rndmxl.columns = ['Random Codes']
	rndmxl.to_excel("random.xlsx")
	
	# current path of generated file
	
	cwd = os.path.realpath("random.xlsx")
		
	messagebox.showinfo("Save", "Codes are ready; Select a folder to save your code file")
	
	# Destination path to save file
	
	new_dir_name = filedialog.askdirectory(title="Select a folder to save your code")
	
	
	# copies file to destination insted of moving
	# to avoid "File already Exist" error, 
	# and deletes it from the original/root location

	shutil.copy(cwd, new_dir_name) 
	os.remove(cwd)
	messagebox.showinfo("File Saved", "File Saved")



button = tk.Button(text = 'Enter ', command = getnum) 
button.grid(row = 0, column = 3, sticky = W, padx = (30,8), pady = (10,5)) 

#*****************Premium*********************************#

button2 = tk.Button(text = 'Enter ', state = 'disabled') 
button2.grid(row = 5, column = 3, padx = (30,8), pady = (0)) 


button3 = tk.Button(text = 'Enter ', state = 'disabled')
button3.grid(row = 7, column = 3, padx = (30,8), pady = (0)) 

button4 = tk.Button(text = 'Enter ', state = 'disabled')
button4.grid(row = 9, column = 3, padx = (30,8), pady = (0)) 

#***********************************************************#

# to popup "Do you want to quit" dialouge for root/main window

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()
