from PIL import Image, ImageTk
import tkinter as tk
from easygui import buttonbox


def func2():
    arr = ['0', '1', '2', '3', '4', '5', '6', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'action', 'agent', 'algo', 'code', 'data', 'domain','_',
           'dynamic'
        , 'fifo', 'game', 'goal', 'loop', 'nlp', 'nodes', 'no', 'peas', 'pop', 'state', 'static', 'tasks', 'usb', 'web'
        , 'windows', 'yes', 'hira', 'lifo', 'exit', 'send', 'map', 'cpu', 'quit', 'tool', 'gui', 'abacus']

    def process_text():
        text = text_entry.get().lower()

        if text == 'goodbye' or text == 'good bye' or text == 'bye':
            print("Oops! Time to say goodbye")
            root.destroy()
            return

        for word in text.split():
            if word in arr:
                pass
            #     image_address = f'letters1/{word}.jpg'
            #     image = Image.open(image_address)
            #     photo = ImageTk.PhotoImage(image)
            #     label = tk.Label(root, image=photo)
            #     label.image = photo
            #     label.pack()

        else:
             text1 = list(text)
             length = 7
             frame = tk.Frame(root)  # Create a frame to contain the labels
             frame.pack()  # Use pack layout manager for the frame
             

        for x in text1:
            
            if len(text1)<=6:
               image_address = f'letters1/{x}.jpg'
               image = Image.open(image_address)
               photo = ImageTk.PhotoImage(image)
               label = tk.Label(frame, image=photo)
               label.image = photo
               label.pack(side=tk.LEFT, padx=5) 
            
            else:
                for x in text1:
                    while text1:  
                      line = text1[:4] 
                      text1 = text1[4:]   

                      line_frame = tk.Frame(root)  # Create a new frame 
                      line_frame.pack() 

                      for x in line:
                          if x == "_": 
                           line_frame = tk.Frame(root)  # Create a new frame 
                           line_frame.pack() 
                          else:   
                           image_address = f'letters1/{x}.jpg'
                           image = Image.open(image_address)
                           photo = ImageTk.PhotoImage(image)
                           label = tk.Label(line_frame, image=photo)
                           label.image = photo
                           label.pack(side=tk.LEFT, padx=5)
                break       
                          
                        
                  
            #    image_address = 'letters1/invalid.jpg'
            #    image = Image.open(image_address)
            #    photo = ImageTk.PhotoImage(image)
            #    label = tk.Label(frame, image=photo)
            #    label.image = photo
            #    label.pack()
            
            
            
               
                
        # else:
            #    image_address = f'letters1/{x}.jpg'
            #    image = Image.open(image_address)
            #    photo = ImageTk.PhotoImage(image)
            #    label = tk.Label(root, image=photo)
            #    label.image = photo
            #    label.pack()

    def backbutton():
        root.destroy()
        func1()

    def reload():
        root.destroy()
        func2()

    root = tk.Tk()
    root.geometry("1600x1000")  # Set the size of the window (width x height) #1050x500

    window_width = 1400  # 1050
    window_height = 700  # 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label = tk.Label(root, text="Enter text:", font=("Courier New", 16, "bold"))
    label.pack()

    text_entry = tk.Entry(root)
    text_entry.pack()

    button = tk.Button(root, text="CONVERT", width=7, command=process_text, height=2, bg="lightblue", fg="black",
                       font=("Courier New", 13), relief="raised", activebackground="#DBBFDB",
                       activeforeground="white",
                       highlightbackground="yellow", highlightcolor="red")
    button.pack(side='left')

    button1 = tk.Button(root, text="BACK", width=7, command=backbutton, height=2, bg="lightblue", fg="black",
                        font=("Courier New", 13), relief="raised", activebackground="#DBBFDB",
                        activeforeground="white",
                        highlightbackground="yellow", highlightcolor="red")
    button1.pack(side='right')

    button2 = tk.Button(root, text="Reload", width=7, command=reload, height=2, bg="lightblue", fg="black",
                        font=("Courier New", 13), relief="raised", activebackground="#DBBFDB",
                        activeforeground="white", highlightbackground="yellow", highlightcolor="red")

    # Place the button at the bottom
    button2.pack(side=tk.BOTTOM, padx=10, pady=10)
    # button2 = tk.Button(root, text="Reload", width=7, command=reload, height=2, bg="lightblue", fg="black",
    #                     font=("Courier New", 13), relief="raised", activebackground="#DBBFDB",
    #                     activeforeground="white",
    #                     highlightbackground="yellow", highlightcolor="red")
    # button2.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    root.resizable(False, False)

    root.mainloop()


def func1():
    def text():
        root.destroy()
        func2()

    def go_back():
        root.destroy()

    root = tk.Tk()
    root.title("Menu")

    # Set window size and center it
    window_width = 1100
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.resizable(False, False)

    heading_label = tk.Label(root, text="Welcome to Signtistics", font=("Courier New", 20, "bold"))
    heading_label.pack(pady=10)

    heading_label = tk.Label(root, text="Make A Choice", font=("Courier New", 13, "bold"))
    heading_label.pack(pady=14)

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
    alphabets3 = ['u', 'v', 'w', 'x', 'y', 'z']
    word_list1 = ['action', 'agent', 'algo', 'code', 'data', 'domain', 'dynamic', 'fifo', 'game', 'goal', 'good',
                  'loop', 'nlp', 'nodes', 'no', 'peas', 'pop', 'state', 'static', 'tasks']
    word_list2 = ['usb', 'web', 'windows', 'yes', 'hira', 'lifo', 'exit', 'send', 'map', 'cpu', 'quit', 'tool', 'gui',
                  'abacus', 'queue', 'stack']

    # Create a frame for the numbers' grid layout
    numbers_frame = tk.Frame(root, padx=10, pady=4)
    numbers_frame.pack()

    # Create labels for each number in the array
    for index, value in enumerate(numbers):
        # Customize the appearance based on the type of element
        if value.isdigit():
            label = tk.Label(numbers_frame, text=value, bg="#DBBFDB", fg="black")
        elif value.isalpha():
            label = tk.Label(numbers_frame, text=value, bg="green", fg="white")
        else:
            label = tk.Label(numbers_frame, text=value, bg="yellow", fg="black")

        # Configure the label's appearance and padding
        label.config(width=5, height=2, relief="solid")

        # Insert a line break after every 10 characters
        if index % 10 == 0 and index != 0:
            label.pack(pady=(10, 0))  # Add padding after the line break
        else:
            label.pack(side="left", padx=5, pady=3)

    # Create a frame for the alphabets' grid layout
    alphabets_frame = tk.Frame(root, padx=10, pady=10)
    alphabets_frame.pack()

    # Create labels for each alphabet in the array
    for index, value in enumerate(alphabets):
        label = tk.Label(alphabets_frame, text=value, bg="#CE94BC", fg="black")
        label.config(width=5, height=2, relief="solid")

        # Insert a line break after every 10 characters
        if index % 20 == 0 and index != 0:
            label.pack(pady=(10, 0))  # Add padding after the line break
        else:
            label.pack(side="left", padx=5, pady=5)

    # Create a frame for the third alphabets' grid layout
    alphabets_frame3 = tk.Frame(root, padx=10, pady=0)
    alphabets_frame3.pack()

    # Create labels for each alphabet in the array
    for index, value in enumerate(alphabets3):
        label = tk.Label(alphabets_frame3, text=value, bg="#CE94BC", fg="black")
        label.config(width=5, height=2, relief="solid")

        # Insert a line break after every 10 characters
        if index % 10 == 0 and index != 0:
            label.pack(pady=(10, 0))  # Add padding after the line break
        else:
            label.pack(side="left", padx=5, pady=5)

    # Wordlist1

    # Create a frame for the second alphabets' grid layout
    word_frame1 = tk.Frame(root, padx=10, pady=15)
    word_frame1.pack()

    # Create labels for each alphabet in the array
    for index, value in enumerate(word_list1):
        label = tk.Label(word_frame1, text=value, bg="#C8A4D4", fg="black")
        label.config(width=6, height=2, relief="solid")

        # Insert a line break after every 10 characters
        if index % 20 == 0 and index != 0:
            label.pack(pady=(10, 0))  # Add padding after the line break
        else:
            label.pack(side="left", padx=2, pady=5)

            # Wordlist2

    # Create a frame for the second alphabets' grid layout
    word_frame2 = tk.Frame(root, padx=10, pady=-7)
    word_frame2.pack()

    # Create labels for each alphabet in the array
    for index, value in enumerate(word_list2):
        label = tk.Label(word_frame2, text=value, bg="#C8A4D4", fg="black")
        label.config(width=9, height=2, relief="solid")

        # Insert a line break after every 10 characters
        if index % 16 == 0 and index != 0:
            label.pack(pady=(10, 0))  # Add padding after the line break
        else:
            label.pack(side="left", padx=2, pady=5)

            # Create the Text button
    button1 = tk.Button(root, text="Text", width=10, height=2, bg="lightblue", command=text,
                        font=("Courier New", 10, "bold"))
    button1.pack(side="left", padx=(430, 10), pady=10)

    # Create the Back button
    button2 = tk.Button(root, text="Back", width=10, height=2, bg="lightblue", command=go_back,
                        font=("Courier New", 10, "bold"))
    button2.pack(side="left", padx=40, pady=10)

    root.mainloop()


while True:
    # image = "hello.png"
    # msg = "Welcome To Signtistics"
    # choices = ["Menu", "Quit"]
    # reply = buttonbox(msg, image=image, choices=choices,button_color=("white","blue"),font=("Helvetica", 12"))
    # if reply == choices[0]:
    #     func1()
    # if reply == choices[1]:
    #     quit()

    import tkinter as tk
    from tkinter import messagebox


    def show_menu():
        root = tk.Tk()
        root.title("Welcome To Signtistics")

        window_width = 700
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Set the background image
        background_image = tk.PhotoImage(file="hello.png")
        background_label = tk.Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def menu_choice(choice):
            if choice == "Menu":
                root.destroy()
                func1()
            elif choice == "Quit":
                root.destroy()
                quit()

        # Create the buttons
        button_menu = tk.Button(root, text="Menu", font=("Courier New", 12), fg="black", bg="lightblue",
                                command=lambda: menu_choice("Menu"))
        button_quit = tk.Button(root, text="Quit", font=("Courier New", 12), fg="black", bg="lightblue",
                                command=lambda: menu_choice("Quit"))

        # Position the buttons
        button_menu.pack(side="left", padx=10, pady=10)
        button_quit.pack(side="right", padx=10, pady=10)

        root.mainloop()


    show_menu()