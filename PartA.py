import sys

# My function runs in linear time relative to the amount of characters in the file
# Achieving an O(n) time complexity where n is the number of total characters
def tokenize(filepath: str) -> list[str]:
    tokens: list[str] = list()
    current_token = ''

    try:
        # Read parameter filepath
        with open(filepath, 'r', encoding='utf-8') as file:
            # Iterate through file character-by-character until EOF
            while char := file.read(1).lower():
                # If whitespace, not alphanumeric, or isnt english, add token, else build token
                if char.isspace() or not char.isalnum() or not char.isascii():
                    # Checks for alphanumeric + english language character (skips bad input)
                    if current_token:
                        tokens.append(current_token)
                        current_token = ''
                else:
                    current_token += char
                    

            # Adds token at EOF if its truthy
            if current_token: 
                tokens.append(current_token) 
    except FileNotFoundError as e:
        print('File does not exist, please try again:', e)

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
#  algorithm (timsort) compares items log n times 
def printFrequency(frequency: dict[str, int]) -> None:
    ordered_keys = [k for k, _ in sorted(frequency.items(), key=lambda f: (-f[1], f[0]))]
    for key in ordered_keys:
        print(key, '=>', frequency[key])

if __name__ == '__main__':
    # Retrieves 2nd argument (filepath) after py command
    filepath: str = sys.argv[1]
    tokens = tokenize(filepath)
    if tokens:
        freq = tokenFrequency(tokens)
        printFrequency(freq)
    