from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(
    name="toolbox502",
    version="1.0",
    description="Toolbox trial of Edgar Minault",
    packages=find_packages(),
    test_suite="tests",
    # include_package_data: to install data from MANIFEST.in
    include_package_data=True,
    # scripts=["scripts/toolbox502-run"],
    zip_safe=False,
)
