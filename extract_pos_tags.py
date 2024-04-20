import sys

def extract_pos_tags(filename):
    pos_tags = set()  # A set to store unique POS tags
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#') and line.strip():  # Ignore comment lines and empty lines
                parts = line.split('\t')  # Split the line into columns
                if len(parts) > 3:  # Ensure there are enough parts
                    pos_tag = parts[3]  # Get the POS tag from the fourth column
                    pos_tags.add(pos_tag)  # Add the POS tag to the set
    return pos_tags

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python extract_pos_tags.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    unique_pos_tags = extract_pos_tags(filename)
    print("Unique POS tags:", unique_pos_tags)
    print("Number of unique POS tags:", len(unique_pos_tags))
