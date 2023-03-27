import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="filter",
    version="0.1.0",
    author="parkminwoo",
    author_email="parkminwoo1991@gmail.com",
    description="The Python package filter is used to detect and remove inappropriate information from text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DSDanielPark/filter",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        "re",
        "pandas"
    ])