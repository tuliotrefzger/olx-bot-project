import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Search GUI")

# Dynamically adjust the window size and centering
root.geometry("650x300")  # Adjust width as needed


# Function to center window on screen
def center_window(w=300, h=200):
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Calculate x and y coordinates
    x = (screen_width / 2) - (w / 2)
    y = (screen_height / 2) - (h / 2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))


center_window(600, 200)  # Adjust width and height as needed

# Configure the grid columns to distribute space evenly
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# Elements setup with dynamic centering

# Your dropdowns, input boxes, and button setup here

# Example for one dropdown (apply similar adjustments for others)
marca_label = ttk.Label(root, text="Marca:")
marca_label.grid(column=0, row=0, padx=10, pady=10, sticky="EW")

marca_var = tk.StringVar()
marca_dropdown = ttk.Combobox(root, textvariable=marca_var, state="readonly")
marca_dropdown["values"] = ("Marca1", "Marca2", "Marca3")  # Example brands
marca_dropdown.grid(column=1, row=0, padx=10, pady=10, sticky="EW")

# Dropdown for "Modelo"
modelo_label = ttk.Label(root, text="Modelo:")
modelo_label.grid(column=2, row=0, sticky="E")

modelo_var = tk.StringVar()
modelo_dropdown = ttk.Combobox(root, textvariable=modelo_var, state="readonly")
modelo_dropdown["values"] = ("Modelo1", "Modelo2", "Modelo3")  # Example models
modelo_dropdown.grid(column=3, row=0, sticky="EW")

# Input boxes
input_labels = ["Ano Max", "Ano Min", "KM Max", "KM Min"]
inputs = []

for i, label in enumerate(input_labels, start=0):
    ttk.Label(root, text=label).grid(column=i, row=1, padx=10, pady=10)
    entry_var = tk.StringVar()
    entry = ttk.Entry(root, textvariable=entry_var)
    entry.grid(column=i, row=2, padx=10, pady=10)
    inputs.append(entry)
# Search Button
search_button = tk.Button(
    root, text="Buscar", command=lambda: print("Searching..."), bg="red", fg="white"
)
search_button.grid(column=0, row=3, columnspan=4, pady=20, sticky="EW")

# Main loop
root.mainloop()
