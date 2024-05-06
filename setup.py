from setuptools import setup, find_packages


HYPHEN_E_DOT = '-e .'

def get_requirements(file_name) -> list[str]:
    """
    This function will read from requirements.txt and return the list of all the packages required.
    """
    with open(file_name) as f:  # reading the lines from the file
        requiremnts = f.readlines()
    requirements = [req.replace('\n', '') for req in requiremnts]# replacing the escape charachter from the text

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)  # Removing the -e. from the requirements.
        
    return requirements

setup(
    name='Premium prediction',
    version='0.0.1',
    description='Industry level project for premium prediction.',
    author='Pritam Kumar',
    author_email='singhpritam983@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
