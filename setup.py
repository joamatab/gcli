from setuptools import setup, find_packages


def get_install_requires():
    with open("requirements.txt", "r") as f:
        return [line.strip() for line in f.readlines() if not line.startswith("-")]


setup(
    version="0.0.2",
    name="gitcli",
    packages=find_packages(),
    # package_data={"": ["*.lsf", "*.json"]},
    include_package_data=True,
    scripts=["gcli/cli.py"],
    # use_scm_version=True,
    # setup_requires=['setuptools_scm'],
    description="Git Command Line Interface",
    author="joaquin",
    install_requires=get_install_requires(),
    tests_require=["pytest", "tox"],
    python_requires=">=3",
    entry_points="""
        [console_scripts]
        gcli=gcli.cli:cli
    """,
)
