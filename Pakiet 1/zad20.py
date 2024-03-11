def analyze_data(data):
    if isinstance(data, list):
        print("This is a list with length", len(data))
    elif isinstance(data, tuple):
        print("This is a tuple with length", len(data))
    else:
        print("This is another data structure")

analyze_data([1, 2, 3])
analyze_data((4, 5, 6))
analyze_data("abc")