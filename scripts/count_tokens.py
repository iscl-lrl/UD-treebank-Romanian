import sys

def count_tokens_and_unique_tokens(filename):
    tokens = set()  # A set to store unique tokens
    total_tokens = 0  # Counter for total number of tokens
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#') and line.strip():  
                parts = line.split('\t') 
                if len(parts) > 1:  
                    token = parts[1]  
                    tokens.add(token)  
                    total_tokens += 1  

    return total_tokens, len(tokens)  

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python count_tokens.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    total_tokens, unique_tokens_count = count_tokens_and_unique_tokens(filename)
    print("Total number of tokens:", total_tokens)
    print("Total number of unique tokens:", unique_tokens_count)