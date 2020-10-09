# Autocorrect
![build](https://github.com/fsondej/autocorrect/workflows/build/badge.svg)

Spelling corrector in python. Currently supports English, Polish, Turkish, Russian, Ukrainian, Czech and Spanish, but you can easily add new languages.

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

For the correction to work well, you need to cut out rarely used words. First, in test_all.py, write test words for your language, and add them to optional_language_tests the same way as it's done for other languages. It's good to have at least 30 words. Now run:
```
python ./test_all.py find_threshold hi
```
 and see which threshold value has the least badly corrected words. After that, manually delete all the words with less occurences than the threshold value you found, from the file in hi.tar.gz (it's already sorted so it should be easy).

If you do it, please make a pull request. Good luck!

# Contribute
https://github.com/fsondej/autocorrect

# Todo
- in double typos we check same words twice
