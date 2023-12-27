# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# def main():
#     print("Temperature Converter")
#     print("1. Fahrenheit to Celsius")
#     print("2. Celsius to Fahrenheit")

#     choice = int(input("Enter your choice (1 or 2): "))

#     if choice == 1:
#         fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#         celsius = fahrenheit_to_celsius(fahrenheit)
#         print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")
#     elif choice == 2:
#         celsius = float(input("Enter temperature in Celsius: "))
#         fahrenheit = celsius_to_fahrenheit(celsius)
#         print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")
#     else:
#         print("Invalid choice. Please enter 1 or 2.")

# if __name__ == "__main__":
#     main()

import tkinter as tk

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        if var.get() == 1:
            result = fahrenheit_to_celsius(temperature)
            label_result.config(text=f"{temperature:.2f} Fahrenheit is equal to {result:.2f} Celsius")
        elif var.get() == 2:
            result = celsius_to_fahrenheit(temperature)
            label_result.config(text=f"{temperature:.2f} Celsius is equal to {result:.2f} Fahrenheit")
    except ValueError:
        label_result.config(text="Invalid input. Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Temperature entry
label_temperature = tk.Label(window, text="Enter Temperature:")
label_temperature.pack()

entry_temperature = tk.Entry(window)
entry_temperature.pack()

# Radio buttons for conversion direction
var = tk.IntVar()
radio_f_to_c = tk.Radiobutton(window, text="Fahrenheit to Celsius", variable=var, value=1)
radio_c_to_f = tk.Radiobutton(window, text="Celsius to Fahrenheit", variable=var, value=2)

radio_f_to_c.pack()
radio_c_to_f.pack()

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.pack()

# Result label
label_result = tk.Label(window, text="")
label_result.pack()

# Run the main loop
window.mainloop()

