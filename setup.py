from setuptools import setup, find_packages
from os import getenv

try:
    with open('requirements.txt') as r:
        requirements = r.readlines()
except:
    requirements = []
    
try:
    from __package__ import *
    
except:
    package_name = getenv("PACKAGE_NAME", None)
    version      = getenv("PACKAGE_VERSION", None)
    github_url   = getenv("GITHUB_URL", None)

    assert version != None, "PACKAGE_VERSION unset"
    assert package_name != None, "PACKAGE_NAME name unset"
    assert github_url != None, "GITHUB_URL url unset"
    
    with open("__package__.py", 'w') as f:
        f.write(
            "\n".join(
                [
                    f'package_name="{package_name}"',
                    f'github_url="{github_url}"',
                    f'version="{version}"',
                ]
            )
        )
        
package_name_importable = package_name.replace('-','_')

setup(
    name = package_name,
    version = version,    
    description = '',
    url = github_url,
    author = 'TP',
    author_email = '',
    license = '',
    packages = [
        package_name_importable + package.partition('src')[2]
        for package in find_packages()
    ],
    package_dir = {
        package_name_importable: 'src'
    },
    install_requires = requirements,
    classifiers = [
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
