from setuptools import setup, find_packages

setup(
    name="resource-dashboard",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pandas>=2.1.0',
        'numpy>=1.24.3',
        'openpyxl>=3.1.2',
        'yfinance>=0.2.28'
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A resource allocation and budget tracking dashboard using real financial data",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/resource-dashboard",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
