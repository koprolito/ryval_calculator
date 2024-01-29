import customtkinter as ctk
from PIL import Image, ImageTk
import Operation


class SlidePanel(ctk.CTkFrame):
	def __init__(self, parent:ctk, start_pos:float, end_pos:float, above_these_frames: list,
			  settings_button_command: callable = None):
		super().__init__(master = parent)

		# general attributes 
		self.start_pos = start_pos - 0.04
		self.end_pos = end_pos + 0.03
		self.width = abs(start_pos + end_pos) - 0.03
		self.aboabove_these_frames = above_these_frames

		# animation logic
		self.pos = self.start_pos
		self.in_start_pos = True

		# divider
		self.divider = ctk.CTkFrame(master=self, fg_color="black", height=2, width=1200)  # Change color and height as needed
		self.divider.place(relx = -0.5, rely = 0.90)  # Change padding as needed

		#Settings button
		self.settings_button = SettingsButton(self, text = "Settings",  
			relx = 0, rely = 0.905, height = 65, 
			relwidth = 1, fg_color = "#C0C0C0", 
            text_color="black", 
            image=ctk.CTkImage(Image.open('settings_image.png')), 
			command=settings_button_command)
		self.settings_button.configure(corner_radius=0)

		# Areas calculator button
		self.areas_calculator_button = ctk.CTkButton(master=self, text="Areas Calculator", 
			fg_color="#C0C0C0", text_color="black", command=None, height=65)
		self.areas_calculator_button.place(relx=0, rely=0.1, relwidth=1)

		# layout
		self.place(relx = self.start_pos, relwidth = self.width, relheight = 1.0)

	def is_active(self):
		"""Returns True if the panel is in the end position, 
		\nFalse otherwise"""
		return self.pos == self.end_pos

	def animate(self):
		"""Animates the panel to the end position if 
		it is \nin the start position"""
		if self.in_start_pos:
			self.animate_forward()
			try:
				self.lift(aboveThis=self.aboabove_these_frames)
			except:
				pass
		else:
			self.animate_backwards()

	def animate_forward(self):
		"""Animates the panel to the end position"""
		if self.pos < self.end_pos-0.16:
			self.pos += 0.04
			self.place(relx = self.pos, relwidth = self.width, relheight = 1.0)
			self.after(10, self.animate_forward)
		else:
			self.in_start_pos = False

	def animate_backwards(self):
		"""Animates the panel to the start position"""
		if self.pos > self.start_pos:
			self.pos -= 0.04
			self.place(relx = self.pos, relwidth = self.width, relheight = 1.0)
			self.after(10, self.animate_backwards)
		else:
			self.in_start_pos = True

class SettingsPanel(SlidePanel):

	def __init__(self, parent:ctk, start_pos:float, end_pos:float, above_these_frames: list):
		super().__init__(parent, start_pos, end_pos, above_these_frames)

		self.width = abs(start_pos + end_pos) + 0.4

		# Remove settings button and areas calculator button
		self.settings_button.destroy()
		self.areas_calculator_button.destroy()

		self.settings_label = ctk.CTkLabel(master=self, text="Settings", font=ctk.CTkFont(family="Helvetica", size=20))
		self.settings_label.place(relx=0.1, rely=0.05)
		self.divider.place(relx = -0.5, rely = 0.15)  # Change padding as needed

		self.themes_label = ctk.CTkLabel(master=self, text="Themes", font=ctk.CTkFont(family="Helvetica", size=15))
		self.themes_label.place(relx=0.1, rely=0.2)
		
		# Create an IntVar for the Switches
		self.switch_var = ctk.IntVar()

		# Create RadioButtons
		self.switch1 = ctk.CTkSwitch(master=self, text="Ligth mode", variable=self.switch_var, onvalue=1, offvalue=1)
		self.switch2 = ctk.CTkSwitch(master=self, text="Dark mode", variable=self.switch_var, onvalue=2, offvalue=2)
		self.switch3 = ctk.CTkSwitch(master=self, text="Blue mode", variable=self.switch_var, onvalue=3, offvalue=3)

		# Place switchButtons
		self.switch1.place(relx=0.1, rely=0.3)
		self.switch2.place(relx=0.1, rely=0.4)
		self.switch3.place(relx=0.1, rely=0.5)

		# layout
		self.place(relx = self.start_pos, relwidth = self.width, relheight = 1.0)

	def animate_forward(self):
		"""Animates the panel to the end position"""
		if self.pos < self.end_pos-0.16:
			self.pos += 0.03
			self.place(relx = self.pos, relwidth = self.width, relheight = 1.0)
			self.after(10, self.animate_forward)
		else:
			self.in_start_pos = False

	def animate_backwards(self):
		"""Animates the panel to the start position"""
		if self.pos > self.start_pos:
			self.pos -= 0.03
			self.place(relx = self.pos, relwidth = self.width, relheight = 1.0)
			self.after(10, self.animate_backwards)
		else:
			self.in_start_pos = True		

class SettingsButton(ctk.CTkButton):
    def __init__(self, parent: ctk, text: str, 
			relx: float, rely: float, height: float, 
			relwidth: float, fg_color: str, text_color: str, 
			image: ctk.CTkImage = None, command: callable = None) -> None:
		
        super().__init__(master = parent, text = text, 
				command = command, height=height, 
				fg_color = fg_color, text_color = text_color, image = image)
        self.place(relx = relx, rely = rely, relwidth = relwidth)

class Frame(ctk.CTkFrame):

	def __init__(self, parent: ctk, fg: str, x_pos: float, y_pos: float, relwidth: float, relheight: float) -> None:
		super().__init__(master = parent, fg_color= fg)
		self.place(relx = x_pos, rely = y_pos, relwidth = relwidth, relheight = relheight)
		
class Label(ctk.CTkLabel):
	def __init__(self, parent: ctk, textvariable: ctk.StringVar, font: ctk.CTkFont, relx: float, rely: float, anchor: str) -> None:
		super().__init__(master = parent, textvariable = textvariable, font = font)
		self.place(relx = relx, rely = rely, anchor = anchor)

class BasicCalculator():
	def __init__(self, window: ctk) -> None:
		self.window = window #Main window
		self.side_panel_active = False #Determines if the side panel is active or not
		self.current_operation_statement = ctk.StringVar() #Stores the current operation statement
		self.current_operation_statement.set('0') #Initialize the current operation statement with '0'
		self.operations_history_statement = ctk.StringVar() #Stores the operations history statement
		self.operations_flag = False #True if the user has already pressed an operation button		
		self.my_font = ctk.CTkFont(family='Helvetica', size=26) #Define the font for the whole program

		#Frames
		#   Operations and numbers frame
		self.nums_and_operations_frame = Frame(self.window, '#292929', 0.0, 0.3, 1, 0.7)

		#   Results frame
		self.results_frame = Frame(self.window, '#292929', 0.0, 0.0, 1, 0.3)

		#   Animated Slide Panels
		#       Settings Panel
		self.settings_panel = SettingsPanel(self.window, -0.5, 0.46, [self.nums_and_operations_frame, self.results_frame])
		#       Main Slide Panel
		self.slide_panel = SlidePanel(self.window, -0.5, 0.1, [self.nums_and_operations_frame, self.results_frame], self.settings_panel.animate)
		self.slide_panel.settings_button.configure(hover_color = '#a2a2a2')

		self.settings_panel.switch1.configure(command = self.manage_switches)
		self.settings_panel.switch2.configure(command = self.manage_switches)
		self.settings_panel.switch3.configure(command = self.manage_switches)

		#Labels
		#   Number statement label
		self.current_operation_statement_label = Label(self.results_frame, 
			self.current_operation_statement, self.my_font, 0.95, 0.85, 'se')
		self.current_operation_statement_label.configure(text_color = 'white')
		self.my_font = ctk.CTkFont(family='Helvetica', size=14)
		self.operations_history_statement_label = Label(self.results_frame,
			self.operations_history_statement, self.my_font, 0.91, 0.45, 'se')
		self.operations_history_statement_label.configure(text_color = 'white')
		self.my_font = ctk.CTkFont(family='Helvetica', size=20)


		#Buttons
		# Slide Panel Button
		self.slide_panel_button = ctk.CTkButton(self.window, text = '', 
		width=50,height=40,command = self.manage_brother_panels, 
		image=ctk.CTkImage(Image.open('sidebar_image.png')), fg_color='#7c87e7', hover_color='#6B78D3')
		self.slide_panel_button.lift(self.slide_panel)
		self.slide_panel_button.place(anchor = 'nw')
		# Bind the disable and enable functions to the slide panel button
		self.slide_panel_button.bind('<Button-1>', lambda event: self.manage_buttons(event) if self.slide_panel.is_active else self.manage_buttons(event))

		# Set the weight for each row and column
		for i in range(6):
			self.nums_and_operations_frame.grid_rowconfigure(i, weight=1)
			for j in range(4):
				self.nums_and_operations_frame.grid_columnconfigure(j, weight=1)


		# Create the buttons
		#   Create number buttons
		self.number_buttons = []
		self.num = 9
		for i in range(10):
			button = ctk.CTkButton(
				self.nums_and_operations_frame, text = str(self.num-i),
				font=self.my_font, width=130,height=50, 
				fg_color='#7c87e7', hover_color='#6B78D3',
				command=lambda aux = self.num-i:self.update_current_operation_statement(str(aux)))
			self.number_buttons.append(button) # 9-0 buttons
		self.number_buttons.append(ctk.CTkButton(self.nums_and_operations_frame, 
			text = '+/-', font=self.my_font, width=130,
			height=50, fg_color='#7c87e7', hover_color='#6B78D3',
			command=lambda aux = '+/-':self.update_current_operation_statement(aux))) # +/- button
		self.number_buttons.append(ctk.CTkButton(self.nums_and_operations_frame, 
			text = '.',font=self.my_font, width=130,
			height=50, fg_color='#7c87e7', hover_color='#6B78D3',
			command=lambda aux = '.':self.update_current_operation_statement(aux))) # . button

		#   Create operation buttons
		self.operation_buttons = []
		self.operations_symbols = ['x','-','+','=','%','CE','C','del','1/x','x^2','√(x)','÷']
		for i in self.operations_symbols:
			if i == 'del':
				self.operation_buttons.append(ctk.CTkButton(self.nums_and_operations_frame, text = '',
					image=ctk.CTkImage(Image.open('backspace_image.png')),
					font=self.my_font, width=130,height=50, fg_color='#2a4993', hover_color='#233F83'))
			else:
				self.operation_buttons.append(ctk.CTkButton(self.nums_and_operations_frame, 
				text = i,font=self.my_font, width=130,height=50, 
				fg_color='#2a4993', hover_color='#233F83'))

		# Place the buttons
		#   Place operations buttons
		index = 4    
		for i in range(0,2):
			for j in range(0,4):
				self.operation_buttons[index].grid(row=i,column=j, padx=1, pady=1, sticky='nsew')
				self.operation_buttons[index].bind('<Button-1>', lambda event, aux = self.operations_symbols[index]:self.update_current_operation_statement(aux))
				index += 1
		index = 0
		for i in range(2,6):
			self.operation_buttons[index].grid(row=i,column=3, padx=1, pady=1, sticky='nsew')
			self.operation_buttons[index].bind('<Button-1>', lambda event, aux = self.operations_symbols[index]:self.update_current_operation_statement(aux))
			index += 1
		#   Place numbers buttons
		index = 0
		for i in range(2,6):
			for j in range(0,3):
				self.number_buttons[index].grid(row=i,column=j, padx=1, pady=1, sticky='nsew')
				index += 1

		#The app starts with the Blue theme by default (later changing to the OS theme)
		self.settings_panel.switch3.toggle()

	# Functions
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
		for button in self.number_buttons:
			button.configure(fg_color=fg_color_nums, hover_color=hv_color_nums, bg_color = bg_color_nums, text_color = text_color)
		for i in range(len(self.operation_buttons)):
			if i == 7:
				self.operation_buttons[i].configure(fg_color = fg_color_backspace, hover_color = hv_color_backspace, bg_color = bg_color_operations)
			else:
				self.operation_buttons[i].configure(fg_color=fg_color_operations, hover_color=hv_color_operations, bg_color = bg_color_operations, text_color = text_color)
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

	def manage_switches(self):
		"""Deselects all the button in to_deactivate and sets the application\n
		theme to the current selected button value"""

		on_switch = 0

		if self.settings_panel.switch_var.get() == 1:
			self.settings_panel.switch2.deselect()
			self.settings_panel.switch3.deselect()
			on_switch = 1
		elif self.settings_panel.switch_var.get() == 2:
			self.settings_panel.switch1.deselect()
			self.settings_panel.switch3.deselect()
			on_switch = 2
		elif self.settings_panel.switch_var.get() == 3:
			self.settings_panel.switch2.deselect()
			self.settings_panel.switch1.deselect()
			on_switch = 3
		else:
			return None
		
		self.change_application_theme(on_switch)
    
	def has_decimals(self,number: str) -> bool:
		'''Returns True if the given number has decimals different to 0'''
		if number.find('.') != -1:
			for i in range(number.find('.')+1, len(number)):
				if number[i] != '0':
					return True
		return False

	def to_int(self,number: str) -> int:
		'''Returns the given number as an integer
		\nIf the number has decimals different to 0, returns the number as a float'''
		if self.has_decimals(number):
			return float(number)
		else:
			if number.find('.') == -1:
				return int(number)
			else:
				number = number[0:number.find('.')]
				return int(number)

	def get_last_numerical_input(self) -> str:
		'''Returns the last numerical input given by the user'''

		aux = ''
		#Get the last number given by the user
		for i in reversed(self.operations_history_statement.get()):
			if(i in '1234567890.' 
			or i == "-" and aux not in "-" and aux != ''):
				aux = i + aux
			elif i not in '1234567890.' and aux != '':
				break
		return aux

	def validate_division_by_zero(self) -> bool:
		'''Returns True if the user has made a division by zero'''

		if self.current_operation_statement.get() == 'Cannot divide by 0':
			self.operations_history_statement.set('')
			self.update_operations_history_statement('')
			self.current_operation_statement.set('Cannot divide by 0')
			self.current_operation_statement_label.configure(textvariable=self.current_operation_statement)
			return True
		return False

	def manage_porcentage_operation(self) -> None:
		'''Manages the porcentage operation'''

		#Validate if the user has already given a number input
		aux_current = self.current_operation_statement.get() #Bakcup the current operation statement
		if self.operations_history_statement.get() == "":
			self.current_operation_statement.set(self.execute_basic_operation("1", self.current_operation_statement.get(), '%'))
			self.operations_history_statement.set(aux_current+"%=")
		else:
			last_numerical_input = self.get_last_numerical_input()
			porcentage = self.execute_basic_operation(
				last_numerical_input, self.current_operation_statement.get(), '%')
			self.current_operation_statement.set(self.execute_basic_operation(last_numerical_input, 
				porcentage, self.operations_history_statement.get()[-1]))
			self.operations_history_statement.set(self.operations_history_statement.get()
				+porcentage+"%=")
		self.update_operations_history_statement("")

	def manage_buttons(self,event) -> None:
		'''Disable or enable the buttons when the slide panel is active'''

		if not self.side_panel_active:
			for button in self.number_buttons:
				button.configure(state='disabled')
			for button in self.operation_buttons:
				button.configure(state='disabled')
			self.side_panel_active = True
		else:
			for button in self.number_buttons:
				button.configure(state='normal')
			for button in self.operation_buttons:
				button.configure(state='normal')
			self.side_panel_active = False

	def manage_brother_panels(self) -> None:
		'''Manages the brother panels of the main slide panel'''

		self.slide_panel.animate()
		if not self.slide_panel.is_active():
			self.settings_panel.animate_backwards()

	def update_current_operation_statement(self,stmt: str) -> None:
		'''Updates the current operation statement label with the given statement
		\nIt operates with the given statement and the current operation statement'''

		#Validate if the user has exceeded the maximum number of digits (12)
		if(len(self.current_operation_statement.get()) == 12 and stmt != 'C' and stmt != 'CE' and stmt != 'del'
		and stmt not in '+x÷-=%' and stmt != 'x^2' and stmt != '1/x' and stmt != '√(x)'
		and not self.operations_flag):
			return None

		#Validate if the user is giving an negation input
		if stmt == '+/-':
			aux_current = self.current_operation_statement.get() #Bakcup the current operation statement
			self.current_operation_statement.set(self.execute_basic_operation('-1', self.current_operation_statement.get(), 'x'))
			return None

		#Validate if the user has processed a division by zero
		if (self.validate_division_by_zero() == True
		and stmt != 'C' and stmt != 'CE' 
		and stmt != 'del'):
			return None

		#Validate if the user is giving the very first input
		if(self.current_operation_statement.get() == '0' 
		and stmt != 'C' and stmt != 'CE' 
		and stmt != 'del' and stmt not in '+x÷-%'
		and stmt != 'x^2' and stmt != '1/x' and stmt != '√(x)'
		and self.operations_history_statement.get() == ''
		and not self.operations_flag):
			if(stmt == '.'):
				self.current_operation_statement.set('0.')
			else:
				self.current_operation_statement.set(stmt)

		else:

			#Validate if the user is giving an operation input
			if(stmt not in '1234567890.' 
			and self.operations_history_statement.get() == '' 
			and stmt != 'C' and stmt != 'CE' and stmt != 'del'):
				
				#Validate if the user is giving a % input
				if stmt == "%":
					self.manage_porcentage_operation()
				
				#Validate if the user is giving a power, squared root or 1-divided-by operation input
				elif(stmt == 'x^2' or stmt == '1/x' or stmt == '√(x)'):
					aux_current = self.current_operation_statement.get() #Bakcup the current operation statement
					if(stmt == '1/x'):
						stmt = "1÷x"
						self.current_operation_statement.set(self.execute_basic_operation('1', self.current_operation_statement.get(), '÷'))
					else:
						self.current_operation_statement.set(self.execute_advanced_operation(self.current_operation_statement.get(), stmt))
						
					#Validate if the user has made a division by zero
					if self.validate_division_by_zero() == True:
						return None
					
					self.operations_history_statement.set(stmt.replace('x', aux_current)+"=")
					self.update_operations_history_statement("")
				else:
					if(self.operations_history_statement.get() not in '^√'
					and self.operations_history_statement.get().find("1÷") == -1):
						self.operations_history_statement.set(self.current_operation_statement.get()+stmt)
					else:
						self.operations_history_statement.set(self.current_operation_statement.get())
						self.update_operations_history_statement(stmt)
				self.operations_flag = True
				
			#Validate if the user is giving an operation input after another operation input
			elif (stmt in '+-x÷=%' or stmt == 'x^2' or stmt == '1/x' or stmt == '√(x)'
				and self.operations_history_statement.get() != ''):
				
				#Validate if the user is giving a % input
				if stmt == "%":
					self.manage_porcentage_operation()

				#Validate if the user is giving a power, squared root or 1-divided-by operation input
				elif stmt == 'x^2' or stmt == '1/x' or stmt == '√(x)':
					aux_current = self.current_operation_statement.get() #Bakcup the current operation statement
					if(stmt == '1/x'):
						stmt = "1÷x"
						self.current_operation_statement.set(self.execute_basic_operation('1', self.current_operation_statement.get(), '÷'))
					else:
						self.current_operation_statement.set(self.execute_advanced_operation(self.current_operation_statement.get(), stmt))
						
					#Validate if the user has made a division by zero
					if self.validate_division_by_zero() == True:
						return None
					
					self.operations_history_statement.set(stmt.replace('x', aux_current)+"=")
					self.update_operations_history_statement("")
				else:
					aux = self.get_last_numerical_input()

					#Backup the values of the statements
					op_history_aux = self.operations_history_statement.get()
					current_statement_aux = self.current_operation_statement.get()
					#Validate if the user is giving an operation input after a result input
					if self.operations_history_statement.get().find('=') == -1:
						self.current_operation_statement.set(self.execute_basic_operation(aux, 
						self.current_operation_statement.get(), op_history_aux[-1]))                
						#Validate if the user has made a division by zero
						if self.validate_division_by_zero() == True:
							return None

					#Validate if the user is giving an operation input after another operation input
					#different to '='
					if stmt != '=':
						self.operations_history_statement.set('')
						self.update_operations_history_statement(self.current_operation_statement.get()+stmt)
						self.current_operation_statement.set(current_statement_aux)
					else:
						self.operations_history_statement.set('')
						self.update_operations_history_statement(op_history_aux+current_statement_aux+stmt)
					self.operations_flag = True

			#Validate if the user is giving an 'clear operations' input
			elif stmt == 'C':
				self.current_operation_statement.set('0')
				self.operations_history_statement.set('')

			#Validate if the user is giving an 'clear current operator' input
			elif stmt == 'CE':
				self.current_operation_statement.set('0')

			elif stmt == 'del':
				self.current_operation_statement.set(self.current_operation_statement.get()[0:-1])
				if self.current_operation_statement.get() == '':
					self.current_operation_statement.set('0')

			else:
				#Validate if the user is giving an numerical input and if the user has already
				#given an operation input
				if stmt in '1234567890.' and self.operations_flag:
					if self.current_operation_statement.get().find('.') == -1 and stmt == '.':
						self.current_operation_statement.set(self.current_operation_statement.get()+stmt)
					elif self.current_operation_statement.get().find('.') != -1 and stmt == '.':
						return None
					else:
						self.current_operation_statement.set(stmt)
					self.operations_flag = False
				elif stmt in '1234567890.':
					if self.current_operation_statement.get().find('.') != -1 and stmt == '.':
						return None
					else:
						if self.current_operation_statement.get() == '0':
							self.current_operation_statement.set(stmt)
						else:
							self.current_operation_statement.set(self.current_operation_statement.get()+stmt)

		#Update the current operation statement label
		self.current_operation_statement_label.configure(textvariable=self.current_operation_statement)

	def update_operations_history_statement(self,stmt: str) -> None:
		'''Updates the operations history statement label with the given statement'''

		#Validate if the user is giving the very first input
		if(self.operations_history_statement.get() == ''):
			self.operations_history_statement.set(stmt)
		else:
			self.operations_history_statement.set(self.operations_history_statement.get()+stmt)
		self.operations_history_statement_label.configure(textvariable=self.operations_history_statement)

	def execute_basic_operation(self,float_str_1: str, float_str_2: str, operation: str) -> str:
		'''Executes the given basic arithmetical operation with the given numbers and returns the result'''

		result = ''
		if operation == '+':
			result = str(self.to_int(str(Operation.Operation.sum(float(float_str_1), float(float_str_2)))))
		elif operation == '-':
			result = str(self.to_int(str(Operation.Operation.substract(float(float_str_1), float(float_str_2)))))
		elif operation == 'x':
			result = str(self.to_int(str(Operation.Operation.multiply(float(float_str_1), float(float_str_2)))))
		elif operation == '÷':
			result = str(self.to_int(str(Operation.Operation.divide(float(float_str_1), float(float_str_2)))))
		elif operation == '%':
			result = str(self.to_int(str(Operation.Operation.porcentage(float(float_str_1), float(float_str_2)))))
		
		return result

	def execute_advanced_operation(self,float_str_1: str, operation: str) -> str:
		'''Executes the given basic arithmetical operation with the given numbers and returns the result'''

		result = ''
		if operation == '√(x)':
			result = str(str(Operation.Operation.squared_root(float(float_str_1))))
		elif operation == 'x^2':
			result = str(str(Operation.Operation.power(float(float_str_1),2)))

		#Validate if the result contains parenthesis
		if result[0] == "(":
			result = result.replace('(', '')
			result = result.replace(')', '')

		#Validate if the result contains a comlpex number
		if result.find('j') != -1:
			result = result[0:result.find('+')]

		#Validate if the result is an integer
		result = str(self.to_int(result))
			
		return result