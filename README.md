# Autocorrect
Spelling corrector in python. Currently supports english and polish, but you can easily add new languages.

Based on: https://github.com/phatpiglet/autocorrect

# Installation
```bash
pip install autocorrect
```

# Examples
```python
>>> from autocorrect import speller
>>> spell = Speller()
>>> spell("I'm not sleapy and tehre is no place I'm giong to.")
"I'm not sleepy and there is no place I'm going to."

>>> spell = Speller(lang='pl')
>>> spell('ptaaki latatją kluczmm')                                         
'ptaki latają kluczem'
```

# Adding new languages
First add special letters in autocorrect/constants.py.

Now, you need a bunch of text. Easiest way is to download wikipedia.
For example for russian go to:
https://dumps.wikimedia.org/ruwiki/latest/ 
and download ruwiki-latest-pages-articles.xml.bz2

```
tar -jxvf ruwiki-latest-pages-articles.xml.bz2
```

After that:

```python
>>> from autocorrect.word_count import count_words
>>> count_words('ruwiki-latest-pages-articles.xml', 'ru')
```

```
tar -zcvf autocorrect/data/ru.tar.gz word_count.json
```

# Speed
```python
%timeit spell('Hey! Mr. Tambourine Man, play a song for me,')
250 µs ± 10.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit spell("I'm not sleapy and tehre is no place I'm giong to.")
410 µs ± 6.84 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit spell("There is no comin to consiousnes without pain.")
186 ms ± 1.59 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

# Contribute
https://github.com/fifimajster/autocorrect

# Todo
- capitalized words shouldn't be corrected into uncapitalized
- some words are corrected to implausible versions (see english2 in unit_tests)
- python2 doesn't support correction with polish special chars