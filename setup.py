import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kinesis_wrapper",
    version="0.1.1",
    author="Cong Wang",
    author_email="wangimagine@gmail.com",
    description="This package provides capabilities of using Python to programmatically control Thorlab's kinesis software.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carbonscott/kinesis_wrapper",
    keywords = ['thorlab', 'wrapper', 'kinesis'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
