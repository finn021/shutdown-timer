import tkinter as tk
import subprocess

def schedule_shutdown_minutes(minutes):
    try:
        seconds = int(minutes) * 60
        subprocess.run(["shutdown", "/s", "/t", str(seconds)], shell=True)
        status_label.config(text=f"Shutdown scheduled in {minutes} minute(s).")
    except ValueError:
        status_label.config(text="Please enter a valid number.")

def schedule_from_entry():
    minutes = time_var.get()
    schedule_shutdown_minutes(minutes)

def cancel_shutdown():
    subprocess.run(["shutdown", "/a"], shell=True)
    status_label.config(text="Shutdown cancelled.")

def validate_entry(*args):
    """Enable button only if entry has a valid positive number."""
    text = time_var.get()
    if text.isdigit() and int(text) > 0:
        schedule_button.config(state="normal")
    else:
        schedule_button.config(state="disabled")

# GUI setup
root = tk.Tk()
root.title("Shutdown Timer")
root.geometry("350x250")
root.minsize(320, 240)  # Prevent shrinking

# Entry + binding
time_var = tk.StringVar()
time_var.trace_add("write", validate_entry)  # Monitor changes

entry_label = tk.Label(root, text="Custom time before shutdown (minutes):")
entry_label.pack()

entry = tk.Entry(root, textvariable=time_var)
entry.pack()

schedule_button = tk.Button(root, text="Schedule Shutdown", command=schedule_from_entry, state="disabled")
schedule_button.pack(pady=5)

# Preset time buttons
preset_frame = tk.Frame(root)
preset_frame.pack(pady=10)

tk.Label(preset_frame, text="Quick Schedule:").grid(row=0, column=0, columnspan=4)

btn_15min = tk.Button(preset_frame, text="15 min", width=8, command=lambda: schedule_shutdown_minutes(15))
btn_30min = tk.Button(preset_frame, text="30 min", width=8, command=lambda: schedule_shutdown_minutes(30))
btn_1hr = tk.Button(preset_frame, text="1 hr", width=8, command=lambda: schedule_shutdown_minutes(60))
btn_2hr = tk.Button(preset_frame, text="2 hr", width=8, command=lambda: schedule_shutdown_minutes(120))

btn_15min.grid(row=1, column=0, padx=5, pady=2)
btn_30min.grid(row=1, column=1, padx=5, pady=2)
btn_1hr.grid(row=1, column=2, padx=5, pady=2)
btn_2hr.grid(row=1, column=3, padx=5, pady=2)

# Cancel button
cancel_button = tk.Button(root, text="Cancel Shutdown", fg="red", command=cancel_shutdown)
cancel_button.pack(pady=10)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=5)

root.mainloop()
