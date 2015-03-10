from Tkinter import *

root = Tk()
#root.option_readfile('optionDB')
root.title('Canvas')
canvas = Canvas(root, width = 400, height = 400)

xy = 10, 105, 100, 200
canvas.create_arc(xy, start = 0, extent = 270, file = 'gray60')

cancas.pack()
root.mainloop()
