def main():
    def getData(n):
        numbers = []
        for x in range(n):
            print
            "Enter value", x, ":",
            value = input()
            numbers.append(value)
        return numbers

    main()