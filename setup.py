from setuptools import setup, find_packages

setup(
    name='pyxhook',
    version='1.0.0',
    description='Packaged version of pyxhook',
    maintainer='hosty',
    license='GNU version 2',
    url='https://github.com/hosty/pyxhook/',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    entry_points={
    },
    install_requires=[
        'python-xlib'
    ]
)
