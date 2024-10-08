from setuptools import setup, find_packages

setup(
    name="weather-sdk",
    version="1.0.0",
    description="A simple SDK to fetch weather and forecast data from OpenWeather API",
    author="Benjamim Francisco",
    author_email="benjamim.francisco@hotmail.com",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)