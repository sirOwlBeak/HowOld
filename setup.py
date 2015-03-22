import os

from setuptools import setup, find_packages


about_path = os.path.join(os.getcwd(), 'agetoseconds', '__about__.py')
about = {}
with open(about_path) as fp:
    exec(fp.read(), about)


setup(
    name = about["__title__"],
    version = about["__version__"],
    description = about["__summary__"],
    author = about["__author__"],
    
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 2.7',
    ],
    
    packages = find_packages(),
    
    install_requires = [
        'Click',
    ],
    
    entry_points = '''
        [console_scripts]
        howold=agetoseconds.age2sec:cli
    ''',
)
