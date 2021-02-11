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
    license='MIT',
    description='CLI App to manage window environment variables',
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

