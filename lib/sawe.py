# created: 2023-12-30
# modified: 2023-12-30

"""
SAWE (Simple Automatic Word Extracted algoritm)

Automatic word extraction from individual document wothout complex calculation, just extract words.
Example:

Document: Tahun 2023-12-30,saya mau belajar Bahasa Pemrogaman Python dan Algoritma Similarity!.

* document after folding to lowercase
Document: tahun 2023-12-30,saya mau belajar bahasa pemrogaman python dan algoritma similarity!.

* document after punctations and digits have been removing
Document: tahun            saya mau belajar bahasa pemrogaman python dan algoritma similarity

* document after double spacing and whitespace (\n\t\r) has been removing
Document: tahun saya mau belajar bahasa pemrogaman python dan algoritma similarity

* split words by spacing (tokenizing)
List of words: ['tahun', 'saya', 'mau', 'belajar', 'bahasa', 'pemrogaman', 'python', 'dan', 'algoritma', 'similarity']

* list words after stopwords and shortword has been removing
List of words: ['tahun', 'belajar', 'bahasa', 'pemrogaman', 'python', 'algoritma', 'similarity']
"""

import re
from nltk.corpus import stopwords as get_stopwords
from nltk import word_tokenize

# improve code readability
Text = str
Word = str

class Sawe:

    def __init__(self,
                 document: Text,
                 stopwords = None,
                 min_length: int = 4
                ) -> None:

        """
        :param document: document will be extracted
        :param stopwords: words that will be ignored from the extraction process
        :param min_length: minimum length of word will be extracted
        """

        self.document: Text = document

        if stopwords:
            self.stopwords = stopwords
        else:
            self.stopwords = get_stopwords.words('indonesian')
        self.min_length: int = min_length

        # variable to be extracted from the provided document
        self.tokens: list[Word]

    def _clean_document(self):
        """
        function to folding document to lowercase and
        remove punctuation and digits

        :return: lowercase document with no punctuation and digits
        """
        # remove punctations and digits
        clean = re.sub('[^\w\s]+|\d', ' ', self.document.lower())
        # removing double spacing
        clean = ' '.join(clean.split())
        return clean

    def _extract_tokens(self):
        """
        method to generate tokens from document, filter it.
        """

        tokens = word_tokenize(self._clean_document())

        # filtering keyword
        tokens = list(filter(self._ignored_word, tokens))
        return tokens

    def _ignored_word(self, word: str):
        """
        function to filter stopwords and minimum words length
        """
        if (not word in self.stopwords) and (len(word) >= self.min_length):
            return True

    def get_tokens(self):
        """
        Method to fetch tokens

        :return: list of tokens
        """
        return self._extract_tokens()


if __name__ == "__main__":
    url = 'https://pandasid.blogspot.com/2020/05/cara-mendapatkan-cookie-facebook-dengan.html'
    # text = get_text.from_url(url)
    text = open('./text1.txt', 'r').read()

    text = 'Tahun 2023-12-30,saya mau belajar Bahasa Pemrogaman Python dan Algoritma Similarity!.'

    sake = Sawe(text)
    tokens = sake.get_tokens()
    print(tokens)
