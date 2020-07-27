from setuptools import setup, find_packages

__version__ = "0.1.0"

setup(
    name="skel",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "skel = skel.configurations.manage:cli"
        ]
    },
)
