"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    words=title.split()
    capitalized_words=[word.capitalize() for word in words]
    capitalize_sentence=' '.join(capitalized_words)
    return capitalize_sentence


    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """
    
def check_sentence_ending(sentence):
    words=sentence.split()
    length=len(words)
    end=words[length-1]
    lend=len(end)
    if end[lend-1]==".":
        return True
    else:
        return False


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """
    new_sentence=sentence.replace(old_word,new_word)
    return new_sentence

