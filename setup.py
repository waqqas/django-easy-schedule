from setuptools import find_packages, setup

setup(
    name="django-easy-schedule",
    version="0.1.7",
    packages=find_packages(),
    description="Django integration with schedule module",
    author="Waqqas Jabbar",
    author_email="waqqas.jabbar@egmail.com",
    url="https://github.com/waqqas/django-easy-schedule",
    license="MIT",
    install_requires=[
        "Django>=4.0",
        "schedule>=1.0",
    ],
    python_requires='>=3.9',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    include_package_data=True,
    zip_safe=False,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=["django", "schedule"],
)
