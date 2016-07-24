from setuptools import setup, find_packages

setup(
    name='job_server',
    version='1.0.0-dev',
    author='jessicalucci14@gmail.com',
    description='Job Server',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
