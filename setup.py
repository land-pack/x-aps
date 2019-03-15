import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="x-aps",
    version="0.1.0",
    author="landpack",
    author_email="landpassing@gmail.com",
    description="Using decorator way to work with APScheduler on Tornado",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/land-pack/x-aps",
    #packages=setuptools.find_packages(),
    packages=['xaps',],
    install_requires = ['tornado', 'apscheduler'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
