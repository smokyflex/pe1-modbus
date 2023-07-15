from setuptools import setup, find_packages

setup(
    name='pe1-modbus',
    version='0.0.0',
    #packages=find_packages(include=['src.ambilite.*', 'test.ambilite.*']),
    packages=find_packages(),

    install_requires=[
        "pymodbus"
    ]
)