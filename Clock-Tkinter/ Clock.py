import tkinter
# retrieve system's time
from time import strftime
root = tkinter.Tk()
root.title("Clock")

# resizable() method is used to allow Tkinter root window to change it’s size according to the users need
# as well we can prohibit resizing of the Tkinter window.
# So, basically, if user wants to create a fixed size window, this method can be used.

#restricting the resizable property
root.resizable(0, 0)
clockTime = tkinter.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')


def time():
    # We can create our own time statement with the strftime () function.
    system_time = strftime('%H:%M:%S %p')
    # Configure resources of a widget.
    clockTime.config(text=system_time)
    #  .after(delay, callback=None) is a method defined for all tkinter widgets.
    #   This method simply calls the function callback after the given delay in ms.
    clockTime.after(1000, time)

# The Pack geometry manager packs widgets in rows or columns.
clockTime.pack(anchor = "center")
time()
root.mainloop()
