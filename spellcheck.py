# MCS 260 Spring 2022 Project 4
# Jesus Romero
# Declaration: I, Jesus Romero, am the sole author of this code, which was developed in accordance with the rules in the couorse syllabus.




import tkinter
import tkinter.ttk
from tkinter import Text, Label, Button
import re
import difflib


pg = tkinter.Tk()
pg.geometry("1000x1000")
pg.title("Spell Check!")

text1 = Text(pg,height=15,width=55,font=('Comic Sans MS',15))
text1.grid(row=2,column=1,padx=15,pady=15)
lbl = Label(pg,text="Enter the text you want checked below:",font=('Comic Sans MS',20,'bold italic')).grid(row=1,column=1)


"""This function is called whenever the button created with Tkinter is clicked. It calls the mainfunction."""
def buttonactivator():
    mainfunction()

B = Button(pg,text="Check my words!",command=buttonactivator).grid(row=3,column=1)


"""This function is used to separate each word entered in the text box by the user and put it in a list. It is also stripping all the new line characters that are present at the end of each word"""
def readdicfile():
    dictionaryfile = open("dictionary.txt","r")
    global dictlist
    dictlist = []
    for line in dictionaryfile:
        word = line.strip()
        dictlist.append(word)
    dictionaryfile.close()


"""This function takes the input entered in the text box by the user and sets it equal to the 'userinput' variable. That input is then written onto a new file named 'usertext.txt"""
def text2file():
    global userinput
    userinput = text1.get(1.0,"end-1c")
    usertext = open("textbeingchecked.txt","w")
    userinput = userinput.replace(" ","\n")
    usertext.write(userinput)
    usertext.close()



"""This function reads the text file containing all the text input from the user and goes through each line and adds each word onto the list giventext, while also stripping everyword from all punctuation such as commas and periods"""
def readtextfile():
    usertext = open("textbeingchecked.txt","r")
    global giventext
    giventext = []
    for line in usertext:
        newword = line.strip(',.?/:;"!\n').lower()
        giventext.append(newword)

"""The purpose of this function is to use the dictionary list and the list containing all the words entered in the box by the user. We search to see if each individual word is included in the dictionary file. If the word is included in the dictionary file, it means the word is correct, but if it is not included, it means the word is incorrectly written"""
def locateerrors():
    errorsolutions = open("errorsolutions.txt","w")
    global misspelledwords
    misspelledwords = []
    for word in giventext:
        if word not in dictlist:
            misspelledwords.append(word)
            print("The word",word,"is spelled wrong!")
            finderrorsolutions()
            misspelledwords = []
            errorsolutions.write(word+"\n")
    errorsolutions.close()
"""The purpose of this funciton is to find possible solutions or fixes for the misspelled words"""
def finderrorsolutions():
    errorsolutions = open("errorsolutions.txt","a+")
    for word in misspelledwords:
        suggestion = difflib.get_close_matches(word,dictlist)
        print("Did you mean,",suggestion,"?")
        errorsolutions.write(str(suggestion)+"\n")
    errorsolutions.close()




"""This function is called by the buttonactivator function which means that this is called everytime the button is clicked. The functions tex2fle(), readdictfile(), readtextfile(), locateerrors() and suggestions() are called by this function."""
def mainfunction():
    text2file()
    readdicfile()
    readtextfile()
    locateerrors()
    solution2file()




















pg.mainloop()
