from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='doomsayer',
    description="Send out Hipchat notification when spot instance is marked for termination.",
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements
)
