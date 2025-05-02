import tkinter as tk
from tkinter import Listbox

from trie import Trie

trie = Trie()
words =["banana", "bananas", "car", "bike", "cat", "binocle", "cake", "dog", "dogs", "orange", "orbit", "orangutang"]
for word in words:
    trie.insert(word)
    
#GUI setup
root = tk.Tk()
root.title("Autocomplete Form")
root.geometry("300x400")

# Search
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Listbox for suggestions
listbox = Listbox(root, width=30, height=15)
listbox.pack(pady=10)

# Initialize list with words
for word in words:
    listbox.insert(tk.END, word)
    
# Update listbox on input
def update_list(event):
    listbox.delete(0, tk.END) #clear current list
    prefix = entry.get()
    suggestions = trie.autocomplete(prefix)
    for suggestion in suggestions:
        listbox.insert(tk.END, suggestion)
        
# Bind typing to update
entry.bind("<KeyRelease>", update_list)
root.mainloop()