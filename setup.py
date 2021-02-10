from setuptools import setup

def get_requirements(filename):
    requirements = []
    with open(filename, "rt") as req_file:
        for line in req_file.read().splitlines():
            if not line.strip().startswith("#"):
                requirements.append(line)
    return requirements


project_requirements = get_requirements("requirements.txt")

setup(
    name="setenv",
    version='1',

    # Author details
    author='Maksim Beliaev',
    author_email='beliaev.m.s@gmail.com',

    license='MIT',

    py_modules=['setenv'],
    install_requires=project_requirements,
    entry_points='''
        [console_scripts]
        setenv=setenv:set_variable
    ''',
)
