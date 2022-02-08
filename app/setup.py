from setuptools import setup

setup(
    name='cli',
    version='1.0',
    packages=['cli', 'cli.commands'],
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        cli=cli.cli:cli
    """,
)
