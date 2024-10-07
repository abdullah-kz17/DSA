import re

def split_camel_case(text):
    # Split based on uppercase letters, while keeping the letter itself in the split
    return ' '.join(re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)', text)).lower()

def combine_camel_case(words, type):
    words = words.split()
    if type == 'C':  # Class - capitalize each word, including the first one
        return ''.join(word.capitalize() for word in words)
    elif type == 'V':  # Variable - lowercase the first word, capitalize subsequent
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    elif type == 'M':  # Method - same as variable but with () at the end
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:]) + '()'

def process_input(line):
    operation, type, data = line.split(';')
    
    if operation == 'S':  # Split operation
        if type == 'M':  # For method, remove the parentheses before splitting
            data = data[:-2]
        print(split_camel_case(data))
    
    elif operation == 'C':  # Combine operation
        print(combine_camel_case(data, type))

def main():
    import sys
    # Reading all input from stdin
    inputs = sys.stdin.read().strip().splitlines()
    
    # Process each input line
    for line in inputs:
        process_input(line)

if __name__ == "__main__":
    main()
