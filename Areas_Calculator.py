import Default_Components

class Areas_Calculator(Default_Components.BasicCalculator):
    def __init__(self, parent: Default_Components.ctk, area_to_calculate: str) -> None:
        super().__init__(parent)
        
        self.num_textboxes = 1
        self.nums_and_operations_frame.place(relx = 0.0, rely = 0.5, relwidth = 1, relheight = 0.5)
        self.results_frame.place(relx = 0.0, rely = 0.0, relwidth = 1, relheight = 0.5)       

        #   Animated Slide Panels
        #       Settings Panel
        self.settings_panel = Default_Components.SettingsPanel(self.window, -0.5, 0.46, [self.nums_and_operations_frame, self.results_frame])
        #       Main Slide Panel
        self.slide_panel = Default_Components.SlidePanelBackAndForth(self.window, -0.5, 0.1, [self.nums_and_operations_frame, self.results_frame], self.settings_panel.animate)
        self.slide_panel.settings_button.configure(hover_color = '#a2a2a2')
        #       Shape Areas panel
        self.shape_areas_panel = Default_Components.SlidePanelUpAndDown(self.window, -0.3, 0.3, [self.nums_and_operations_frame, self.results_frame])
    
        self.settings_panel.switch1.configure(command = self.manage_switches)
        self.settings_panel.switch2.configure(command = self.manage_switches)
        self.settings_panel.switch3.configure(command = self.manage_switches)

        #Buttons
        # Slide Panel Button
        self.slide_panel_button = Default_Components.ctk.CTkButton(self.window, text = '', 
        width=50,height=40,command = self.manage_brother_panels, 
        image=Default_Components.ctk.CTkImage(Default_Components.Image.open('sidebar_image.png')), fg_color='#7c87e7', hover_color='#6B78D3')
        self.slide_panel_button.lift(self.slide_panel)
        self.slide_panel_button.place(anchor = 'nw')
        # Bind the disable and enable functions to the slide panel button
        self.slide_panel_button.bind('<Button-1>', lambda event: self.manage_buttons(event) if self.slide_panel.is_active else self.manage_buttons(event))
        # Shape button
        self.shape_button = Default_Components.ctk.CTkButton(master=self.window, text='\u2193', command=self.shape_areas_panel.animate, font=self.my_font, width= 0.1, height  =0.1)
        self.shape_button.lift(self.shape_areas_panel)
        self.shape_button.place(relx = 0.5, rely = 0.0)
        self.shape_button.bind('<Button-1>', lambda event: self.manage_buttons(event) if self.shape_areas_panel.is_active else self.manage_buttons(event))

        # Set the weight for each row and column
        for i in range(4):
            self.nums_and_operations_frame.grid_rowconfigure(i, weight=1)
            for j in range(3):
                self.nums_and_operations_frame.grid_columnconfigure(j, weight=1)

        for i in range(len(self.operation_buttons)):
         self.operation_buttons[i].destroy()

        self.number_buttons[10].destroy()

        index = 0
        for i in range(3):
            for j in range(3):
                 if self.number_buttons[index] != None:
                    self.number_buttons[index].configure(command = lambda x=self.number_buttons[index].cget("text"): self.update_current_operation_statement(str(x)))
                    self.number_buttons[index].grid(row=i,column=j, padx=1, pady=1, sticky='nsew')
                 index+=1
        self.number_buttons[9].configure(command = lambda x=self.number_buttons[index].cget("text"): self.update_current_operation_statement(str(x)))
        self.number_buttons[9].grid(row=3,column=0, padx=1, pady=1, sticky='nsew')
        self.number_buttons[11].configure(command = lambda x=self.number_buttons[index].cget("text"): self.update_current_operation_statement(str(x)))
        self.number_buttons[11].grid(row=3,column=1, padx=1, pady=1, sticky='nsew')
        
        # Create the textboxes according the area to calculate
        if area_to_calculate == "Circle":
            self.canvas = Default_Components.ctk.CTkCanvas(master=self.results_frame, bg = 'black')
            self.canvas.place(relx = 0.05, rely = 0.3, relwidth = 0.5, relheight = 0.6)
            self.canvas.bind('<Configure>', self.draw_circle)
            self.formula_label = Default_Components.ctk.CTkLabel(master=self.results_frame, text = '\u03C0 x r^2', font=self.my_font, text_color = 'white')
            self.formula_label.place(relx = 0.7, rely = 0.3, relwidth = 0.2,relheight = 0.2)
            self.r_label = Default_Components.ctk.CTkLabel(master=self.results_frame, text="r=", font=self.my_font, text_color='white')
            self.r_label.place(relx=0.65, rely=0.45, relwidth=0.05, relheight=0.18)
            self.textbox_1 = Default_Components.ctk.CTkTextbox(master=self.results_frame,font=self.my_font)
            self.textbox_1.insert(1.0, '0')
            self.textbox_1.place(relx = 0.7, rely = 0.45, relwidth = 0.2,relheight = 0.18)
        elif area_to_calculate == "Square":
            self.canvas = Default_Components.ctk.CTkCanvas(master=self.results_frame, bg = 'black')
            self.canvas.place(relx = 0.1, rely = 0.3, relwidth = 0.5, relheight = 0.6)
            self.canvas.bind('<Configure>', self.draw_square)
            self.formula_label = Default_Components.ctk.CTkLabel(master=self.results_frame, text = 'b^2', font=self.my_font, text_color = 'white')
            self.formula_label.place(relx = 0.7, rely = 0.3, relwidth = 0.2,relheight = 0.2)
            self.base_label = Default_Components.ctk.CTkLabel(master=self.results_frame, text="b=", font=self.my_font, text_color='white')
            self.base_label.place(relx=0.6, rely=0.45, relwidth=0.1, relheight=0.2)
            self.textbox_1 = Default_Components.ctk.CTkTextbox(master=self.results_frame,font=self.my_font)
            self.textbox_1.insert(1.0, '0')
            self.textbox_1.place(relx = 0.7, rely = 0.45, relwidth = 0.2,relheight = 0.18)
        elif area_to_calculate == "Triangle":
            self.canvas = Default_Components.ctk.CTkCanvas(master=self.results_frame, bg='black')
            self.canvas.place(relx=0.1, rely=0.3, relwidth=0.5, relheight=0.6)
            self.canvas.bind('<Configure>', self.draw_triangle)
            self.formula_label = Default_Components.ctk.CTkLabel(master=self.results_frame, text = '(b x h)/2', font=self.my_font, text_color = 'white')
            self.formula_label.place(relx = 0.65, rely = 0.15, relwidth = 0.3,relheight = 0.3)
            self.textbox_1 = Default_Components.ctk.CTkTextbox(master=self.results_frame,font=self.my_font)
            self.textbox_1.insert(1.0, '0')
            self.textbox_1.place(relx = 0.7, rely = 0.35, relwidth = 0.2,relheight = 0.18)
            self.textbox_2 = Default_Components.ctk.CTkTextbox(master=self.results_frame,font=self.my_font)
            self.textbox_2.insert(1.0, '0')
            self.base_label = Default_Components.ctk.CTkLabel(master=self.results_frame, text="b=", font=self.my_font, text_color='white')
            self.base_label.place(relx=0.6, rely=0.35, relwidth=0.1, relheight=0.2)
            self.height_label = Default_Components.ctk.CTkLabel(master=self.results_frame, text="h=", font=self.my_font, text_color='white')
            self.height_label.place(relx=0.6, rely=0.55, relwidth=0.1, relheight=0.2)
            self.textbox_2.place(relx = 0.7, rely = 0.55, relwidth = 0.2,relheight = 0.18)

        # Link the validate_dot function to the textboxes
        self.textbox_1.bind("<Key>", self.validate_dot)
        self.textbox_2.bind("<Key>", self.validate_dot)


        self.current_operation_statement_label.place(relx=0.95, rely=0.9, anchor='se')

        #The app starts with the Blue theme by default (later changing to the OS theme)
        self.settings_panel.switch3.toggle()

    def change_application_theme(self, value: int):
        '''Method for changing the application theme according to the value,\n
        which is given by pressing one of the CtkSwitches'''

        #Variables for assgination of each component's colors
        fg_color_window_frame_panel = fg_color_nums = fg_color_operations = fg_color_backspace= ''
        fg_color_divider = fg_color_radio_buttons = fg_color_slide_panel_button = ''
        fg_color_setting_button = fg_color_slide_panels =''
        fg_color_results_frame_panel =''

        hv_color_nums = hv_color_operations = hv_color_backspace = ''
        hv_color_settings_button = ''

        bg_color_nums = bg_color_operations = ''

        text_color = text_color_settings = ''    

        if value == 1:
            fg_color_window_frame_panel = '#f6f6f6'
            fg_color_setting_button = fg_color_radio_buttons = fg_color_slide_panels = fg_color_window_frame_panel
            fg_color_results_frame_panel = fg_color_window_frame_panel
            fg_color_nums = '#fafbfd'
            fg_color_slide_panel_button = '#FFFFFF'
            fg_color_operations = '#f8f8ff'
            fg_color_backspace = '#e3f2fd'
            fg_color_divider = '#000000'
            hv_color_nums = '#d4d1d0'
            hv_color_operations = '#f4f4f4'
            hv_color_backspace = '#f0f8ff'
            hv_color_settings_button = hv_color_nums
            bg_color_nums = '#FFFFFF'
            bg_color_operations = '#FFFFFF'
            text_color_settings = text_color = 'black'
        elif value == 2:
            fg_color_window_frame_panel = '#000000'
            fg_color_radio_buttons = fg_color_slide_panels = fg_color_window_frame_panel
            fg_color_results_frame_panel = fg_color_window_frame_panel
            fg_color_setting_button = '#C0C0C0'  
            fg_color_nums = '#000000'
            fg_color_slide_panel_button = '#d0d0d0'
            fg_color_operations = '#c35831'
            fg_color_backspace = '#f8f8ff'
            fg_color_divider = '#FFFFFF'
            hv_color_settings_button = hv_color_nums
            hv_color_operations = '#c57360'
            hv_color_nums = '#191919'
            hv_color_backspace = '#d4d1d0'
            bg_color_nums = '#000000'
            bg_color_operations = '#000000'
            text_color = 'white'
            text_color_settings = 'white'
        elif value == 3:
            fg_color_window_frame_panel = "#292929"  
            fg_color_slide_panels = ['gray86', 'gray17']
            fg_color_radio_buttons = '#292929'
            fg_color_nums = '#7c87e7'
            fg_color_slide_panel_button = '#7c87e7'
            fg_color_operations = '#2a4993'
            fg_color_backspace = '#2a4993'
            fg_color_divider = '#000000'
            fg_color_setting_button = '#C0C0C0'   
            fg_color_results_frame_panel = '#292929'
            hv_color_nums = '#6B78D3'
            hv_color_operations = '#233F83'
            hv_color_backspace = '#233F83'
            hv_color_settings_button = '#a2a2a2'
            bg_color_nums = '#292929'
            bg_color_operations = '#292929'
            text_color = 'white'
            text_color_settings = 'black'

        self.window.configure(fg_color=fg_color_window_frame_panel)
        self.nums_and_operations_frame.configure(fg_color=fg_color_window_frame_panel)
        self.results_frame.configure(fg_color=fg_color_results_frame_panel)
        self.current_operation_statement_label.configure( text_color = text_color)
        self.operations_history_statement_label.configure( text_color = text_color)
        for i in range(len(self.number_buttons)):
            if i != 10:
                self.number_buttons[i].configure(fg_color=fg_color_nums, hover_color=hv_color_nums, bg_color = bg_color_nums, text_color = text_color)
        self.slide_panel.configure(fg_color = fg_color_slide_panels)
        self.slide_panel_button.configure(fg_color=fg_color_slide_panel_button, hover_color=hv_color_nums)
        self.slide_panel.areas_calculator_button.configure(fg_color = fg_color_slide_panels, hover_color = hv_color_settings_button, text_color = text_color_settings, bg_color = text_color)
        self.slide_panel.settings_button.configure(fg_color = fg_color_setting_button, hover_color = hv_color_settings_button, text_color = text_color_settings)
        self.slide_panel.divider.configure(fg_color = fg_color_divider)
        self.settings_panel.configure(fg_color=fg_color_slide_panels)
        self.settings_panel.settings_label.configure(text_color = text_color_settings)
        self.settings_panel.themes_label.configure(text_color = text_color_settings)
        self.settings_panel.divider.configure(fg_color=fg_color_divider)
        self.settings_panel.switch1.configure(fg_color=fg_color_radio_buttons, text_color = text_color_settings)
        self.settings_panel.switch2.configure(fg_color=fg_color_radio_buttons, text_color = text_color_settings)
        self.settings_panel.switch3.configure(fg_color=fg_color_radio_buttons, text_color = text_color_settings)    

    def manage_buttons(self,event) -> None:
        '''Disable or enable the buttons when the slide panel is active'''
        if not self.side_panel_active:
            for i in range(len(self.number_buttons)):
                if i != 10:
                    self.number_buttons[i].configure(state='disabled')            
            self.textbox_1.configure(state='disabled')
            self.textbox_2.configure(state='disabled')
            self.side_panel_active = True
        else:
            for i in range(len(self.number_buttons)):
                if i != 10:
                    self.number_buttons[i].configure(state='normal')        
            self.textbox_1.configure(state='normal')
            self.textbox_2.configure(state='normal')
            self.side_panel_active = False
    
    def manage_area_to_calculate(self, area_to_calculate: str) -> None:
        '''Method for managing the view according to the area to calculate'''

        # Remove all widgets from the window
        for widget in self.window.winfo_children():
            widget.destroy()

        if area_to_calculate == "Circle":
            self.areas_calculator = Areas_Calculator(self.window, "Circle")

    def update_current_operation_statement(self,stmt: str) -> None:
        '''Updates the current operation statement label with the given statement
        \nIt operates with the given statement and the current operation statement'''

        # Obtain the focused widget
        focused_widget = self.window.focus_get()

        # Prove if the focused widget is a textbox
        if focused_widget == self.textbox_1:
            if stmt == ".":
                if "." in self.textbox_1.get(1.0, 'end-1c'):
                    return None
                else:
                    self.textbox_1.insert('end', stmt)
            elif stmt in "1234567890":
                if self.textbox_1.get(1.0, 'end-1c') == "0":
                    self.textbox_1.delete(1.0, 'end')
                    self.textbox_1.insert('end', stmt)
                else:
                    self.textbox_1.insert('end', stmt)
        elif focused_widget == self.textbox_2:
            if stmt == ".":
                if "." in self.textbox_1.get(1.0, 'end-1c'):
                    return None
                else:
                    self.textbox_1.insert('end', stmt)
            elif stmt in "1234567890":
                if self.textbox_1.get(1.0, 'end-1c') == "0":
                    self.textbox_1.delete(1.0, 'end')
                    self.textbox_1.insert('end', stmt)
                else:
                    self.textbox_1.insert('end', stmt)
        else:
            print()
            #Logic for a messagebox

        #Update the current operation statement label
        self.current_operation_statement_label.configure(textvariable=self.current_operation_statement)

    def draw_circle(self,event) -> None:
        '''Method for drawing a circle in the canvas'''
        # Delete all the elements in the canvas
        self.canvas.delete('all')

        # Obtain the width and height of the canvas
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Draw the circle
        self.canvas.create_oval(0, 0, width, height, fill='white')

    def draw_square(self, event) -> None:
        '''Method for drawing a square in the canvas'''
        # Delete all the elements in the canvas
        self.canvas.delete('all')

        # Obtain the width and height of the canvas
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Draw the full square
        self.canvas.create_rectangle(0, 0, width, height)

        # Draw a smaller square inside the original square
        # This will fill a portion of the original square with white
        self.canvas.create_rectangle(width*0.15, height*0.15, width*0.85, height*0.85, fill='white')

    def draw_triangle(self, event):

        # Delete all the elements in the canvas
        self.canvas.delete('all')

        # Obtain the width and height of the canvas
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Draw the triangle
        self.canvas.create_polygon([(width / 2, 0), (0, height), (width, height)], fill='white')

    def validate_dot(self,event):
        # Obtaining the current text in the textbox
        current_text = event.widget.get("1.0", 'end-1c')

        # Verify if the dot is already in the textbox
        if event.char == "." and "." in current_text:
            return None