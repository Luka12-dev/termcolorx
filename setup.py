from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="termcolorxcore",
    version="0.1.0",
    author="Luka",
    author_email="lukadevpypi@gmail.com",
    description="Colorful, styled terminal output with ASCII banners and emoji support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Luka12-dev/termcolorx",
    packages=find_packages(),
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)