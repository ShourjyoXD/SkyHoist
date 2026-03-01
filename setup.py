from setuptools import setup, find_packages

setup(
    name="skyhoist",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "click",
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "skyhoist=skyhoist.cli:cli",
        ],
    },
)