#!/usr/bin/env python2.7 -i

import os
import logging
from collections import defaultdict
from itertools import (chain, combinations, ifilter)


logging.basicConfig(level=logging.DEBUG)

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = logging.getLogger(__name__)


class Word(object):
    def __init__(self, characters):
        self.raw = filter(lambda c: c.isalpha(), characters)
        self._letters_counts = None
        self._letters = None

    @classmethod
    def join(cls, *words):
        return Word(''.join([x.raw for x in words]))

    @property
    def letters_counts(self):
        if self._letters_counts is None:
            self._letters_counts = self._build_letters()
        return self._letters_counts

    @property
    def letters(self):
        if self._letters is None:
            self._letters = set([x[0] for x in self.letters_counts])
        return self._letters

    def _build_letters(self):
        letters = defaultdict(int)
        for letter in self.raw:
            letters[letter.lower()] += 1
        return set(letters.items())

    def anagram_of(self, subject_word):
        return self.letters_counts == subject_word.letters_counts

    def subset_of(self, subject_word):
        return self.letters <= subject_word.letters

    def __repr__(self):
        return self.raw

    def __len__(self):
        return len(self.raw)


class WordList(list):
    def __init__(self, path, *args, **kw):
        super(list, self).__init__(self, *args, **kw)
        LOG.debug('Loading {}'.format(path))
        with open(path, 'r') as fd:
            for line in fd:
                line = line.strip()
                if len(line) > 1:  # "ignore the single-character words"
                    self.append(Word(line))


class AnagramSolver(object):
    def __init__(self, word_list):
        self.word_list = word_list

    def _powerset(self, words):
        # gross
        return chain.from_iterable(combinations(words, r)
                                   for r in xrange(len(words) + 1))

    def _words_in(self, subject):
        return filter(lambda w: w.subset_of(subject), self.word_list)

    def _with_len(self, size, iterable):
        return ifilter(lambda t: sum(map(len, t)) == size, iterable)

    def _having_anagram_for(self, subject, iterable):
        return ifilter(lambda t: Word.join(*t).anagram_of(subject), iterable)

    def find_all(self, characters):
        # 1. find all words that can (partially) compose subject.
        # 2. generate power set of result.
        # 3. filter those items that when concatenated completely compose subj.
        subj = Word(characters)
        words = self._with_len(len(subj), self._powerset(self._words_in(subj)))
        return self._having_anagram_for(subj, words)

    def two_words(self, characters):
        for result in self.find_all(characters):
            if len(result) == 2:
                return result

    def most_words(self, characters):
        # slow, gross, wrong. :(
        last_count = 0
        max_count = len(characters) / 2
        max_loops = len(self.word_list) * (2 ** len(characters))
        for result in self.find_all(characters):
            if max_loops == 0 or last_count >= max_count:
                break
            last_count = len(result)
            max_loops -= 1
        return result

    def two_and_most(self, chars):
        print '2-word anagram of {!r}: {}'.format(chars, self.two_words(chars))
        print 'Anagram with most words: {}'.format(self.most_words(chars))


if __name__ == '__main__':
    solver = AnagramSolver(WordList(os.path.join(HERE, 'words.txt')))
    print """Try these:
        foo = solver.find_all('howdy')
        for i in range(5): foo.next()
        solver.two_and_most('infinite')
        print solver.two_words('incredible')
        print solver.most_words('hello')
        """
