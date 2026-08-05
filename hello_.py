def main():
    name = input("Enter a number: ")
    print(hello(name))

def hello(to="world"):
    return f"hello,{to}"

if __name__ == "__main__":
    main()
