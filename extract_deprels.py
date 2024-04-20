import sys

def extract_deprels(filename):
    deprels = set()  # A set to store unique dependency relations
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#') and line.strip():  
                parts = line.split('\t')  
                if len(parts) > 7:  
                    deprel = parts[7]  
                    deprels.add(deprel)  
    return deprels

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python extract_deprels.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    unique_deprels = extract_deprels(filename)
    sorted_deprels = sorted(unique_deprels)  
    print("Unique dependency relations:", sorted_deprels)
    print("Number of unique dependency relations:", len(sorted_deprels))
