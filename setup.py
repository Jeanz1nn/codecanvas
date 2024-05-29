from setuptools import setup, find_packages

with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    name='codecanvas',
    version='1.0.0',
    license='MIT License',
    author='Jean Branco',
    author_email='jeanlourencobranco13@gmail.com',
    description='CodeCanvas é um pacote Python que permite adicionar estilo e formatação visual ao console.',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='code canvas',
    packages=find_packages()
)
