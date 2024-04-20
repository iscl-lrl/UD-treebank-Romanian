import sys

def extract_deprels(filename):
    deprels = set()  # A set to store unique dependency relations
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#') and line.strip():  # Ignore comment lines and empty lines
                parts = line.split('\t')  # Split the line into columns
                if len(parts) > 7:  # Ensure there are enough parts to include column 8
                    deprel = parts[7]  # Get the dependency relation from the eighth column
                    deprels.add(deprel)  # Add the dependency relation to the set
    return deprels

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python extract_deprels.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    unique_deprels = extract_deprels(filename)
    sorted_deprels = sorted(unique_deprels)  # Sort the dependency relations alphabetically
    print("Unique dependency relations:", sorted_deprels)
    print("Number of unique dependency relations:", len(sorted_deprels))