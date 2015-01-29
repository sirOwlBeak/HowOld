from setuptools import setup, find_packages

setup(
    name='a2s',
    version='1.0',
    description='calculates your age in seconds',
    author='sirOwlBeak',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        a2s=agetoseconds.a2s:cli
    ''',
)
