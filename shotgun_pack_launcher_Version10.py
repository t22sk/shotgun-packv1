import tkinter as tk

def open_progress_window():
    # Hide main window
    root.withdraw()
    # Create progress window
    progress_win = tk.Toplevel()
    progress_win.title("Applying Shotgun-Pack v1")
    progress_win.geometry("800x400")  # Larger progress window
    progress_win.resizable(False, False)
    progress_win.configure(bg="#4a4a4a")  # Grey background

    label = tk.Label(
        progress_win, 
        text="Applying Shotgun-Pack v1...", 
        font=("Arial", 24), 
        bg="#4a4a4a", 
        fg="#ffffff"  # White text
    )
    label.pack(pady=50)

    progress_var = tk.DoubleVar()
    progress_bar = tk.Canvas(progress_win, width=600, height=50, bg="#ffffff", bd=0, highlightthickness=0)  # White bar background
    bar_rect = progress_bar.create_rectangle(0, 0, 0, 50, fill="#a9a9a9")  # Grey progress fill (#a9a9a9 or #808080)
    progress_bar.pack(pady=30)

    percent_label = tk.Label(progress_win, text="0%", font=("Arial", 22), bg="#4a4a4a", fg="#ffffff")  # White text
    percent_label.pack()

    def update_bar(*args):
        value = progress_var.get()
        width = int(value / 100 * 600)
        progress_bar.coords(bar_rect, 0, 0, width, 50)

    progress_var.trace("w", update_bar)

    def update_progress(increment, step):
        current = progress_var.get()
        if current < 100:
            progress_var.set(min(current + increment, 100))
            percent_label.config(text=f"{int(progress_var.get())}%")
            progress_win.after(50, lambda: update_progress(increment, step + 1))  # 50 ms per update
        else:
            progress_var.set(100)
            percent_label.config(text="100%")
            label.config(text="Changes have been applied. Please close this window.")

    # 4 seconds, 20 updates per second = 80 steps
    increment = 100 / (4 * 20)
    progress_win.after(100, lambda: update_progress(increment, 0))

root = tk.Tk()
root.title("Shotgun-Pack v1 Launcher")
root.geometry("900x450")  # Much larger launcher window
root.resizable(False, False)

frame = tk.Frame(root, bg="#4a4a4a")  # Grey background
frame.pack(fill=tk.BOTH, expand=True)

status_label = tk.Label(
    frame,
    text="Click here to apply Shotgun-Pack v1",
    font=("Arial", 28),
    bg="#4a4a4a",
    fg="#ffffff"  # White text
)
status_label.pack(pady=80)

apply_button = tk.Button(
    frame,
    text="Apply",
    font=("Arial", 22),
    bg="#ffffff",  # White button
    fg="#4a4a4a",  # Grey text
    command=open_progress_window,
    relief=tk.RAISED,
    borderwidth=2,
    width=25,
    height=3
)
apply_button.pack(pady=30)

root.mainloop()