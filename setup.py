from setuptools import setup, find_packages
import pathlib

# Get current directory
HERE = pathlib.Path(__file__).parent

# Read README for long description
README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name='ragdoc-portal',   #  package name
    version='0.1.0',    # package version
    author='ShivpalSW', 
    author_email="shivpalwaiml@gmail.com",    
    long_description=README,  # Read the long description from README file
    long_description_content_type="text/markdown",
    url="https://github.com/shivpalSW/Advanced-RAG-Doc-System",  # Update with your repo URL
    packages=find_packages(),
    include_package_data=True, )
