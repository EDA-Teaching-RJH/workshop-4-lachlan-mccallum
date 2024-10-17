def main():
    s = input("give your name in camel case ")
    print("snake_case ", end="")

    for c in s:
        if c.islower():
            print(c,end="")
        elif c.isupper():
            print ("_", c.lower(), end = "", sep = "")
    print()

main()