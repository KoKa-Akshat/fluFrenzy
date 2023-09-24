""" ======================================================================================
Project Flu Frenzy
Students: Milo Savage-Webster and Akshat Koirala
Core Concepts of Computer Science
Professor: Joslenne Pena
Test File - only add code here that works in trial:Error.py
======================================================================================"""


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import turtle
import random
import matplotlib.pyplot as plt


class CharacterSelection(tk.Frame):
    """creates a character selection window with four characters for our game. User can pick any of the four character.
    User input will be passed to the Flu_Frenzy CLass which is the main game screen."""
    def __init__(self,master=None):
        """Initialize: character selection window and character buttons."""

        # the master parameter is used to connect our two classes together by giving it a reference to the same parent
        # widget (tk.Frame), allowing the classes to interact with each other and share information as needed.
        self.master=master
        self.master.title("In-Game-Characters")
        self.master.geometry("505x520")

        self.canvas=tk.Canvas(self.master, width=480, height=480, relief=tk.RIDGE)
        self.canvas.grid(row=1, column=1)
        self.image=tk.PhotoImage(file="charSel.png")
        self.canvas.create_image(0,0,image=self.image,anchor="nw")

        # Characters are placed on the canvas screen as canvas objects
        self.holyCat = tk.PhotoImage(file="holyCat.png")
        self.rect1 = self.canvas.create_image(48,114,image=self.holyCat,anchor="nw")
        self.fran = tk.PhotoImage(file="fran.png")
        self.rect2 = self.canvas.create_image(310,114,image=self.fran,anchor="nw")
        self.MC = tk.PhotoImage(file="MC.png")
        self.rect3 = self.canvas.create_image(60,320,image=self.MC,anchor="nw")
        self.bro = tk.PhotoImage(file="2D-bro.png")
        self.rect4 = self.canvas.create_image(330,320,image=self.bro,anchor="nw")

        # .tag_bind is like command but for Canvas objects (a shape, a text, or an image) displayed on the canvas.
        # lambda events for each canvas object i.e., in game characters
        self.canvas.tag_bind(self.rect1, "<ButtonPress-1>", lambda event: self.button_click("holyCat.png"))
        self.canvas.tag_bind(self.rect2, "<ButtonPress-1>", lambda event: self.button_click("fran.png"))
        self.canvas.tag_bind(self.rect3, "<ButtonPress-1>", lambda event: self.button_click("MC.png"))
        self.canvas.tag_bind(self.rect4, "<ButtonPress-1>", lambda event: self.button_click("2D-bro.png"))

    """Method to pass user input from this class to the next class"""
    def button_click(self, val):
        """shares the value of clicked image to Flu_Frenzy, closes the characterSelection window and starts Flu_Frenzy."""
        self.shared_val=val
        self.master.destroy()
        Flu_Frenzy(tk.Tk(),val)


class Flu_Frenzy(tk.Frame):
    """Our main game window with various objects and various methods"""
    def __init__(self, master=None, val=None):
        """Initialize: window, counters, imagefiles, canvas screen, and setsup canvas screen and labelframe screen"""
        self.value=val
        self.window = master
        self.window.title("Flu Frenzy")
        self.window.geometry("1400x550")

        """Setting up the display counters that need to be constantly updated in the left screen and on calcRo"""
        self.counterRnaught = 0
        self.counterPeopleInfected = 0
        self.switch_count = 0
        self.multiplicative_con = 0

        """All the photo files- 950X450 png"""
        self.mac_blueprint = tk.PhotoImage(file="blueprint_1.png")
        self.LC= tk.PhotoImage(file="LC.png")
        self.CC=tk.PhotoImage(file="CC.PNG")
        self.JW=tk.PhotoImage(file="JW.png")
        self.OlRi=tk.PhotoImage(file="OLRi.png")
        self.OM = tk.PhotoImage(file="OM.png")
        self.JWMSCS = tk.PhotoImage(file="JWMSCS.png")
        self.Carnegie= tk.PhotoImage(file="Carnegie.png")
        self.DeW= tk.PhotoImage(file="DeW.png")
        self.Chapel= tk.PhotoImage(file="Chapel.png")
        self.WeyH= tk.PhotoImage(file="WeyH.png")

        """Canvas"""
        self.canvaScreen = tk.LabelFrame(self.window, text="Game Screen", padx=5, pady=5, bg="beige", fg="black", relief=tk.RIDGE)
        self.canvaScreen.grid(row=1, column=2, padx=5, pady=5, columnspan=5, sticky=tk.E + tk.W + tk.N + tk.S)

        self.canvas = tk.Canvas(self.canvaScreen, width=910, height=410, relief=tk.RIDGE)
        self.canvas.grid(row=1, column=1, padx=5, pady=5, columnspan=5)
        self.canvas.create_image(-30, -30, image=self.mac_blueprint, anchor="nw") # used (-30,-30) to get building 2 inside the gamescreen
        self.image=tk.PhotoImage(file=self.value)
        self.item =self.canvas.create_image(200,230, image=self.image)

        """Notebook widget on the top left"""
        self.notebook_frame = tk.LabelFrame(self.window, text="Scenarios", padx=5, pady=5, bg="turquoise2", fg="black", relief=tk.RIDGE)
        self.notebook_frame.grid(row=1, column=1, sticky=tk.W + tk.N , columnspan=1)
        self.imageCat = tk.PhotoImage(file="palla.png")
        self.background_label = tk.Label(self.notebook_frame, image=self.imageCat)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.image = self.imageCat

        """All of my other widgets are created here."""
        self.create_notebook()
        self.create_widgets()

    def create_notebook(self):
        """Creates the notebook object with tabs and radiobuttons for the trivia"""
        self.notebook_label = ttk.Label(self.notebook_frame, text="Trivia")
        self.notebook_label.grid(row=2, column=1, sticky=tk.W, pady=3)

        self.notebook = ttk.Notebook(self.notebook_frame)
        self.notebook.grid(row=3, column=1, sticky=tk.E + tk.W + tk.N + tk.S, columnspan=2, pady=8)  # maybe pady=10

        # Three instances of the tk.IntVar class, used to store the value of the selected radio button in each of the
        # three tabs of the Notebook widget.
        self.tab1_rb_var = tk.IntVar(value=0)
        self.tab2_rb_var = tk.IntVar(value=0)
        self.tab3_rb_var = tk.IntVar(value=0)

        self.tab1 = tk.Frame(self.notebook)
        self.tab2 = tk.Frame(self.notebook)
        self.tab3 = tk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="How many\n people?", compound=tk.TOP)
        self.notebook.add(self.tab2, text="What floor?", compound=tk.TOP)
        self.notebook.add(self.tab3, text="# people you \n knew?", compound=tk.TOP)

        # Create Radio Buttons for each notebook tab using create_radioButtons
        self.create_radioButtons(self.tab1, "10-25 people", "25-40 people", "more than 40 people", 1, 2, 3, self.tab2_rb_var,self.tab2)
        self.create_radioButtons(self.tab2, "1", "2", "both 1 & 2", 1, 2, 3, self.tab3_rb_var, self.tab3)
        self.create_radioButtons(self.tab3, "1-5 bros", "5-10 bros", "more than 10 bros", 1, 2, 3, self.tab1_rb_var, self.tab1)

    def create_radioButtons(self, parent, a, b, c, a_val, b_val, c_val, var, next_tab):
        """Creates radiobuttons for our notebook and attribute a setofButtons to tk.IntVar values"""
        self.rb1 = tk.Radiobutton(parent, text=a, value=a_val, variable=var, command=lambda: self.delayed_tab_switch(next_tab))
        self.rb1.grid(row=1, column=1)
        self.rb2 = tk.Radiobutton(parent, text=b, value=b_val, variable=var, command=lambda: self.delayed_tab_switch(next_tab))
        self.rb2.grid(row=2, column=1)
        self.rb3 = tk.Radiobutton(parent, text=c, value=c_val, variable=var, command=lambda: self.delayed_tab_switch(next_tab))
        self.rb3.grid(row=3, column=1)


    def create_widgets(self):
        """All other Widgets on my grid"""
        # Create padding inside all internal frames
        self.window["padx"]= 10
        self.window["pady"] = 5

        """Time Entry Widget"""
        scale_label = tk.Label(self.notebook_frame, text="Time spent here \n (hours)")
        scale_label.grid(row=4, column=1, sticky=tk.W)
        self.scale = tk.Scale(self.notebook_frame, from_=0.0, to=10.0, orient=tk.HORIZONTAL, length=200)
        self.scale.grid(row=4, column=2, pady=4, sticky=tk.W)
        """Spacing- by adding a line"""
        sep = ttk.Separator(self.notebook_frame, orient=tk.HORIZONTAL)
        sep.grid(row=5, column=1, pady=2)
        """Collector"""
        entry_label = tk.Label(self.notebook_frame, text="Collector")
        entry_label.grid(row=7, column=1, sticky=tk.W )
        self.display_box = tk.Button(self.notebook_frame, text="Get Value", command=self.get_selected_value, height=4, width=20, fg="blue", font="Arial 13 bold")
        self.display_box.grid(row=7, column=2, sticky=tk.W)
        """Spacing- by adding a line"""
        sep = ttk.Separator(self.notebook_frame, orient=tk.HORIZONTAL)
        sep.grid(row=8, column=1, padx=15, pady=12)
        """Display the counter values"""
        self.Ro_label = ttk.Label(self.notebook_frame, text='RoValue: 0.00', font=('Arial', 20))
        self.Ro_label.grid(row=9, column=1, pady=8, sticky=tk.W)
        self.Ro_value = ttk.Progressbar(self.notebook_frame, orient='horizontal', length=200, mode='indeterminate')
        self.Ro_value.grid(row=10, column=1, pady=8, sticky=tk.W)
        self.Infected_label = ttk.Label(self.notebook_frame, text='# people infected:', font=('Arial', 14))
        self.Infected_label.grid(row=11, column=1, pady=8, sticky=tk.W)
        self.Infected_value = ttk.Progressbar(self.notebook_frame, orient='horizontal', length=200, mode='indeterminate')
        self.Infected_value.grid(row=12, column=1, pady=8, sticky=tk.W)
        self.quit_button=tk.Button(self.notebook_frame, text="Quit", bg="white", fg="red")
        self.quit_button.grid(row=13, column=2, sticky=tk.E+tk.S)
        self.quit_button.bind("<ButtonPress-1>", self.quit_window)

        # Canvas Buttons

        self.button_1=tk.Button(self.canvaScreen,text="1. Leonard Center", padx=5, pady=2, bg="grey", fg="black")
        self.button_1.grid(row=2,column=1, columnspan=1)
        self.button_1.bind("<ButtonPress-1>", self.gotoLC)
        self.button_2 = tk.Button(self.canvaScreen, text="2. Olin Rice", padx=5, pady=2, bg="grey", fg="black")
        self.button_2.grid(row=3, column=1, columnspan=1)
        self.button_2.bind("<ButtonPress-1>", self.gotoOlRi)
        self.button_3 = tk.Button(self.canvaScreen, text="3. JWall Art", padx=5, pady=2, bg="grey", fg="black")
        self.button_3.grid(row=2,column=2, columnspan=1 )
        self.button_3.bind("<ButtonPress-1>", self.gotoJW)
        self.button_5 = tk.Button(self.canvaScreen, text="5. Carnegie", padx=5, pady=2, bg="grey", fg="black")
        self.button_5.grid(row=3, column=5, columnspan=1)
        self.button_5.bind("<ButtonPress-1>", self.gotoCarnegie)
        self.button_6 = tk.Button(self.canvaScreen, text="6. Old Main", padx=5, pady=2, bg="grey", fg="black")
        self.button_6.grid(row=2,column=5, columnspan=1)
        self.button_6.bind("<ButtonPress-1>", self.gotoOM)
        self.button_7 = tk.Button(self.canvaScreen, text="7. DeWitt Wallace Library", padx=5, pady=2, bg="grey", fg="black")
        self.button_7.grid(row=2,column=4, columnspan=1)
        self.button_7.bind("<ButtonPress-1>", self.gotoDeW)
        self.button_8 = tk.Button(self.canvaScreen, text="8. CampusCenter", padx=5, pady=2, bg="grey", fg="black")
        self.button_8.grid(row=3, column=4, columnspan=1)
        self.button_8.bind("<ButtonPress-1>", self.gotoCC)
        self.button_9 = tk.Button(self.canvaScreen, text="9. Chapel", padx=5, pady=2, bg="grey", fg="black")
        self.button_9.grid(row=3, column=3, columnspan=1)
        self.button_9.bind("<ButtonPress-1>", self.gotoChapel)
        self.button_10 = tk.Button(self.canvaScreen, text="10. Weyerheuser", padx=5, pady=2, bg="grey", fg="black")
        self.button_10.grid(row=3, column=2, columnspan=1)
        self.button_10.bind("<ButtonPress-1>", self.gotoWeyH)
        self.button_14 = tk.Button(self.canvaScreen, text="14. JWall MSCS", padx=5, pady=2, bg="grey", fg="black")
        self.button_14.grid(row=2,column=3, columnspan=1)
        self.button_14.bind("<ButtonPress-1>", self.gotoJWMSCS)

    # Methods

    def on_progressbar_moved(self):
        """Increment the progress bar value by a certain amount when the user types in the entry widget"""
        self.Ro_value.step(1)
        self.Infected_value.step(1)

    def on_focus_out(self):
        """Get the value entered by the user and display it in the Ro label when the user is not typing"""
        Ro= '{:.3g}'.format(self.counterRnaught)
        infected = '{:.3g}'.format(self.counterPeopleInfected)
        self.Ro_label.config(text='RoValue: {}'.format(Ro))
        self.Infected_label.config(text='# people infected: {}'.format(infected))
        if self.multiplicative_con==1:
            tk.messagebox.showinfo("Information", 'What is R-naught?\n R-naught (R0) is a value that can be calculated for communicable diseases. It represents, on average, the number of people that a single infected person can be expected to transmit that disease to. In other words, it is a calculation of the average “spreadability” of an infectious disease.')

    def get_selected_value(self):
        """Get the selected radio button value and display it in the display box"""
        tab1_value = self.tab1_rb_var.get()
        tab2_value = self.tab2_rb_var.get()
        tab3_value = self.tab3_rb_var.get()
        scale_value = self.scale.get()
        display_text = f"Tab 1 Value: {tab2_value}\nTab 2 Value: {tab3_value}\nTab 3 Value: {tab1_value}\nScale Value: {scale_value}"
        self.display_box.configure(text=display_text)
        self.calcRo()
        self.on_focus_out()
        self.reset_canvas()

    def delayed_tab_switch(self, next_tab):
        """Switch notebook tabs with a half-second delay"""
        if self.switch_count < 2:
            self.window.after(500, lambda: self.notebook.select(next_tab))
            self.switch_count += 1

    def reset_canvas(self):
        """Resets the canvas to blueprint and In-Game-Char after inputs have been given."""
        self.canvas.delete("all")
        self.canvas.create_image(-30, -30, image=self.mac_blueprint, anchor="nw")
        self.item = self.canvas.create_image(200, 230, image=self.image)

    def reset_values(self):
        """resets values for input widgets."""
        self.scale.set(0)
        self.tab1_rb_var.set(0)
        self.tab2_rb_var.set(0)
        self.tab3_rb_var.set(0)
        self.switch_count=0
        self.notebook.select(0)
        self.display_box.configure(text="Get Value")

    def gotoLC(self, event):
        """Takes the In-Game-Character to Leonard Center and prompts the user to answer a Trivia."""
        self.on_progressbar_moved()
        self.reset_values()
        self.canvas.move(self.item, 440,-110)
        self.canvas.after(1500, lambda: self.canvas.create_image(-30, -30, image=self.LC, anchor="nw"))
        self.canvas.after(2500, lambda: self.canvas.create_image(110, 360, image=self.image))
        self.canvas.after(3000, lambda: tk.messagebox.showinfo("Information", "Please answer the Trivia on your left before going to next building."))

    def gotoCC(self, event):
        """Takes the In-Game-Character to Campus Center and prompts the user to answer a Trivia."""
        self.on_progressbar_moved()
        self.reset_values()
        self.canvas.move(self.item, -25,-190)
        self.canvas.after(1500, lambda: self.canvas.create_image(-30, -30, image=self.CC, anchor="nw"))
        self.canvas.after(2500, lambda: self.canvas.create_image(430, 350, image=self.image))
        self.canvas.after(3000, lambda: tk.messagebox.showinfo("Information", "Please answer the Trivia on your left before going to next building."))

    def gotoJW(self, event):
        """Takes the In-Game-Character to JWall and prompts the user to answer a Trivia."""
        self.on_progressbar_moved()
        self.reset_values()
        self.canvas.move(self.item, 400, 120)
        self.canvas.after(1500, lambda: self.canvas.create_image(-30, -30, image=self.JW, anchor = "nw"))
        self.canvas.after(2500, lambda: self.canvas.create_image(240, 370, image=self.image))
        self.canvas.after(3000, lambda: tk.messagebox.showinfo("Information", "Please answer the Trivia on your left before going to next building."))

    def gotoOlRi(self, event):
        """Takes the In-Game-Character to Olin Rice and prompts the user to answer a Trivia."""
        self.on_progressbar_moved()
        self.reset_values()
        self.canvas.move(self.item, 400, 120)
        self.canvas.after(1500, lambda: self.canvas.create_image(-30, -30, image=self.OlRi, anchor = "nw"))
        self.canvas.after(2500, lambda: self.canvas.create_image(610, 370, image=self.image))
        self.canvas.after(3000, lambda: tk.messagebox.showinfo("Information", "Please answer the Trivia on your left before going to next building."))

    def gotoOM(self, event):
        """Takes the In-Game-Character to Old Main and prompts the user to answer a Trivia."""
        self.on_progressbar_moved()
        self.reset_values()
        self.canvas.move(self.item, 400, 120)
        self.canvas.after(1500, lambda: self.canvas.create_image(-30, -30, image=self.OM, anchor = "nw"))
        self.canvas.after(2500, lambda: self.canvas.create_image(530, 370, image=self.image))
        self.canvas.after(3000, lambda: tk.messagebox.showinfo("Information", "Please answer the Trivia on your left before going to next building."))

    def gotoJWMSCS(self, event):
        """Takes the In-Game-Character to JWall MSCS block and prompts the user to answer a Trivia."""
        self.on_progressbar_moved()
        self.reset_values()
        self.canvas.move(self.item, 520, 110)
        self.canvas.after(1500, lambda: self.canvas.create_image(-30, -30, image=self.JWMSCS, anchor = "nw"))
        self.canvas.after(2500, lambda: self.canvas.create_image(530, 370, image=self.image))
        self.canvas.after(3000, lambda: tk.messagebox.showinfo("Information", "Please answer the Trivia on your left before going to next building."))

    def gotoCarnegie(self, event):
        """Takes the In-Game-Character to Carnegie and prompts the user to answer a Trivia."""
        self.on_progressbar_moved()
        self.reset_values()
        self.canvas.move(self.item, 150, 100)
        self.canvas.after(1500, lambda: self.canvas.create_image(-30, -30, image=self.Carnegie, anchor = "nw"))
        self.canvas.after(2500, lambda: self.canvas.create_image(300, 270, image=self.image))
        self.canvas.after(3000, lambda: tk.messagebox.showinfo("Information", "Please answer the Trivia on your left before going to next building."))

    def gotoDeW(self, event):
        """Takes the In-Game-Character to DeWitt Wallace Library and prompts the user to answer a Trivia."""
        self.on_progressbar_moved()
        self.reset_values()
        self.canvas.move(self.item, 200, -90)
        self.canvas.after(1500, lambda: self.canvas.create_image(-30, -30, image=self.DeW, anchor = "nw"))
        self.canvas.after(2500, lambda: self.canvas.create_image(430, 180, image=self.image))
        self.canvas.after(3000, lambda: tk.messagebox.showinfo("Information", "Please answer the Trivia on your left before going to next building."))

    def gotoChapel(self, event):
        """Takes the In-Game-Character to DeWitt Wallace Library and prompts the user to answer a Trivia."""
        self.on_progressbar_moved()
        self.reset_values()
        self.canvas.move(self.item, -105, 0)
        self.canvas.after(1500, lambda: self.canvas.create_image(-30, -30, image=self.Chapel, anchor = "nw"))
        self.canvas.after(2500, lambda: self.canvas.create_image(430, 370, image=self.image))
        self.canvas.after(3000, lambda: tk.messagebox.showinfo("Information", "Please answer the Trivia on your left before going to next building."))

    def gotoWeyH(self, event):
        """Takes the In-Game-Character to DeWitt Wallace Library and prompts the user to answer a Trivia."""
        self.on_progressbar_moved()
        self.reset_values()
        self.canvas.move(self.item, -25, 90)
        self.canvas.after(1500, lambda: self.canvas.create_image(-30, -30, image=self.WeyH, anchor = "nw"))
        self.canvas.after(2500, lambda: self.canvas.create_image(730, 370, image=self.image))
        self.canvas.after(3000, lambda: tk.messagebox.showinfo("Information", "Please answer the Trivia on your left before going to next building."))

    def calcRo(self):
        """Calculates the Ro value and the # of people infected from user input values"""
        # Getting the input values
        label_text = str(self.display_box['text'])
        list=label_text.split("\n")
        # Formula for R0 = (transmission rate x duration of infectiousness x contact rate) / recovery rate
        rb1_val=int(list[0][13])
        rb2_val=int(list[1][13])
        rb3_val=int(list[2][13])
        scale_val=int(list[3][13:])
        # If operators to sort out input values
        if rb1_val==1 or rb1_val==2:
            peeps=random.randint(10,21)
        elif rb1_val==3:
            peeps=random.randint(31,51)
        if rb2_val==1 or rb2_val==2:
            floor_value=1
        elif rb2_val==3:
            floor_value=2
        if rb3_val==1 or rb3_val==2:
            bro_val=random.randint(4,8)
        elif rb3_val==3:
            bro_val=random.randint(8,15)
        transmission_rate=peeps/20 + floor_value/2
        if transmission_rate>2.5:
            transmission_rate=2.5
        contact_rate=(peeps+(bro_val*(scale_val)))/24
        self.counterRnaught=transmission_rate*contact_rate*(scale_val)/5+0.2*self.multiplicative_con
        self.counterPeopleInfected=self.counterRnaught*peeps/4+0.5*self.multiplicative_con
        self.multiplicative_con+=1

    def quit_window(self, event):
        """Close the game when quit button is called"""
        self.multiplicative_con = 0
        # Some function to display a graph - Create
        self.window.destroy()
        self.create_graph()

    def create_graph(self):
        """Creates a personal flu spread graph from the game simulation"""
        m = self.counterRnaught
        c = self.counterPeopleInfected
        x = range(1, 100)
        y = [m * xi + c for xi in x]
        fig = plt.figure(figsize=(8, 6))
        plt.plot(x, y)
        plt.xlabel('Hours')
        plt.ylabel('Number of Macalester students catching flu')
        plt.title('FluFrenzy Graph for individuals\n Your Ro value is {:.3g} and The #people infected is {:.3g}'.format(m,c), fontsize=10)
        plt.suptitle('The total number of sick MAC students, due to you, is {:.3g}'.format(m*50+c),fontsize=10, fontweight='bold', y=0.03)
        # Show the graph
        plt.show()
        tk.messagebox.showinfo("Information", "See you next time or maybeNot!! STAY INDOORS... Ciao")

user_reply=tk.messagebox.askokcancel("Information", "Welcome to Flu-Frenzy!!!\n\nHow to play the game?\n\n1. Firstly, start on the right screen, use buttons to navigate through different buildings\n\n2. Shortly, a messagebox will prompt you to input on the left. Don't forget to get your inputs from the collector.\n\n3. Once you quit Flu Frenzy will generate your causality graph based on your gameplay.\n \nLet's play Flu Frenzy :) 0.0")
if user_reply==True:
    if __name__=='__main__':
        root = tk.Tk()
        app = CharacterSelection(root)
        root.mainloop()
