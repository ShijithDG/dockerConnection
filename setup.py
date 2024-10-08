from setuptools import setup, find_packages

setup(
    name='simple_calculator',
    version='0.1',
    packages=find_packages(),
    description='A simple calculator for basic operations',
    author='Shijith',
    author_email='shijith.pk@datagrokr.com',
    install_requires=[],  # List dependencies here, if any
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
