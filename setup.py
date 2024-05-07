from setuptools import setup, find_packages

setup(
    name='torchresearch',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torch',
    ],
    author='zungwooker',
    author_email='zungwooker@gmail.com',
    description='A set of tools for PyTorch research.',
    license='MIT',
)
