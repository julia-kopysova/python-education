from typing import List


class SentenceIterator:
    """
    Class represents Iterator for Sentence
    Attributes:
        _string: str: string that will be operated
        length: int: amount of words in string
    Properties:
        words(self): List[str]: returns list of words in string
    Methods:
        __iter__(self): returns itself
        __next__(self): raises Error
    """
    def __init__(self, string: str) -> None:
        """
        Initializes Sentence Iterator
        If string is not a sentence, raises ValueError
        If string is not str, raises TypeError
        :param string: str: string for operation
        :return: None
        """
        if type(string) is not str:
            raise TypeError
        elif string[-1] != "." and string[-1] != "!" and string[-1] != "?":
            raise ValueError
        else:
            self._string: str = string
        self.length: int = len(self.words)

    @property
    def words(self) -> List[str]:
        """
        Property for splitting a string into a list word by word
        :return: List[str]: list of words from sentence
        """
        return self._string.split()

    def __iter__(self):
        """
        Returns itself
        :return:
        """
        return self

    def __next__(self) -> str:
        """
        Raises StopIteration if next elements doesn't exist
        :return: str
        """
        if self.length > 0:
            word_from_list = self.words[len(self.words) - self.length]
            self.length -= 1
            return word_from_list
        raise StopIteration


class Sentence:
    """
    Class represents container for Sentence
    Attributes:
        _string: str: string that will be operated
        length: int: amount of words in string
    Properties:
        words(self): List[str]: returns list of words in string
        other_chars(self): List[str]: returns list of other chars
    Methods:
        __iter__(self): returns iterator
        _words(self): returns lazy iterator
        __repr__(self): string representation of object
        __len__(self): amount of words
        __getitem__(self, index): returns word by index
    """
    def __init__(self, string: str) -> None:
        """
        Initializes Sentence
        Receives string
        If string is not a sentence, raises ValueError
        If string is not str, raises TypeError
        :param string: str: string for operation
        :return: None
        """
        if type(string) is not str:
            raise TypeError
        elif string[-1] != "." and string[-1] != "!" and string[-1] != "?":
            raise ValueError
        else:
            self._string = string
        self.length = len(self.words)

    def _words(self):
        """
        Realizes lazy iterator
        :return: generator
        """
        list_words = self._string.split()
        for i in list_words:
            yield i

    @property
    def words(self) -> List[str]:
        """
        Property for splitting a string into a list word by word
        :return: List[str]: list of words from sentence
        """
        return self._string.split()

    @property
    def other_chars(self) -> List[str]:
        """
        Property for finding other chars in the string
        :return: List[str]: list of other chars from sentence
        """
        list_chars = []
        for i, c in enumerate(self._string):
            if not c.isalpha():
                list_chars.append(c)
        return list_chars

    def __repr__(self) -> str:
        """
        String representation
        :return: str
        """
        return f"Sentence: {self._string} (words={len(self.words)}, other_chars={len(self.other_chars)})"

    def __iter__(self):
        """
        Returns iterator
        """
        return SentenceIterator(self._string)

    def __len__(self) -> int:
        """
        Returns amount of words in string
        """
        return len(self.words)

    def __getitem__(self, index):
        """
        Returns word by index
        :param index: number of position the word in string
        :return: str
        """
        if isinstance(index, slice):
            return self.words[index.start:index.stop:index.step]
        else:
            if index >= len(self):
                raise IndexError
            else:
                return self.words[index]


if __name__ == "__main__":
    # Create sentence
    my_sentence = Sentence("Hello word!")
    print(my_sentence)
    sen = iter(my_sentence)
    print(type(sen))
    # Get word by index
    print(my_sentence[0])
    # Test method _words()
    print(type(my_sentence._words()))
    print(next(my_sentence._words()))
    print(my_sentence.words)
    print(my_sentence.other_chars)
    # Slice of sentence
    print(my_sentence[:])
    # Loop
    for word in my_sentence:
        print(word)
