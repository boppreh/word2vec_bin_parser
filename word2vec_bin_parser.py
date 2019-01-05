import struct
import math

def read_until(open_file, byte):
    while True:
        char = open_file.read(1)
        if char == b' ':
            break
        yield char

def bin2stream(bin_file_path):
    """
    Given the path of a .bin Word2Vec embedding, returns a stream/generator
    of pairs (word, vector).
    """
    with open(bin_file_path, 'rb') as f:
        # The file starts with two ASCII numbers, separated by a space and
        # ending with a newline. The first is the number of words, the second
        # is the number of dimensions that each vector has.
        first_line = f.readline()
        n_words, n_dim = map(int, first_line.split())

        for n_word in range(n_words):
            # Each word starts with the word itself, followed by a space...
            word = b''.join(read_until(f, ' ')).decode('utf-8')
            # ... followed by `n_dim` floats. And that's it!
            vector = struct.unpack('f' * n_dim, f.read(n_dim * 4))
            yield word, vector

def get_distance(vectorA, vectorB):
    total = 0
    for a, b in zip(vectorA, vectorB):
        total += (a - b) ** 2
    return math.sqrt(total)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print('Usage: parse_bin_vectors.py GoogleNews-vectors-negative300.bin')
    else:
        for path in sys.argv[1:]:
            for word, vector in bin2stream(path):
                print(word, vector)