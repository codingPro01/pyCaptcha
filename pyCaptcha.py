import tkinter as tk
import random
requ = random.randrange(0, 11)
pressed = 0
closed = False
print(f"Click the button {requ} times.")
def printout():
    global pressed
    pressed += 1
    print(f"Pressed {pressed} times.")
def closewin():
    print("Verification window closed.")
    window.destroy()
    closed = True
window = tk.Tk()
window.title("Test")
window.wm_iconbitmap('appicon.ico')
window.geometry("500x200")
button = tk.Button(window, activebackground="#000000", activeforeground="#ffffff", text="Click here", command=printout)
clbtn = tk.Button(window, activebackground="#000000", activeforeground="#ffffff", text="Close", command=closewin)
button.place(x=100, y=10)
clbtn.place(x=200, y=10)
info1 = tk.Label(text="pyCaptcha")
info1.place(x=10, y=10)
window.mainloop()
if requ == pressed:
    print("Verification complete.")
else:
    print("Verification failed.")