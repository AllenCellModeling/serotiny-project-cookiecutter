# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup, find_namespace_packages

requirements = [
    "serotiny"
]


setup(
    author="Ryan Spangler, Ritvik Vasan, Guilherme Pires, Caleb Chan, Theo Knijnenburg",
    author_email="ryan.spangler@alleninstitute.org, ritvik.vasan@alleninstitute.org, guilherme.pires@alleninstitute.org, caleb.chan@alleninstitute.org, theo.knijnenburg@alleninstitute.org",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="{{cookiecutter.project_description}}",
    install_requires=requirements,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="{{cookiecutter.package_name}}",
    name="{{cookiecutter.package_name}}",
    packages=find_namespace_packages(include=["hydra_plugins.*"]) +
        find_packages(exclude=["tests", "*.tests", "*.tests.*"]),
    python_requires=">=3.7",
    # Do not edit this string manually, always use bumpversion
    # Details in CONTRIBUTING.rst
    version="0.0.0",
    zip_safe=False,
)
