from setuptools import setup, find_packages

setup(
    name='pyBunniApi',
    version='1.2.3',
    description='A API Client for communicating with the Bunni accounting software',
    url='https://github.com/sme4gle/pyBunniApi',
    author='Mickael van Schie',
    author_email='mickael.v.s.19@hotmail.com',
    package_data={
        "pyBunniApi": ["py.typed"],
    },
    license='BSD 2-clause',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
