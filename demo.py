from termcolorxcore import success, input_colored, error, warning

try:
    x_str = input_colored("Enter x: ", color="cyan", styles=["bold"])
    x = int(x_str)  # convert to integer
except ValueError:
    error("Invalid input! Please enter a number.")
    exit(1)

if x > 5:
    success("X is bigger than 5.")
elif x < 5:
    warning("X is not bigger than 5.")
else:
    success("X is exactly 5.")