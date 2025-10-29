from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ft_package",
    version="0.0.1",
    author="bchene",
    author_email="bchene@student.42angouleme.fr",
    description="A sample test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bchene/ft_package",
    license="MIT",
    license_files=("LICENSE.txt",),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
