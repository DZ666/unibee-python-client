# coding: utf-8

"""
    UniBee Python SDK

    Official Python client for the UniBee Billing API.
    
    Documentation: https://docs.unibee.dev
"""

from setuptools import setup, find_packages

NAME = "unibee"
VERSION = "2.0.0"
PYTHON_REQUIRES = ">=3.8"
REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="UniBee Python SDK - Official Python client for the UniBee Billing API",
    author="UniBee Team",
    author_email="support@unibee.dev",
    url="https://github.com/UniBee-Billing/unibee-python-client",
    keywords=["UniBee", "billing", "subscription", "payments", "SaaS", "invoicing"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests", "examples"]),
    include_package_data=True,
    license="Apache-2.0",
    long_description_content_type='text/markdown',
    long_description=long_description,
    package_data={"openapi_client": ["py.typed"]},
    python_requires=PYTHON_REQUIRES,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
