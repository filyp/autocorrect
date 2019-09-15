from distutils.core import setup

setup(name='autocorrect',
      version='0.3.1',
      packages=['autocorrect'],
      package_data={'autocorrect': ['words.bz2']},
      description='Python 3 Spelling Corrector',
      author='Jonas McCallum',
      author_email='jonasmccallum@gmail.com',
      url='https://github.com/fifimajster/autocorrect',
      license='http://www.opensource.org/licenses/mit-license.php',
      classifiers=('Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',),
      keywords='autocorrect spelling corrector')
