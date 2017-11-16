def is_mod(base, divisor, result):
    if (base % divisor) == 0:
        return result
    return ""


for i in range(0, 130):
    output = ""

    output += is_mod(i, 3, "Fizz")
    output += is_mod(i, 5, "Buzz")
    output += is_mod(i, 8, "Fuzz")

    if output == "":
        output = str(i)
    print(output)
