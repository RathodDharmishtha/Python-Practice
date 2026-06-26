def print_list(lst, idx):
    if idx == len(lst):   # Base case
        return

    print(lst[idx])       
    print_list(lst, idx + 1)  # Recursive call

cars = ["RR", "BMW", "Range Rover"]
print_list(cars, 0)