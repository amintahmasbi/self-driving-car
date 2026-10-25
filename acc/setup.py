from setuptools import setup


setup(
    name='acc',
    version='0.1.1',
    url='http://github.com/udacity/self-driving-car',
    license='MIT',
    author='Udacity ND013 members',
    description='Adaptive Cruise Control',
    long_description=open('README.md').read() + '\n',
    # Run the tests with: pip install -e .[test] && pytest
    extras_require={'test': ['pytest>=9.0.3', 'coveralls', 'flake8']},
    py_modules=['acc'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
