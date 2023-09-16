import time
from tkinter import Tk, Label

def time_update():
    current_time = time.strftime("%H:%M:%S %p")  # Get the current time
    label.config(text=current_time)  # Update the label text
    label.after(1000, time_update)  # Update the time every 1000ms (1 second)

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")  # Corrected the geometry string

window.configure(bg="steelblue")
label = Label(window, text="Welcome!", font=("Arial Black", 48, "bold"), bg="steelblue")
label.pack(pady=100)

# Start the time update function
time_update()

window.mainloop()

