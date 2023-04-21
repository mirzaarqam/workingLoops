import tkinter as tk
from tkinter import simpledialog, messagebox

# Create a Tkinter root window
root = tk.Tk()

# Hide the root window
root.withdraw()

# Ask for the first number using a dialog box
num1 = simpledialog.askinteger(title="Input", prompt="Enter the first number:")

# Ask for the second number using a dialog box
num2 = simpledialog.askinteger(title="Input", prompt="Enter the second number:")

# Compute the sum of the two numbers
result = num1 + num2

# Show the result in a dialog box
messagebox.showinfo(title="Result", message="The sum is " + str(result))

# Start the Tkinter event loop
root.mainloop()
