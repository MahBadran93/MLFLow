from setuptools import setup, find_packages

def get_req(path:str):
    """
    return list of packages"
    """

    reqs = []

    with open(path) as file_obj:
        reqs = file_obj.readlines()
        reqs = [req.replace("\n", "") for req in reqs]

    return reqs


path = './requirements.txt'


setup(
    name='test_mlflow',
    version='0.0.1',
    author='mahmoud',
    author_email='mahmoud.s.badran@gmail.com',
    description='mlops project structure (testing and deployment with CD/CI pipeline)',
    packages=find_packages(),
    install_requires=get_req(path)
)