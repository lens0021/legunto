import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="legunto",
    version="1.0.3",
    description="Fetch MediaWiki Scribunto modules from wikis",
    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=[
        'legunto',
        'scribunto'
    ],
    install_requires=["mwclient"],
    package_dir={'': 'src'},

    entry_points={
        'console_scripts': ['legunto = legunto:console_main'],
    }
)
