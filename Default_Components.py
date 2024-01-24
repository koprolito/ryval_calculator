import customtkinter as ctk
from PIL import Image, ImageTk


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

		self.settings_button.destroy()

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