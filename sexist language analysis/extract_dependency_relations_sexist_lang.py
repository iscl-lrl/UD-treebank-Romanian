import sys

def extract_dependency_relations_sexist_lang(filename):
    relations = []  
    collecting = False  
    sentence_relations = [] 

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#'):
                if 'language_type = sexist' in line:
                    collecting = True  
                    if sentence_relations:
                        relations.append(sentence_relations)
                        sentence_relations = []  # Reset for the next sentence
            elif line.strip() == "":
                collecting = False 
            elif collecting and not line.startswith('#'):
                parts = line.split('\t')
                if len(parts) > 7:
                    # Extract ID, form (word), dependency head, and relation
                    token_id = parts[0]
                    word = parts[1]
                    head = parts[6]
                    relation = parts[7]
                    sentence_relations.append((token_id, word, head, relation))

    return relations

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: extract_dependency_relations_sexist_lang <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    deps = extract_dependency_relations_sexist_lang(filename)
    print("Extracted Dependency Relations Sexist Language Analysis:")
    for relation in deps:
        print(relation)
