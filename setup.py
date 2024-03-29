from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
]

setup(
    name='Receiptify',
    version='1.0',
    description='An application that gets your top spotify tracks and turns them into a receipt',
    author='Etchilia Madrid',
    author_email='etchmadridlia@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)