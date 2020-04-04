# Autocorrect
Spelling corrector in python. Currently supports English, Polish, Turkish, Russian and Ukrainian, but you can easily add new languages.

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

>>> spell = Speller(lang='pl')
>>> spell('ptaaki latatją kluczmm')                                         
'ptaki latają kluczem'
```

# Adding new languages
First add special letters in autocorrect/constants.py.

Now, you need a bunch of text. Easiest way is to download wikipedia.
For example for Spanish go to:
https://dumps.wikimedia.org/eswiki/latest/
and download eswiki-latest-pages-articles.xml.bz2

```
tar -jxvf eswiki-latest-pages-articles.xml.bz2
```

After that:

```python
>>> from autocorrect.word_count import count_words
>>> count_words('eswiki-latest-pages-articles.xml', 'ru')
```

```
tar -zcvf autocorrect/data/es.tar.gz word_count.json
```

# Speed
```python
%timeit spell("I'm not sleapy and tehre is no place I'm giong to.")
410 µs ± 6.84 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit spell("There is no comin to consiousnes without pain.")
186 ms ± 1.59 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
```

# Contribute
https://github.com/fifimajster/autocorrect

# Todo
- some words are corrected to implausible versions (see english2 in unit_tests)
- python2 doesn't support correction with polish special chars
- option to disable double typer for speed
- it looks that loading spellers multiple times may be leaking memory