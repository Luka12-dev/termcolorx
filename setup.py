from setuptools import setup, find_packages

setup(
    name="termcolorx",
    version="0.1.1",
    author="Luka",
    author_email="lukadevpypi@gmail.com",
    description="Lightweight terminal styling helpers (ANSI-only). Simple, dependency-free.",
    packages=find_packages(exclude=("tests", "examples")),
    python_requires=">=3.7",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)