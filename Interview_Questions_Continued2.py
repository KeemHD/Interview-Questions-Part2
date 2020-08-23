#8/21/21
#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given a string that may represent a number, determine if it is a number.
# Here's some of examples of how the number may be presented:
#"123" # Integer
#"12.3" # Floating point
#"-123" # Negative numbers
#"-.3" # Negative floating point
#"1.5e5" # Scientific notation
#Here's some examples of what isn't a proper number:
#"12a" # No letters
#"1 2" # No space between numbers
#"1e1.2" # Exponent can only be an integer (positive or negative or 0)
#Scientific notation requires the first number to be less than 10,
# however to simplify the solution assume the first number can be greater than 10.
# Do not parse the string with int() or any other python functions.


def parse_number(s):
    # Fill this in.
    print(s)

    neg_count = 0
    e_count = 0
    dot_count = 0

    for n in s:
        if neg_count <= 1 and e_count <= 1 and dot_count <= 1:
            if n == "-":
                neg_count+=1
            elif n == ".":
                dot_count+=1
            elif n == "e":
                e_count+=1
                dot_count = 1

            elif not n.isnumeric():
                return False

        else:
            return False

    return True

print("Determine if number 8-21")
print("<-----------------START--------------<DONE")
print(parse_number("12.3"))
# True

print(parse_number("12a"))
# False
print("<-----------------END--------------<")