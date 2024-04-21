def power_function(exponent):
    return lambda x: x ** exponent

square_power = power_function(2)
print(square_power(3))