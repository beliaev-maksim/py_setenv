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
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'setenv=py_setenv:main',
        ],
    },
)

