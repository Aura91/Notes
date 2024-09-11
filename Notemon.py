from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font
import os

# New file method
def newFile():
    global file
    root.title("Untitled - Notemon!")
    file = None
    TextArea.delete(1.0, END)

# Open file method
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notemon!")
        TextArea.delete(1.0, END)
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())

# Save method
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file == "":
            file = None
        else:
            with open(file, "w") as f:
                f.write(TextArea.get(1.0, END))
            root.title(os.path.basename(file) + " - Notemon!")
    else:
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))

# Save as method
def saveAs():
    global file
    file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file == "":
        file = None
    else:
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))
        root.title(os.path.basename(file) + " - Notemon!")

# Exit method
def quitApp():
    root.destroy()

# Cut, copy, paste methods
def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

# Help/About method
def about():
    showinfo("Notemon", "This is Notemon made by Tilak!")

# Change font
def changeFont(font_name):
    current_font = TextArea.cget("font")
    font = Font(font=current_font)
    font.config(family=font_name)
    TextArea.config(font=font)

# Change font size
def changeFontSize(size):
    current_font = TextArea.cget("font")
    font = Font(font=current_font)
    font.config(size=size)
    TextArea.config(font=font)

# Toggle bold
def toggleBold():
    current_font = TextArea.cget("font")
    font = Font(font=current_font)
    weight = 'bold' if font.actual()['weight'] == 'normal' else 'normal'
    font.config(weight=weight)
    TextArea.config(font=font)

# Toggle italic
def toggleItalic():
    current_font = TextArea.cget("font")
    font = Font(font=current_font)
    slant = 'italic' if font.actual()['slant'] == 'roman' else 'roman'
    font.config(slant=slant)
    TextArea.config(font=font)

# Toggle strikethrough
def toggleStrikethrough():
    current_font = TextArea.cget("font")
    font = Font(font=current_font)
    overstrike = 1 if font.actual()['overstrike'] == 0 else 0
    font.config(overstrike=overstrike)
    TextArea.config(font=font)

# Main
if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notemon!")
    root.geometry("640x420")

    # TextArea settings
    TextArea = Text(root, font="lucida 13", bg="#181818", fg="White")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Menubar START
    Menubar = Menu(root)

    # File Menu START
    File_menu = Menu(Menubar, tearoff=0)
    File_menu.add_command(label="New", command=newFile)
    File_menu.add_command(label="Open", command=openFile)
    File_menu.add_command(label="Save", command=saveFile)
    File_menu.add_command(label="Save as", command=saveAs)
    File_menu.add_separator()
    File_menu.add_command(label="Exit", command=quitApp)
    Menubar.add_cascade(label="File", menu=File_menu)

    # Edit Menu START
    Edit_menu = Menu(Menubar, tearoff=0)
    Edit_menu.add_command(label="Cut", command=cut)
    Edit_menu.add_command(label="Copy", command=copy)
    Edit_menu.add_command(label="Paste", command=paste)
    Menubar.add_cascade(label="Edit", menu=Edit_menu)

    # Format Menu START
    Format_menu = Menu(Menubar, tearoff=0)
    
    Font_menu = Menu(Format_menu, tearoff=0)
    Font_menu.add_command(label="Arial", command=lambda: changeFont("Arial"))
    Font_menu.add_command(label="Courier", command=lambda: changeFont("Courier"))
    Font_menu.add_command(label="Times New Roman", command=lambda: changeFont("Times New Roman"))
    Format_menu.add_cascade(label="Font", menu=Font_menu)
    
    Font_size_menu = Menu(Format_menu, tearoff=0)
    Font_size_menu.add_command(label="10", command=lambda: changeFontSize(10))
    Font_size_menu.add_command(label="12", command=lambda: changeFontSize(12))
    Font_size_menu.add_command(label="14", command=lambda: changeFontSize(14))
    Font_size_menu.add_command(label="16", command=lambda: changeFontSize(16))
    Font_size_menu.add_command(label="18", command=lambda: changeFontSize(18))
    Font_size_menu.add_command(label="20", command=lambda: changeFontSize(20))
    Format_menu.add_cascade(label="Font Size", menu=Font_size_menu)
    
    Format_menu.add_command(label="Bold", command=toggleBold)
    Format_menu.add_command(label="Italic", command=toggleItalic)
    Format_menu.add_command(label="Strikethrough", command=toggleStrikethrough)
    Menubar.add_cascade(label="Format", menu=Format_menu)

    # Help Menu START
    Help_menu = Menu(Menubar, tearoff=0)
    Help_menu.add_command(label="About", command=about)
    Menubar.add_cascade(label="Help", menu=Help_menu)

    root.config(menu=Menubar)

    # Scrollbar START
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    TextArea.config(yscrollcommand=Scroll.set)
    Scroll.config(command=TextArea.yview)
    # Scrollbar END

    root.mainloop()
