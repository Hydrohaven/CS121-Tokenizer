# My function runs in linear time relative to the amount of characters in the file
# Achieving an O(n) time complexity where n is the number of total characters
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
            
def tokenFrequency(tokens: list[str]) -> dict[str, int]:
    freq = dict()

    for token in tokens:
        if freq.get(token):
            freq[token] += 1
        else:
            freq[token] = 1

    return freq

if __name__ == '__main__':
    filepath: str = input("Please enter a file path to read: ")
    print(tokens := tokenize(filepath))
    print(freq := tokenFrequency(tokens))