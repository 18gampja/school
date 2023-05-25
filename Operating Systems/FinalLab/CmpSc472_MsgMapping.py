# Jacob Gampa CMPSC 472 Final Lab
# This program is one that reads a text file in the same directory
# and stores its data. Then, it can read it back to  you or display it.
# It can also reconstruct any of the lines for you.

import tkinter as tk
from tkinter import messagebox
import re
import os
from pathlib import Path

scriptPath = Path(__file__, '..').resolve()

stringList, wordList = [], []

def showTextFile():

    success = False
    txtFile = os.path.join(scriptPath, inputEntry.get())

    try:
        with open(txtFile, 'r') as file:
            success = True
            messagebox.showerror(title=inputEntry.get(), message=file.read())    

    except:
        pass

    if success == False:
        try:
            with open(inputEntry.get(), 'r') as file:
                messagebox.showerror(title=inputEntry.get(), message=file.read())

        except FileNotFoundError:
            messagebox.showerror(title="Error:", message="Error: Cannot find Text File!")

def readTextButton():

    txtFile = os.path.join(scriptPath, inputEntry.get())

    try:
        with open(txtFile, 'r') as file:
            for i, line in enumerate(file.readlines()):
                words = [wordList.index(word) if word in wordList else wordList.append(word) or len(wordList) - 1 for word in re.findall(r"[\w']+", line.lower())]
                stringData = {"fileName": inputEntry.get(), "messageNumber": i + 1, "numWords": len(words), "replacedWords": words, "uniqueWords": len(set(words))}
                stringList.append(stringData)
                wordsTextbox.insert(tk.END, f"Words found in Message: {i + 1}: {set(words)}\n")
    except FileNotFoundError:
        messagebox.showerror(title="Error:", message="Error: Cannot find Text File!")

def reassembleMessage():
    
    messageNumber = int(inputEntry2.get())

    for stringData in stringList:
        if stringData["messageNumber"] == messageNumber:
            reassembleMessage.delete("1.0", tk.END)
            reassembleMessage.insert(tk.END, "\"" + " ".join([wordList[num] + "." if i == len(stringData["replacedWords"]) - 1 else wordList[num] for i, num in enumerate(stringData["replacedWords"])]) + "\"")
            break
    else:
        messagebox.showerror(title="Error:", message="Error: Cannot find Message!")

window = tk.Tk()
window.title("Message Mapping Program")
window.geometry("1000x750+250-60")

inputLabel = tk.Label(window, text="Input Text File Here", anchor="w")
inputLabel.pack(fill="x", padx=10, pady=10)

inputEntry = tk.Entry(window)
inputEntry.pack(fill="x", padx=10)

tk.Button(window, text="Show Text File.", command=showTextFile).pack(padx=10, pady=10, anchor="w")
tk.Button(window, text="Read messages from Text File.", command=readTextButton).pack(padx=10, pady=10, anchor="w")

wordsLabel = tk.Label(window, text="Words Found:", anchor="w")
wordsLabel.pack(fill="x", padx=10, pady=10)

wordsTextbox = tk.Text(window, height=10, font=("Arial", 10))
wordsTextbox.pack(fill="both", padx=10)

inputLabel2 = tk.Label(window, text="Input message number to reassemble here", anchor="w")
inputLabel2.pack(fill="x", padx=10, pady=10)

inputEntry2 = tk.Entry(window)
inputEntry2.pack(fill="x", padx=10)

tk.Button(window, text="Reassemble Message.", command=reassembleMessage).pack(padx=10, pady=10, anchor="w")

wordsLabel = tk.Label(window, text="Reassembled Message:", anchor="w")
wordsLabel.pack(fill="x", padx=10, pady=10)

reassembleMessage = tk.Text(window, height=10)
reassembleMessage.pack(fill="both", padx=10)

window.mainloop()
