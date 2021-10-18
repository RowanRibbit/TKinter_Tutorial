from tkinter import *
import tkinter as tk

# create the app root
root = Tk()

class ToDoItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Create a class to hold the props of the app
class ToDoListApp:
    def __init__(self, root):
        # Customize the app
        root.title('To Do List')
        # root.geometry([str]) for dim
        # root.geometry('500x400')
        # max size does not take in a string
        # root.maxsize(1000,800)

        # the frame widget - used to group widgets Frame(root, relief='[border]')
        frame = Frame(root, relief='sunken', borderwidth=2)
        frame.grid(column=1,row=1, sticky=(N, E, S, W))
        # columnconfigure takes the root and configures a grid or column structure that exists within in
        # now the root has a grid within it, setting column 1 as weight 1 for the entire window
        # as the frame exists within root have to call root.xconfigure()
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        # create a todo item list
        self.todo_items = [
            ToDoItem("Workout", "Squats"),
            ToDoItem("Cleaning", 'Clean Kitchen, Hoover'),
            ToDoItem('Wash up', 'Shave legs, Do hair')
        ]

        # listbox widget
        # create a list, feed into a string variable, and pass into listvariable
        self.list_item_strings = ['Hey', 'Hi', 'Hello', 'Howdy']
        # list_items = StringVar(value=self.list_item_strings)


        
        list_label = Label(frame, text='Todo Items')
        list_label.grid(column=1, row=1, sticky=(S, W))
        # now have a list of todo items, so instead use this
        # map the todo items to a list of strings
        # map applies this lambda function to each item in the list, making a new list of names
        self.todo_names = StringVar(value=list(map(lambda x: x.name, self.todo_items)))

        items_list = Listbox(frame, listvariable=self.todo_names)
        # listbox.pack(side=tk.LEFT, padx=40, pady=20)
        items_list.grid(column=1, row=2, sticky=(E, W), rowspan=5)

        # default listbox size is 10 rows
        # change the size of te listbox in intializer or configure or dictionary
        # bind to bind events to the listbox, bind the function to the selection form the listbox, takes in action and function
        # <<[keycode]>>
        # lambda function to call self.x current selected index, passes into select_item
        items_list.bind('<<ListboxSelect>>', lambda s: self.select_item(items_list.curselection()))

        self.selected_description = StringVar()
        selected_description_label = Label(frame, textvariable=self.selected_description, wraplength=120)
        selected_description_label.grid(column=1, row=7, sticky=(N, E, W))

        # new Todo items
        new_item_label = Label(frame, text='New Item')
        new_item_label.grid(column=2, row=1, sticky=(S, W))

        # Heading and entry for name
        name_label = Label(frame, text='Item name')
        name_label.grid(column=2, row=2, sticky=(S,W))

        self.name = StringVar()
        name_entry = Entry(frame, textvariable=self.name)
        name_entry.grid(column=2, row=3, sticky=(N, E, W))

        # Heading and entry for description
        desc_label = Label(frame, text='Item description')
        desc_label.grid(column=2, row=4, sticky=(S,W))

        self.desc = StringVar()
        desc_entry = Entry(frame, textvariable=self.desc)
        desc_entry.grid(column=2, row=5, sticky=(N, E, W))

        # save button
        save_button = Button(frame, text='Save', command=self.new_item)
        save_button.grid(column=2, row=6, sticky=(E))

        # for loop to add padding to everything with a parent
        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=5)

        # to initialize a widget have to include the parent widget
        # label = Label(root, text='new label')

        # now we have the frame within the widget, change root to frame
        # label = Label(frame, text='New Label')

        # x.pack() adds a widget from top to bottom
        # side=tk.TOP is default behaviour, top > bottom, similarly BOTTOM is bottom > top, also LEFT/RIGHT
        # padx and pady=[pixel values]
        # label.pack(side=tk.TOP, padx=10, pady=5)
        # use grid to define a grid at runtime with widgets
        # label.grid(column=1, row=1)

        
        # grid widgets are not glued to any dimensions, size determined by greatest dimensions, x or y
        # grid(column=1, row=1) is top left, but grid currently only 1 column


        # dictonary syntax can change a widget content, useful if want to change one at a time
        # label['text'] = 'new label text'
        # label['font'] = ('Courier', 40)
        # but if you want to change multiple things, better to use the configure method
        # label.configure(text = 'more labels', font = ('Courier', 30))

        # entry widgets - single line text inputs. Will bind the entry text to a variable for processing
        # StringVar is special, binds text in Entry
        # self.entry_text = StringVar()
        # bind the StringVar to our Entry, automatically updates the StringVar
        # entry = Entry(frame, textvariable=self.entry_text)
        # Can entry_text.get and entry_text.set to get and set vars
        # entry.pack()

        # instead use entry.place(x, y) to define position, useful for fine control but can be tricky with multiple widges
        # entry.place(x=100,y=50)

        # instead of place use Grid - specify which row and column you want a widget to go in and when you're done it builds the grid
        # can determine the position within the grid, or the size of the element
        # sticky takes in coordinates as a tuple i.e., S, W (behaves the same as SW)
        # make the button fill the width of the cell using S, E, W to go across the entire width of the cell
        # entry.grid(column=2, row=1)

        # bind the StringVar to the label, so updating the text box updates the label
        # label['textvariable'] = entry_text

        # Buttons, command takes in reference to a function with no parentheses
        # button = Button(frame, text='button', command=self.press_button)
        # button.pack()
        # sizing
        # button.place(x=0, y=0)
        # width based on char size, height on char height
        # button.configure(width=10, height=1, font=('Courier', 40))

        # button.grid(column=1, row=2, sticky=(S, E, W))
        

        # get the string value and set the value of the label text within press_button()
        # create a string variable just for the label to limit what you're assigning to a field
        # Update entry_text and label_text to self.x
        # self.label_text = StringVar()
        # label['textvariable'] = self.label_text
        # can also bind to the return key but will be using the button for this tutorial
        
        



    def press_button(self):        
        text = self.entry_text.get()
        self.label_text.set(text)

    def select_item(self, index):
        # takes in index of the selected item
        # access the index of list_item_strings so make self.x
        # lambda curselection function returns a tuple (index, blank)
        # selected_item = self.list_item_strings[index[0]]
        # todo: actual logic
        print(index[0])
        description = self.todo_items[index[0]].description
        print(description)
        # use Set for StringVar(), rather than assigning var
        self.selected_description.set(description)
        print('item selected')

    def new_item(self):
        # use get when dealing with StringVar()
        new_name = self.name.get()
        new_desc = self.desc.get()
        todo = ToDoItem(new_name, new_desc)
        self.todo_items.append(todo)
        # remap the list of todo_names
        # set todo_names to the new list of names
        self.todo_names.set(list(map(lambda x: x.name, self.todo_items)))
        self.name.set('')
        self.desc.set('')


# Initialize the class
ToDoListApp(root)

# run the root
root.mainloop()
