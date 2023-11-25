# making a WORKING paint app with absolutely no gliches
from tkinter import messagebox
from tkinter import filedialog
import tkinter
from tkinter import *
import PIL.ImageGrab as ImageGrab


draw_window = Tk()
draw_window.title('Drawing Program')

draw_window.geometry('1000x700+550+100')
color= tkinter.StringVar(draw_window)

color.set('Black')
# ----------------------------------------------------------------Functions ----------------------------------------------------------------------------------------------#

def Exit():
	draw_window.destroy()
	return()

def SAVE():
	fileLocation = filedialog.asksaveasfilename(defaultextension=".png")
	x = int(draw_window.winfo_rootx())
	y = int(draw_window.winfo_rooty())
	img = ImageGrab.grab(bbox=(x,y,x+1000,y+600))
	img.save(fileLocation)
	showImage = messagebox.askyesno("Paint App" , "Do you want to open image?")
	if showImage:
		img.show()
	else:
		return()
	return()

var = StringVar()
var.set("")
class CHANGE_COLOR():
	def Red():
		color.set('red')
		
		
	def Blue():
		color.set('blue')
		
		
	def Green():
		color.set('green')
		
		
	def Purple():
		color.set('purple')
		
		
	def Pink():
		color.set('pink')
		
def pencil():
	Edit_menu.entryconfig("Change Pen Color", state="active")

	color.set('black')
	canvas["cursor"]= 'arrow'




def ERASE():
	Edit_menu.entryconfig("Change Pen Color", state="disabled")
	if var.get()== "":
		color.set('white')
	else:
		color.set(var.get())

	canvas["cursor"]= DOTBOX

# the drawing func
prevpoint = [0,0]
currpoint = [0,0]

def painter(event):
	global prevpoint, currpoint
	x = event.x
	y = event.y
	currpoint = [x, y]

	if prevpoint != [0,0] :
		canvas.create_polygon( prevpoint[0], prevpoint[1], currpoint[0], currpoint[1], fill=color.get(),outline=color.get(), width=Size_scale.get())

	prevpoint = currpoint
	if event.type != "6":
		prevpoint = [0,0]
class Canvas_change():
	def Red():
		canvas.delete('all')
		canvas.config(bg="red")
		pencil()
		var.set('red')
	def Blue():
		canvas.delete('all')
		canvas.config(bg="blue")
		pencil()

		var.set('blue')
	def Green():
		canvas.delete('all')
		canvas.config(bg="green")
		pencil()
		var.set('green')
	def Purple():
		canvas.delete('all')
		canvas.config(bg="purple")
		pencil()
		var.set('purple')
	def Pink():
		canvas.delete('all')
		canvas.config(bg="pink")
		pencil()
		var.set('pink')
def NEW():
	pass

# --------------------------------------------------------------- UI, Canvas and Menubar -----------------------------------------------------------------------------------------#

menubar = Menu(draw_window)
draw_window.config(menu=menubar)

File_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=File_menu)
File_menu.add_command(label="New",command=NEW)
File_menu.add_command(label="Save",command=SAVE)
File_menu.add_separator()
File_menu.add_command(label="Exit",command=Exit)

Edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=Edit_menu)
Edit_menu.add_command(label="Eraser",command=ERASE)
color_change_menu = Menu(Edit_menu, tearoff=0)
Edit_menu.add_cascade(label="Change Pen Color", menu = color_change_menu)
color_change_menu.add_command(label="Red", command= CHANGE_COLOR.Red)
color_change_menu.add_command(label="Blue", command= CHANGE_COLOR.Blue)
color_change_menu.add_command(label="Green", command= CHANGE_COLOR.Green)
color_change_menu.add_command(label="Purple", command= CHANGE_COLOR.Purple)
color_change_menu.add_command(label="Pink", command= CHANGE_COLOR.Pink)
Edit_menu.add_separator()
canvas_color_change_menu = Menu(Edit_menu, tearoff = 0)
Edit_menu.add_cascade(label="Change Backgrounf color", menu=canvas_color_change_menu)
canvas_color_change_menu.add_command(label="Red", command= Canvas_change.Red)
canvas_color_change_menu.add_command(label="Blue", command= Canvas_change.Blue)
canvas_color_change_menu.add_command(label="Green", command= Canvas_change.Green)
canvas_color_change_menu.add_command(label="Purple", command= Canvas_change.Purple)
canvas_color_change_menu.add_command(label="Pink", command= Canvas_change.Pink)











canvas = Canvas(draw_window, bg='white', height= 600, width=1000)
canvas.grid(column=0, columnspan=10)

canvas.bind("<B1-Motion>", painter)
canvas.bind("<ButtonRelease-1>", painter)
Size_scale = Scale(draw_window, from_=0, to=50, orient=HORIZONTAL)
Size_scale.grid(row=1, column=0)
Size_label = Label(draw_window, text="Select the size", font=('Times New roman', '14')).grid(row=2,column=0)

Pencil_button =Button(draw_window, text ="pencil",font=('Times New roman', '14'), command=pencil).grid(row=1,column=1)
Eraser_button =Button(draw_window, text ="Eraser",font=('Times New roman', '14'), command=ERASE).grid(row=2,column=1)




draw_window.resizable(False, False)
draw_window.mainloop()