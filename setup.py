import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name='bode_utils',    # This is the name of your PyPI-package.
    version='1.0.0',
    url='https://github.com/ryanGT/bode_utils',
    author='Ryan Krauss',
    author_email='ryanwkrauss@gmail.com',
    description="package for generating Bode plots",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
