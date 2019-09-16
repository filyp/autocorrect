===========
autocorrect
===========
Spelling corrector in python. Currently supports english and polish, but you can easily add new languages.

Based on: https://github.com/phatpiglet/autocorrect

Installation
============
.. code-block:: bash

    pip install autocorrect

Examples
========
.. code-block:: python

    >>> from autocorrect import Speller
    >>> spell = Speller(lang='pl')
    >>> spell('ptaaki latatją kluczmm')                                         
    'ptaki latają kluczem'

    >>> spell = Speller(lang='en')
    >>> spell("I'm not sleapy and tehre is no place I'm giong to.")
    "I'm not sleepy and there is no place I'm going to."

Adding new languages
========
First add special letters in autocorrect/constants.py.

Now, you need a bunch of text. Easiest way is to download wikipedia.
For example for russian go to:
https://dumps.wikimedia.org/enwiki/latest/ 
and download ruwiki-latest-pages-articles.xml.bz2

.. code-block:: bash

    tar -jxvf ruwiki-latest-pages-articles.xml.bz2

After that:

.. code-block:: python

    >>> from autocorrect.word_count import count_words
    >>> count_words('ruwiki-latest-pages-articles.xml', 'ru')

.. code-block:: bash

    tar -zcvf autocorrect/data/ru.tar.gz word_count.json

Contribute
==========
https://github.com/fifimajster/autocorrect

Todo
==========
Python2 doesn't support correction with polish special chars.