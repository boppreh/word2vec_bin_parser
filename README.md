# word2vec_bin_parser
Tiny Python script for parsing Word2Vec .bin embeddings.

Interested in running analyses on Word2Vec embeddings? Maybe you searched for a pre-trained embedding and found the 3.5GB [GoogleNews-vectors-negative300.bin](https://drive.google.com/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download) from [https://code.google.com/archive/p/word2vec/](https://code.google.com/archive/p/word2vec/)? Stuck with a binary file and don't want to download a large machine learning library just to look at the vectors?

Your problems are over! Introducing `word2vec_bin_parser`, a tiny, tiny Python file for reading those monstrosities. You can use it as a library (`bin2stream(path)`), or a converter (`word2vec_bin_parser file.bin`). Because it's Python it's very slow, but feel free to look up the tiny source code and adapt into your program.