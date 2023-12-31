from Default_View import * 

class Standard_Calculator_View(Default_View):
    
    def __init__(self):
        super().__init__()
        #Declarations of the frames to be used to set the respective components
        self.result_frame = Frame(self.root,relief="solid",borderwidth=2)
        self.result_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.operations_frame = Frame(self.root,relief="solid",highlightthickness=1)
        self.operations_frame.pack(side=RIGHT,expand=True, fill=BOTH)
        self.operations_frame.grid_rowconfigure(0, weight=1)
        self.operations_frame.grid_columnconfigure(0, weight=1)

        self.operations_frame_advnc = Frame(self.root,relief="solid",highlightthickness=1)
        self.operations_frame_advnc.pack(side=LEFT,expand=True, fill=BOTH)
        self.operations_frame_advnc.grid_rowconfigure(0, weight=1)
        self.operations_frame_advnc.grid_columnconfigure(0, weight=1)

        self.numbers_frame = Frame(self.root,relief="solid", highlightthickness=1)
        self.numbers_frame.pack(side=BOTTOM,expand=True,fill=BOTH)
        self.numbers_frame.grid_rowconfigure(0, weight=1)
        self.numbers_frame.grid_columnconfigure(0, weight=1)

        #Labels in which the operations and their history will be represented
        self.operations_history_label = Label(self.result_frame, font=("Curier 10",25))
        self.operations_history_label.pack(anchor="e")

        self.operations_label = Label(self.result_frame,font=("Curier 10",30),height=2)
        self.operations_label.pack(anchor="e")

        #Buttons for basic arithmetical operations
        self.division_button = Button(self.operations_frame,text="/", font=("Curier 10", 15),height=2,width=8)
        self.division_button.grid(row=0, column=0, sticky="nsew")

        self.multiplication_button = Button(self.operations_frame,text="x", font=("Curier 10", 15),height=2,width=8)
        self.multiplication_button.grid(row=1, column=0, sticky="nsew")

        self.substraction_button = Button(self.operations_frame,text="-", font=("Curier 10", 15),height=2,width=8)
        self.substraction_button.grid(row=2, column=0, sticky="nsew")

        self.sum_button = Button(self.operations_frame,text="+", font=("Curier 10", 15),height=2,width=8)
        self.sum_button.grid(row=3, column=0, sticky="nsew")

        self.result_button = Button(self.operations_frame,text="=", font=("Curier 10",15),height=2,width=8)
        self.result_button.grid(row=4, column=0, sticky="nsew")

        self.porcentage_button = Button(self.operations_frame_advnc, text="%", font=("Curier 10", 15),height=2,width=8)
        self.porcentage_button.grid(row=0, column=0, sticky="nsew")

        self.power_button = Button(self.operations_frame_advnc,text="x^n", font=("Curier 10", 15),height=2,width=8)
        self.power_button.grid(row=1, column=0, sticky="nsew")

        self.sqrt_button = Button(self.operations_frame_advnc, text="\u221A", font=("Curier 10", 15),height=2,width=8)
        self.sqrt_button.grid(row=2, column=0, sticky="nsew")

        #Number buttons
        self.zero_button = Button(self.numbers_frame, text="0", font=("Curier 10", 15),height=2,width=8)
        self.zero_button.grid(row=4, column=0, sticky='nsew')

        self.double_zero_button = Button(self.numbers_frame, text="00", font=("Curier 10", 15),height=2,width=8)
        self.double_zero_button.grid(row=4, column=1, sticky='nsew')

        self.decimal_button = Button(self.numbers_frame, text=".", font=("Curier 10", 15),height=2,width=8)
        self.decimal_button.grid(row=4,column=2, sticky='nsew')

        self.one_button = Button(self.numbers_frame, text="1", font=("Curier 10", 15),height=2,width=8)
        self.one_button.grid(row=3, column=0, sticky='nsew')

        self.two_button = Button(self.numbers_frame, text="2", font=("Curier 10", 15),height=2,width=8)
        self.two_button.grid(row=3, column=1, sticky='nsew')

        self.three_button = Button(self.numbers_frame, text="3", font=("Curier 10", 15),height=2,width=8)
        self.three_button.grid(row=3, column=2, sticky='nsew')

        self.four_button = Button(self.numbers_frame, text="4", font=("Curier 10", 15),height=2,width=8)
        self.four_button.grid(row=2, column=0, sticky='nsew')

        self.five_button = Button(self.numbers_frame, text="5", font=("Curier 10", 15),height=2,width=8)
        self.five_button.grid(row=2, column=1, sticky='nsew')

        self.six_button = Button(self.numbers_frame, text="6", font=("Curier 10", 15),height=2,width=8)
        self.six_button.grid(row=2, column=2, sticky='nsew')

        self.seven_button = Button(self.numbers_frame, text="7", font=("Curier 10", 15),height=2,width=8)
        self.seven_button.grid(row=1, column=0, sticky='nsew')

        self.eight_button = Button(self.numbers_frame, text="8", font=("Curier 10", 15),height=2,width=8)
        self.eight_button.grid(row=1, column=1, sticky='nsew')

        self.nine_button = Button(self.numbers_frame, text="9", font=("Curier 10", 15),height=2,width=8)
        self.nine_button.grid(row=1, column=2, sticky='nsew')

        self.pi_button = Button(self.numbers_frame,text="\u03C0", font=("Curier 10", 15),height=2,width=8)
        self.pi_button.grid(row=0, column=0, sticky='nsew')

        self.euler_button = Button(self.numbers_frame,text="e", font=("Curier 10", 15),height=2,width=8)
        self.euler_button.grid(row=0, column=1, sticky='nsew')

        #boton c/ce (clear)
        self.clean_button = Button(self.numbers_frame, text="C", font=("Curier 10", 15),height=2,width=8)
        self.clean_button.grid(row=0,column=2, sticky='nsew')