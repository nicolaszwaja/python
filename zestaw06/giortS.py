# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    s = input().strip()

    # Define a custom sorting key function
    def custom_sort(char):
        if char.islower():
            return (1, char)
        elif char.isupper():
            return (2, char)
        elif char.isdigit() and int(char) % 2 != 0:
            return (3, char)
        elif char.isdigit() and int(char) % 2 == 0:
            return (4, char)

    # Sort the string using the custom sorting key
    sorted_string = ''.join(sorted(s, key=custom_sort))

    # Output the sorted string
    print(sorted_string)
