import os
app = raw_input(" Which application would you like to open?...  ")
file = raw_input(" Would you like to open a particular file with it?... ")

if file != "no" and file != "No":
    os.system("open -a" + app + " " + file)
else:
    os.system("open -a" + app)
