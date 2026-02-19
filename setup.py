'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''
from setuptools import find_packages,setup
from typing import List

def get_requirments()->List[str]:
    """ this function return list of requirments"""

    requirments_list:List[str]=[]
    try:

        with open('requirements.txt','r') as file:
        #read lines from file
            lines=file.readlines()
        #process each line
            for line in lines:
                requirment=line.strip()
                #ignore empty line
                if requirment and requirment!='-e .':
                    requirments_list.append(requirment)
    except FileNotFoundError:
        print("requirement.txt file not found error")
    return requirments_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Vikas Chakole",
    author_email="alml9.vikas@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments()
)