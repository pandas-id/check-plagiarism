# created: 2024-01-01

from lib.sawe import Sawe
from lib.html_parser import clean_html

import unittest
import requests


class TestSaweCleanDocument(unittest.TestCase):

    def test_from_clean_html(self):
        # just see the output
        url = 'https://www.google.com/amp/s/www.cnbcindonesia.com/tech/20220325141305-37-326052/mengenal-apa-itu-cookie-browser-dan-cara-mengelolanya/amp'
        text = requests.get(url).text
        document = clean_html(text)
        sawe = Sawe(document)
        result = sawe._clean_document()
        print(result)

    def test_with_normal_document(self):
        document = 'Tahun 2023-12-30,saya mau belajar Bahasa Pemrogaman Python dan Algoritma Similarity!.'
        sawe = Sawe(document)
        result = sawe._clean_document()
        expected = 'tahun saya mau belajar bahasa pemrogaman python dan algoritma similarity'
        self.assertEqual(result, expected)

    def test_with_document_from_file(self):
        document = open('document.txt', 'r').read()
        sawe = Sawe(document)
        result = sawe._clean_document()
        expected = 'pemrograman adalah kunci untuk memecahkan berbagai masalah dengan ide kreatif bahasa python memberikan fleksibilitas dalam pengembangan aplikasi dengan dukungan komunitas yang besar belajar python menjadi lebih menyenangkan dan terbuka untuk semua teknologi terus berkembang memungkinkan inovasi yang luar biasa dalam berbagai bidang'
        self.assertEqual(result, expected)

class TestSaweExtractTokens(unittest.TestCase):

    def test_with_normal_document(self):
        document = 'Tahun 2023-12-30,saya mau belajar Bahasa Pemrogaman Python dan Algoritma Similarity!.'
        sawe = Sawe(document)
        result = sawe._extract_tokens()
        expected = ['belajar', 'bahasa', 'pemrogaman', 'python', 'algoritma', 'similarity']
        self.assertEqual(result, expected)
