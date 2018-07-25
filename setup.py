from setuptools import setup, find_packages

import sys

if sys.version_info < (3,6):
    print("Light requires python version 3.6 or higher.")
    sys.exit(1)

setup(
    name="light",
    version="0.1",
    description="light",
    long_description="light",
    author="CRITs",
    author_email="",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='crits light',
    url='https://www.github.com/crits/light',
    install_requires=[
    ],
    packages=find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            'illuminate=light:main',
        ]
    }
)
