from distutils.core import setup

setup(name='autocorrect',
      version='1.0.0',
      packages=['autocorrect'],
      package_data={'autocorrect': ['data/en.tar.gz']},
      description='Spelling Corrector',
      author='Jonas McCallum, Filip Sondej',
      author_email='filipsondej@protonmail.com',
      url='https://github.com/fsondej/autocorrect',
      license='http://www.opensource.org/licenses/mit-license.php',
      classifiers=('Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Natural Language :: Polish',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',),
      keywords='autocorrect spelling corrector')
