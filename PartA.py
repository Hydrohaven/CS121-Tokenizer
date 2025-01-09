# My function runs in linear time relative to the amount of characters in the file
# Achieving an O(n) time complexity where n is the number of total characters
def tokenize(filepath: str) -> list[str]:
    tokens: list[str] = list()
    current_token = ''

    # TODO: ADD ERROR HANDLING
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

# My function runs in linear time relative to the total amount of tokens
# Achieving a time complexity of O(n), where n is the total number of tokens
def tokenFrequency(tokens: list[str]) -> dict[str, int]:
    freq = dict()

    for token in tokens:
        if freq.get(token):
            freq[token] += 1
        else:
            freq[token] = 1

    return freq

# My function runs in loglinear time relative to the amount of keys
# Achieving a run time complexity of O(n log n) where n is 
#  the number of items in the dictionary with and the sorting
#  algorithm pee
def printFrequency(frequency: dict[str, int]) -> None:
    ordered_keys = [k for k, _ in sorted(list(frequency.items()), key=lambda f: f[1], reverse=True)]
    for key in ordered_keys:
        print(key, '=>', frequency[key])

if __name__ == '__main__':
    filepath: str = input("Please enter a file path to read: ")
    print(tokens := tokenize(filepath))
    print(freq := tokenFrequency(tokens))
    printFrequency(freq)