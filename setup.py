from setuptools import setup

setup(
    name='resume-generator',
    description='Resume Generator API',
    author='Jason Durant',
    author_email='durantjay1@gmail.com',
    zip_safe=False,
    packages=['resume-generator'],
    install_requires=[
        'python-docx'
    ]
)