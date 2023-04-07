from setuptools import find_packages, setup


with open("requirements/base.txt") as f:
    base_requirements = f.read().splitlines()

with open("requirements/test.txt") as f:
    test_requirements = f.read().splitlines()


dependency_links = []


setup(
    name="adam",
    version="0.0.8",
    author="1mg",
    author_email="int-rajdeep.r@1mg.com",
    url="https://bitbucket.org/tata1mg/adam",
    description="command line tool for push OpenAPI specification file",
    packages=find_packages(exclude=("requirements")),
    entry_points={"console_scripts": ["adam=adam.main:main"]},
    install_requires=base_requirements + test_requirements + dependency_links,
)
