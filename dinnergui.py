#Robert Marsh
#Oct 25, 2020
#Program creates gui for dinner selection


import tkinter as tk
import random

def button_click():

    entryone = entry0.get()
    entrytwo = entry1.get()
    entrythree = entry2.get()
    entryfour = entry3.get()
    entryfive = entry4.get()

    if entryone == "666" or entrytwo == "666" or entrythree == "666" or entryfour == "666" or entryfive == "666":
        output_text.config(text = "Torchy's Tacos")
    else:
        while True:
            select = random.randint(1, 5)
            if select == 1 and entryone != "":
                output_text.config(text = entryone)
                break
            elif select == 2 and entrytwo != "":
                output_text.config(text = entrytwo)
                break
            elif select == 3 and entrythree != "":
                output_text.config(text = entrythree)
                break
            elif select == 4 and entryfour != "":
                output_text.config(text = entryfour)
                break
            elif select == 5 and entryfive != "":
                output_text.config(text = entryfive)
                break
            elif entryone == "" and entrytwo == "" and entrythree == "" and entryfour == "" and entryfive == "":
                output_text.config(text = "Why didn't you enter anything?")
                break
     

HEIGHT = 400
WIDTH = 480

root = tk.Tk()

root.resizable(width = False, height = False)

root.title("Dinner Selector")

root.iconbitmap("c:/Users/whybn/OneDrive/Desktop/dinner/forkg.ico")

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg = "red")
canvas.pack()

top_label = tk.Label(root, text = "Enter 5 dinner options, one will be picked randomly.", bg = "red", font = ("Comic Sans MS", 12))
top_label.place(relx = .02, rely = .02, relheight = 0.1)

frame0 = tk.Frame(root, bg = "#80c1ff", bd = 5)
frame0.place(relx = 0.02, rely = 0.12, relwidth = 0.65, relheight = 0.075)

entry0 = tk.Entry(frame0, bg = "white")
entry0.place(relwidth = 0.65, relheight = 1)

label0 = tk.Label(frame0, text = "Choice 1", bg = "white", font = ("Comic Sans MS", 12))
label0.place(relx = .75, relheight = 1)

frame1 = tk.Frame(root, bg = "#80c1ff", bd = 5)
frame1.place(relx = 0.02, rely = 0.24, relwidth = 0.65, relheight = 0.075)

entry1 = tk.Entry(frame1, bg = "white")
entry1.place(relwidth = 0.65, relheight = 1)

label1 = tk.Label(frame1, text = "Choice 2", bg = "white", font = ("Comic Sans MS", 12))
label1.place(relx = .75, relheight = 1)

frame2 = tk.Frame(root, bg = "#80c1ff", bd = 5)
frame2.place(relx = 0.02, rely = 0.36, relwidth = 0.65, relheight = 0.075)

entry2 = tk.Entry(frame2, bg = "white")
entry2.place(relwidth = 0.65, relheight = 1)

label2 = tk.Label(frame2, text = "Choice 3", bg = "white", font = ("Comic Sans MS", 12))
label2.place(relx = .75, relheight = 1)

frame3 = tk.Frame(root, bg = "#80c1ff", bd = 5)
frame3.place(relx = 0.02, rely = 0.48, relwidth = 0.65, relheight = 0.075)

entry3 = tk.Entry(frame3, bg = "white")
entry3.place(relwidth = 0.65, relheight = 1)

label3 = tk.Label(frame3, text = "Choice 4", bg = "white", font = ("Comic Sans MS", 12))
label3.place(relx = .75, relheight = 1)

frame4 = tk.Frame(root, bg = "#80c1ff", bd = 5)
frame4.place(relx = 0.02, rely = 0.60, relwidth = 0.65, relheight = 0.075)

entry4 = tk.Entry(frame4, bg = "white")
entry4.place(relwidth = 0.65, relheight = 1)

label4 = tk.Label(frame4, text = "Choice 5", bg = "white", font = ("Comic Sans MS", 12))
label4.place(relx = .75, relheight = 1)

button = tk.Button(root, text = "I'M HUNGRY!", bg = "grey", command = button_click, font = ("Comic Sans MS", 9))
button.place(relx = .75, rely = .8, relwidth = .20)

selection_label = tk.Label(root, text = "Selection", bg = "red", font = ("Comic Sans MS", 12))
selection_label.place(relx = .02, rely = .725, relheight = 0.1)

output_text = tk.Label(root, bg = "white", text = "", anchor = "w", font = ("Comic Sans MS", 12))
output_text.place(relx = 0.02, rely = 0.8, relwidth = 0.65)


root.mainloop()
