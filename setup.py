from setuptools import setup, find_packages

setup(
    name="google_analytics_integration",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "google-analytics-data==0.18.16",
        "google-auth==1.29.0",
        "google-auth-oauthlib==0.4.4"
    ],
)