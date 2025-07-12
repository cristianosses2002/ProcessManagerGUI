from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="gestor-procesos-avanzado",
    version="1.0.0",
    author="CristianOsses",
    author_email="cristian.osses@ejemplo.com",
    description="Gestor de procesos avanzado para Windows con optimización para gaming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CristianOsses/gestor-procesos-avanzado",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gestor-procesos=test:main",
        ],
    },
    keywords="windows, process, manager, gaming, optimization, system, monitoring",
    project_urls={
        "Bug Reports": "https://github.com/CristianOsses/gestor-procesos-avanzado/issues",
        "Source": "https://github.com/CristianOsses/gestor-procesos-avanzado",
        "Documentation": "https://github.com/CristianOsses/gestor-procesos-avanzado#readme",
    },
) 