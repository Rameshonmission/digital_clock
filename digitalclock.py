import time
from tkinter import Tk, Label

def time_update():
    current_time = time.strftime("%H:%M:%S %p")  # Get the current time
    label.config(text="Welcome time")  # Update the label text
    label.after(1000, time_update)  # Update the time every 1000ms (1 second)

window = Tk()
window.title("Digital Clock")
window.geometry("600x600")  # Corrected the geometry string

window.configure(bg="darkgreen")
label = Label(window, text="Welcome time!", font=("Arial Black", 60, "bold"), bg="darkgreen")
label.pack(pady=100)

def clock():
    current_time = time.strftime("%H:%M:%S %p")  # Get the current time
    label.config(text=current_time)  # Update the label text
    label.after(1000, clock)  # Update the time every 1000ms (1 second)

# Start the time update function
time_update()

window.mainloop()

