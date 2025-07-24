import tkinter as tk

def launch_action():
    # This function does nothing when called
    pass

def main():
    root = tk.Tk()
    root.title("Launcher")

    label = tk.Label(root, text="Click Apply to launch Shot Gun Pack v1")
    label.pack(padx=20, pady=(20,10))

    launch_button = tk.Button(root, text="Apply", command=launch_action)
    launch_button.pack(padx=20, pady=(0,20))

    root.mainloop()

if __name__ == "__main__":
    main()