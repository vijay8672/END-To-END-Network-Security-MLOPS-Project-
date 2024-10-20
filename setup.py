""" Setup.py file package your Python project so others can easily install and use it,
it means you're preparing your project in a way that other people can install it with a 
simple command like pip install instead of manually copying files or setting things up themselves.
It consists of project metadata, dependencies, and more"""

from setuptools import find_packages, setup
from typing import List




def get_requirements()->List[str]:
  """This function will get list of requirements"""

  requirement_lst:List[str]=[]

  try:
    with open('requirements.txt', 'r') as file:
      ## Read lines from the file
      lines=file.readlines()
      for line in lines:
        requirement=line.strip()

        # ignore empty lines and -e . 
        if requirement and requirement!= '-e .':
          requirement_lst.append(requirement)

  except FileNotFoundError:
    print('requirements.txt file not found')


  return requirement_lst

print(get_requirements())



setup(
  name="Network Security Project using MLOPS",
  version="0.0.1",
  author="Vijay Kumar Kodam",
  author_email="vijay.kodam98@gmail.com",
  packages=find_packages(),
  install_requires=get_requirements()
)