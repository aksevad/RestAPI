#from setuptools import setup
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="API-sandbox",
    version="0.0.1",
    install_requires=[
        'fastapi==0.70.0',
        'uvicorn==0.15.0',
        'SQLAlchemy==1.4.26',
        'pytest==6.2.5',
        'requests==2.26.0'
    ],
    scripts=['app/main.py']
)