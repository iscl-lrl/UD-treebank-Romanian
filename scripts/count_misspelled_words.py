import sys

def count_misspelled_words(filename):
    misspelled_count = 0  
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#') and line.strip():  
                parts = line.split('\t')  
                if len(parts) > 9:  
                    misc_column = parts[9]  
                    if 'CorrectForm=' in misc_column:  
                        misspelled_count += 1 
    return misspelled_count

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python count_misspelled_words.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    misspelled_words_count = count_misspelled_words(filename)
    print("Total number of misspelled words:", misspelled_words_count)
