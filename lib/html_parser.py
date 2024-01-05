# 2023-12-31

from bs4 import BeautifulSoup
from bs4.element import Comment, Tag
import re

def parse_html_document(document: str) -> dict[str, str]:
    """
    Function to removing tag from html document

    :return: title and plaintext of body with no html tag and no whitespace (\t\r\n)
    """

    title = ''

    html: Tag = BeautifulSoup(document, 'html.parser')

    if html.find('title'):
        title = html.find('title').text

    if html.body:
        html = html.body

    useless_tags = html.find_all([
        'script', 'style', 'meta', 'include',
        'button', 'form'
    ])

    for tag in useless_tags:
        tag.decompose()

    for element in html(text=lambda text: isinstance(text, Comment)):
        element.extract()

    # make sure there are no more html tags
    plaintext = re.sub('<[^>]+>', '', html.text)

    return {
        'title': title,
        'body': plaintext
    }
