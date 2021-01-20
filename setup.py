from setuptools import setup, find_packages

with open("README.md", "r") as read_me:
    long_description = read_me.read()


setup(
    name="UTK IR Proposed Infrastructure",
    description="a documentation generator for proposing UTK's IR infrastructure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.1",
    author="Mark Baggett",
    author_email="mbagget1@utk.edu",
    maintainer_email="mbagget1@utk.edu",
    url="https://github.com/markpbaggett/utk_ir_infrastructure",
    packages=find_packages(),
    extras_require={
        "docs": [
            "sphinx >= 3.0.1",
            "sphinx-rtd-theme >= 0.5.0",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics :: Presentation",
    ],
    keywords=["libraries", "preservation", "digital repositories", "documentation"],
)