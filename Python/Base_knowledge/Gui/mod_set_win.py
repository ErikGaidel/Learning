from tkinter import *


#   def: function for create window with some settings
#   o - object type class 'tkinter.Tk', if not enter create new object
#   z - set a title of window
#   w - set a width of window
#   h - set a height of window
#   r - if true make a window resizable, if false - not resizable
#   return: o - object type class 'tkinter.Tk'
def window_setting(o=Tk(), z="Window", w=800, h=600, r=True) -> object:
    o.title(z)
    if r:
        o.resizable(True, True)
    else:
        o.resizable(False, False)

    ws = o.winfo_screenwidth()
    wh = o.winfo_screenheight()
    p_x = int(ws / 2 - w / 2)
    p_y = int(wh / 2 - h / 2)
    x = "{0}x{1}+{2}+{3}"
    o.geometry(x.format(w, h, p_x, p_y))
    return o
