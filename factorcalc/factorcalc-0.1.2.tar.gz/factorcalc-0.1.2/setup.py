import setuptools


setuptools.setup(
    name='factorcalc',
    version='0.1.2',
    author='Eli Harrison',
    author_email='eliharrison89@gmail.com',
    url='https://github.com/CopperyMarrow15/factorcalc',
    description='several (currently 5) modules relating to factor and multiple calculation',
    long_description='''factor.f(integer)
    factor.f(int) -> list of int -- provides a list of all the factors of the first argument

factor.gcf(num1, num2)
    factor.gcf(translatable to int, translatable to int) -> int -- provides the greatest common factor of the integers in the first argument

factor.prime(integer)
    factor.prime(int) -> bool -- checks if the first argument is prime

factor.primes(minimum, maximum)
    factor.primes(int, int) -> list of int -- returns all prime numbers within the range of the first and second arguments including the arguments themselves

mult(number, quantity)
    factorcalc.mult(int, int > 0) -> list of int -- returns a list containing, in order, multiples of the first argument with the second argument being its length
    This module does not relate to factor calculation but to multiple calculation. It has been added beause it might be of use.''',
classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Mathematics'
])
# owo
