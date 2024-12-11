import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()

    # Set the window title
    root.title("Maximized Black Window with Blue Box")

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window size to the screen size
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    # Configure the window to be black
    root.configure(bg="black")

    # Create a blue box with rounded corners
    box_width = screen_width // 2
    box_height = screen_height // 4
    box = tk.Canvas(root, width=box_width, height=box_height, bg="blue", highlightthickness=0)
    box.create_rectangle(0, 0, box_width, box_height, fill="blue", outline="")
    box.create_arc(0, 0, 50, 50, start=90, extent=90, fill="black", outline="")
    box.create_arc(box_width-50, 0, box_width, 50, start=0, extent=90, fill="black", outline="")
    box.pack()

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
