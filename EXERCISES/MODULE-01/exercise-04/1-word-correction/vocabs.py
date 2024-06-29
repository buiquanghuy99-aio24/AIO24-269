def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words

vocabs = load_vocab(file_path='EXERCISES/MODULE-01/exercise-04/1-word-correction/vocab.txt')