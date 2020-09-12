# Autocorrect
![Build](https://github.com/fsondej/autocorrect/workflows/Python%20application/badge.svg)

Spelling corrector in python. Currently supports English, Polish, Turkish, Russian, Ukrainian and Spanish, but you can easily add new languages.

Based on: https://github.com/phatpiglet/autocorrect

# Installation
```bash
pip install autocorrect
```

# Examples
```python
>>> from autocorrect import Speller
>>> spell = Speller()
>>> spell("I'm not sleapy and tehre is no place I'm giong to.")
"I'm not sleepy and there is no place I'm going to."

>>> spell = Speller('pl')
>>> spell('ptaaki latatją kluczmm')
'ptaki latają kluczem'
```

# Speed
```python
%timeit spell("I'm not sleapy and tehre is no place I'm giong to.")
410 µs ± 6.84 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit spell("There is no comin to consiousnes without pain.")
186 ms ± 1.59 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

As you see, for some words correction can take ~200ms. If speed is important for your use case (e.g. chatbot) you may want to use option 'fast':
```python
spell = Speller(fast=True)
%timeit spell("There is no comin to consiousnes without pain.")
381 µs ± 2.18 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```
Now, the correction should always work in microseconds, but words with double typos (like 'consiousnes') won't be corrected.

# Adding new languages
First add special letters in autocorrect/constants.py.

Now, you need a bunch of text. Easiest way is to download wikipedia.
For example for Hindi go to:
https://dumps.wikimedia.org/hiwiki/latest/
and download hiwiki-latest-pages-articles.xml.bz2

```
bzip2 -d hiwiki-latest-pages-articles.xml.bz2
```

After that:

```python
>>> from autocorrect.word_count import count_words
>>> count_words('hiwiki-latest-pages-articles.xml', 'hi')
```

```
tar -zcvf autocorrect/data/hi.tar.gz word_count.json
```

For the correction to work well, you need to cut out rarely used words. You can do it by calling for example:

```python
>>> spell = Speller('hi', threshold=4)
```

To use only words which appeared at least 4 times in wikipedia. You'll have to find the right threshold value empirically. It's best to make a unit test in unit_tests/test.py and see which threshold corrects the most words. After that, you can manually delete all those rare words from the file in hi.tar.gz (it's already sorted so it should be easy).

If you do it, please make a pull request. Good luck!

# Contribute
https://github.com/fsondej/autocorrect

# Todo
- some English words are corrected to implausible versions (see english2 in unit_tests); use English wikipedia
- in double typos we check same words twice
- recount polish wikipedia
