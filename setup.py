from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as arq:
    readme = arq.read()

setup(
    name='codecanvas',
    version='1.1.0',
    license='MIT License',
    author='Jean Branco',
    author_email='jeanlourencobranco13@gmail.com',
    description='CodeCanvas é um pacote Python que permite adicionar estilos ao console.',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='code canvas',
    packages=find_packages()
)
