from setuptools import setup, find_packages
from typing import List

hypen_dot = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    It removes any '-e .' entry which is used for editable installs.
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.strip().replace('\n','') for req in requirements]
        
        if hypen_dot in requirements:
            requirements.remove(hypen_dot)
    
    return requirements

setup(
    name='sales_analytics_pipeline',
    version='0.0.1',
    author='Ashu',
    author_email='ashufrancis673@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A sales analytics pipeline project',   
    python_requires='>=3.7'
)