from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def get_requirements(filename):
    requirements = []
    with open(filename, "rt") as req_file:
        for line in req_file.read().splitlines():
            if not line.strip().startswith("#"):
                requirements.append(line)
    return requirements


project_requirements = get_requirements("requirements.txt")

setup(
    name="py_setenv",
    version='1.0.1',
    license='MIT',

    description='CLI App to manage window environment variables',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Maksim Beliaev',
    author_email='beliaev.m.s@gmail.com',

    install_requires=project_requirements,
    entry_points={
        'console_scripts': [
            'setenv=py_setenv:click_command',
        ],
    },

    keywords=['CLI', 'Environment', 'Variable'],

    url='https://github.com/beliaev-maksim/py_setenv',
    download_url='https://github.com/beliaev-maksim/py_setenv/archive/v1.0.tar.gz',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
      ],
)

