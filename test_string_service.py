from string_service import StringService


def test_get_word_frequencies_with_empty_sentence_return_empty_list():
    sentence = ""
    n = 1
    expected_result = []
    result = StringService.get_word_frequencies(sentence, n)
    assert result == expected_result


def test_get_word_frequencies_with_sentence_and_size_of_3_return_valid_list():
    sentence = "baz bar foo foo zblah zblah zblah baz toto bar"
    n = 3
    expected_result = [('zblah', 3), ('bar', 2), ('baz', 2)]
    result = StringService.get_word_frequencies(sentence, n)
    assert result == expected_result
