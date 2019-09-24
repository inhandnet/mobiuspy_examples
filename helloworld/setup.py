  
from setuptools import setup, find_packages

setup(
    name='helloworld',
    sdk_version='1.2.9',
    version='0.0.1',
    author='InHandNetworks',
    author_email='zhengyb@inhand.com.cn',
    description='This is the first simple example for Mobius Python newbies.',
    license='MIT License',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    install_requires=[
    ]
)