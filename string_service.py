from collections import Counter
from typing import List


class StringService:

    @classmethod
    def get_word_frequencies(cls, sentence: str, n: int) -> List[str]:
        """
        Given a sentence and a number n, returns a list of size n where each element
        contains a word and the frequency of that word in the sentence. The list is sorted
        by decreasing frequency and alphabetical order in case of tie.
        """
        words = sentence.split()
        frequency_counts = Counter(words)
        sorted_frequencies = sorted(
            frequency_counts.items(),
            key=lambda word_count: (-word_count[1], word_count[0])
        )
        return sorted_frequencies[:n]
