import sys

def extract_pos_tags(filename):
    pos_tags = set()  
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('#') and line.strip():  
                parts = line.split('\t') 
                if len(parts) > 3: 
                    pos_tag = parts[3]  
                    pos_tags.add(pos_tag)  
    return pos_tags

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python extract_pos_tags.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    unique_pos_tags = extract_pos_tags(filename)
    sorted_pos_tags = sorted(unique_pos_tags) 
    print("Unique POS tags:", sorted_pos_tags)
    print("Number of unique POS tags:", len(sorted_pos_tags))
