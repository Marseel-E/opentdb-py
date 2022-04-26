import setuptools

with open("README.md", 'r', encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opentdb-py",
    version="2.0.1",
    author="Marseel Eeso",
    author_email="marseeleeso@gmail.com",
    description="Python wrapper for the open-trivia-database API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Marseel-E/opentdb-py",
    project_urls={
        "Bug Tracker": "https://github.com/Marseel-E/opentdb-py/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "trivia"},
    packages=setuptools.find_packages(where="trivia"),
    python_requires=">=3.8",
)
