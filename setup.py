from setuptools import find_packages, setup

setup(
    name='iloveflask',
    packages=find_packages(include=['iloveflask','report']),
    version='0.1.1',
    description='iloveflask is a Python library to collect functions that help a flask developer generate reports, config files and repeat code.',
    author='Zekri Sidi Mohamed Hicham',
    license='MIT',
    install_requires=[],
    setup_requires=['python-docx', 'pytest-runner'],
    tests_require=['python-docx', 'pytest==4.6'],
    test_suite='tests',
)