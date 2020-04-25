import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fp:
    install_requires = fp.read()
    
setuptools.setup(
    name="twitter-spider",
    version="0.0.1",
    author="Dainius Preimantas",
    author_email="preimantasd@gmail.com",
    description="A twitter tweets spider",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/pdainius/twitter-spider",
    packages=setuptools.find_packages(exclude=["venv"]),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)