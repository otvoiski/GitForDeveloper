from setuptools import setup

setup(
    name="gfd",
    version="1.0.0",
    py_modules=["gfd"],
    install_requires=[
        "gitpython==3.1.40",
        "colorama==0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "gfd=gfd:main",
        ],
    },
) 