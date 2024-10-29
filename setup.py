##setup.py>> building your application as a package and deploy
#into pypy and then anybody do the installation and saw.
#morel>> building your application as a package

from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    """this funcation will return the list 
       of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements 

setup(
    name="RWS_Project",
    version="0.0.1",
    author="Govind Singh",
    author_email="singhg81484@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)