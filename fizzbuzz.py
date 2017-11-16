def get_string(dict, base):
    string = ""
    for key, value in dict.items():
        if (base % key) == 0:
            string += value
    return string


for i in range(0, 130):
    words = {3: "Fizz", 5: "Buzz", 8: "Fuzz"}
    output = get_string(words, i)
    if output == "":
        output = str(i)
    print(output)
