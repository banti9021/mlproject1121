import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

_version_ = "0.0.0"

REPO_NAME = "project"

AUTHOR_USER_NAME = "banti9021"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "nbanti943@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Updated content type
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
