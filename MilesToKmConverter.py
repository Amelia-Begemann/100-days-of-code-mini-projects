# This code is a simple graphical user interface (GUI) program that converts miles to kilometres. Here is a summary of
# the code:

# Import tkinter module
import tkinter as tk

# Defining a function named "convert" that is called when the "Convert" button is clicked. This function converts the
# miles entered in the Entry widget to kilometers and displays the result in a Label widget.
def convert():
    answer = float(miles_input.get())
    print(f"Float received: {answer}")
    results = round(answer * 1.60934,2)
    km_result.config(text = f"{results}")

# Creating a window using the Tk class and setting its title and padding
window = tk.Tk()
window.title("Miles to km")
window.config(padx=20, pady=20)

# Creating an Entry widget for inputting miles and setting its initial value to 0.
miles_input = tk.Entry(width=20, justify='center')
miles_input.insert(index=0, string=0)
miles_input.grid(row=0, column=1)

# Creating Label widgets for "miles", "km", and "is equal to".
Miles_unit = tk.Label(text="miles")
Miles_unit.grid(row=0, column=2)

km_unit = tk.Label(text="km")
km_unit.grid(row=1, column=2)

km_string = tk.Label(text="is equal to")
km_string.grid(row=1,column=0)

# Creating a Label widget for displaying the result of the conversion.
km_result = tk.Label(text="##")
km_result.grid(row=1, column=1)

# Creating a Button widget with the text "Convert" and linking it to the "convert" function.
my_button = tk.Button(text="Convert", command = convert)
my_button.grid(row = 2, column = 1)

# Running the main event loop using the mainloop() method.
window.mainloop()
