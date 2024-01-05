# created: 2024-01-01

from .sawe import Sawe
from math import sqrt

import logging

from collections import Counter


logger = logging.getLogger(__name__)

def cosine_similarity(first: str, second: str):
    """
    Cosine similarity

    calculate the degree of similarity of two documents
    """

    # vektors: list[tuple[int, int]] = []
    vektors = {}

    logger.debug(f'extract token from first document')
    first_tokens = Sawe(first).get_tokens()
    logger.debug(f"number of tokens extracted from document: {len(first_tokens)}")

    logger.debug(f'extract token from second document')
    second_tokens = Sawe(second).get_tokens()
    logger.debug(f"number of tokens extracted from second document: {len(second_tokens)}")

    logger.debug(f'extract token from second document')
    second_tokens = Sawe(second).get_tokens()
    logger.debug(f"number of tokens extracted from second document: {len(second_tokens)}")

    queries = set(first_tokens + second_tokens)
    logger.debug(f"number queries: {len(queries)}")

    for query in queries:
        # vektors.append((
        #     tokens_doc_1.count(keyword),
        #     tokens_doc_2.count(keyword)
        # ))

        vektors[query] = (
            first_tokens.count(query),
            second_tokens.count(query)
        )

    logger.debug('calculate cosine similarity')
    numerator = sum([vektor[0] * vektor[1] for vektor in vektors.values()])

    a_sqrt = sqrt(sum([ v[0]**2 for v in vektors.values() ]))
    b_sqrt = sqrt(sum([ v[1]**2 for v in vektors.values() ]))

    denominator = a_sqrt * b_sqrt

    try:
        return numerator / denominator
    except ZeroDivisionError:
        return 0
