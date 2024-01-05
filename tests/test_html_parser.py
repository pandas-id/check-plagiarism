
from lib.html_parser import parse_html_document
import unittest
import requests

class TestCleanDocument(unittest.TestCase):

    def test_document_from_url(self):
        url = 'https://www.google.com/amp/s/www.cnbcindonesia.com/tech/20220325141305-37-326052/mengenal-apa-itu-cookie-browser-dan-cara-mengelolanya/amp'
        html = requests.get(url).text

        document = parse_html_document(html)
        print(document)

        # save clean document
        # with open('clean_html.txt', 'w') as f:
        #     f.write(document)

    def test_html_document(self):
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Dokumen HTML Sederhana</title>
        </head>
        <body>
                <h1>Selamat Datang, di     Dunia HTML!</h1>
            <p>Ini adalah  contoh dokumen HTML sederhana.</p>
            <p>ini <i>italic</i> ku</p>
        </body>
        </html>
        """

        expected = """
Selamat Datang, di     Dunia HTML!
Ini adalah  contoh dokumen HTML sederhana.
ini italic ku
"""
        result = parse_html_document(html)
        self.assertEqual(result, expected)

    def test_html_document_with_tag_body(self):
        html = """
        <body>
                <h1>Selamat Datang, di     Dunia HTML!</h1>
            <p>Ini adalah  contoh dokumen HTML sederhana.</p>
            <p>ini <i>italic</i> ku</p>
        """

        expected = """
Selamat Datang, di     Dunia HTML!
Ini adalah  contoh dokumen HTML sederhana.
ini italic ku
"""
        result = parse_html_document(html)
        self.assertEqual(result, expected)
