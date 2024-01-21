import customtkinter as ctk

class SlidePanel(ctk.CTkFrame):
	def __init__(self, parent:ctk, start_pos:float, end_pos:float, above_this_frame: ctk):
		super().__init__(master = parent)

		# general attributes 
		self.start_pos = start_pos - 0.04
		self.end_pos = end_pos + 0.03
		self.width = abs(start_pos + end_pos) - 0.03
		self.above_this_frame = above_this_frame

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
			self.lift(aboveThis=self.above_this_frame)
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

class NumbersFrame(ctk.CTkFrame):

	def __init__(self, parent: ctk, bg: str, x_pos: int, y_pos: int) -> None:
		super().__init__(master = parent, fg_color= bg,border_color = bg,height=200, width=300)
		self.place(relx = x_pos, rely = y_pos)
		self.grid_propagate(False)

class OperationsFrame(ctk.CTkFrame):
	def __init__(self, parent: ctk, bg: str, x_pos: int, y_pos: int) -> None:
		super().__init__(master = parent, fg_color= bg,border_color = bg,height=300, width=200)
		self.place(relx = x_pos, rely = y_pos)
		self.grid_propagate(False)