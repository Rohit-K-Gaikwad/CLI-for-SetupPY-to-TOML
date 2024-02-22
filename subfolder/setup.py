from setuptools import setup

setup(
    name='my_package',
    version='0.1',
    description='A sample Python package',
    author='John Doe',
    author_email='jdoe@example.com',
    packages=['my_package'],
    install_requires=[
        'numpy>=1.20',
        'pandas>=1.3',
    ],
)