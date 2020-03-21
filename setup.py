from setuptools import setup
import os

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements


def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]


setup(
    name='Reflex API',
    version='0.1.0',
    long_description=__doc__,
    packages=['reflex_api'],
    include_package_data=True,
    zip_safe=False,
    author = 'Purushotham Reddy',          
    author_email = 'kspreddy94@gmail.com', 
    install_requires=load_requirements("requirements.txt"),
    url="https://github.com/prsrepo/reflex_api",
    classifiers=[
        'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6'
    ]
)

