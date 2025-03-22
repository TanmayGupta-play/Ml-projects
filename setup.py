from setuptools import setup, find_packages
from typing import List

HYPHEN_SEPARATOR = '-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    this function reads the file and returns the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHEN_SEPARATOR in requirements:
            requirements.remove(HYPHEN_SEPARATOR)
    return requirements
       

setup(
    name='my_package',  # Package name
    version='0.0.1',  # Package version
    author='Tanmay Gupta',  # Author name
    author_email='guptatanmay02@gmail.com',#Author email
    packages=find_packages(),  # List of packages
    install_requires= get_requirements('Requirement.txt'),  # List of dependencies


)