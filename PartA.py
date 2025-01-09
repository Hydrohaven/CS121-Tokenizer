def tokenize(filepath: str) -> list[str]:
    tokens: list[str] = list()
    current_token = ''

    # Read parameter filepath
    with open(filepath, 'r', encoding='utf-8') as file:
        # Iterate through file character-by-character until EOF
        while char := file.read(1).lower():
            # Not whitespace == add char to current token, else add to token list
            if not char.isspace() and char.isalnum():
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''

        # Adds token at EOF if its truthy
        if current_token: 
            tokens.append(current_token) 

    return tokens
            

if __name__ == '__main__':
    filepath: str = input("Please enter a file path to read: ")
    print(tokens := tokenize(filepath))