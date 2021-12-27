from setuptools import find_packages, setup

setup(
    name='iloveflask',
    packages=find_packages(include=['iloveflask','raport']),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['python-docx', 'pytest-runner'],
    tests_require=['python-docx', 'pytest==4.6'],
    test_suite='tests',
)