import customtkinter as ctk

class SlidePanel(ctk.CTkFrame):
	def __init__(self, parent:ctk, start_pos:float, end_pos:float, above_these_frames: list):
		super().__init__(master = parent)

		# general attributes 
		self.start_pos = start_pos - 0.04
		self.end_pos = end_pos + 0.03
		self.width = abs(start_pos + end_pos) - 0.03
		self.aboabove_these_frames = above_these_frames

		# animation logic
		self.pos = self.start_pos
		self.in_start_pos = True

		# layout
		self.place(relx = self.start_pos, relwidth = self.width, relheight = 1.0)

	def is_active(self):
		return self.pos == self.end_pos

	def animate(self):
		if self.in_start_pos:
			self.animate_forward()
			try:
				self.lift(aboveThis=self.aboabove_these_frames)
			except:
				pass
		else:
			self.animate_backwards()

	def animate_forward(self):
		if self.pos < self.end_pos-0.13:
			self.pos += 0.02
			self.place(relx = self.pos, relwidth = self.width, relheight = 1.0)
			self.after(10, self.animate_forward)
		else:
			self.in_start_pos = False

	def animate_backwards(self):
		if self.pos > self.start_pos:
			self.pos -= 0.02
			self.place(relx = self.pos, relwidth = self.width, relheight = 1.0)
			self.after(10, self.animate_backwards)
		else:
			self.in_start_pos = True  

class Frame(ctk.CTkFrame):

	def __init__(self, parent: ctk, fg: str, x_pos: float, y_pos: float, relwidth: float, relheight: float) -> None:
		super().__init__(master = parent, fg_color= fg)
		self.place(relx = x_pos, rely = y_pos, relwidth = relwidth, relheight = relheight)	