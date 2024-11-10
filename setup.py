# setup.py

from setuptools import setup, find_packages

setup(
    name="my_cli_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "argparse",
    ],
    entry_points={
        'console_scripts': [
            'structlab=my_cli_app.proj_struct:cli', 
        ],
    },
    description="Project structure generator",
)
