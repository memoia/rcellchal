Problem 1
---------

Run `make` to run interactively.

I'm not at all happy with the run time. Long words are pretty
much impossible using the strategy I implemented.

[Someone](http://blog.notdot.net/2007/10/Damn-Cool-Algorithms-Part-3-Anagram-Trees)
figured out how to do this with trees. Considering how slow my
solution can get, maybe next time I'll try this approach.

### Summary

```
Given a word from a wordlist, find one anagram with the most number of
words (from the given wordlist) and one anagram with just  two words in
them (if one exists). If no anagrams exist with two or more words, the
program should print an empty string for both cases.

Example: For the word incredible, "bile cinder" is one anagram with just two
words. for the word infinite, "net if I in" is one anagram with the
most number of words. (you can just print one of the many, if there are
many such with the same number of words).

In the word list, ignore single character words.
```

### To use in another application

```python
from anagram import (AnagramSolver, WordList)

solver = AnagramSolver(WordList('words.txt'))
foo = solver.find_all('howdy')
for i in range(5):
    foo.next()

bar = solver.two_words('incredible')
```
