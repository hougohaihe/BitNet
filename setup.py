#!/usr/bin/env python3
"""
Setup script for BitNet - A fork of microsoft/BitNet.

This package provides tools for running inference with BitNet models,
including quantized 1-bit and 1.58-bit language models.
"""

from setuptools import setup, find_packages
import os

# Read the README for the long description
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Core dependencies required for running BitNet inference
install_requires = [
    "numpy>=1.24.0",
    "torch>=2.0.0",
    "transformers>=4.36.0",
    "huggingface_hub>=0.20.0",
    "sentencepiece>=0.1.99",
    "tqdm>=4.65.0",
    "requests>=2.28.0",
    "pyyaml>=6.0",
]

# Optional dependencies for development and testing
extras_require = {
    "dev": [
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
        "black>=23.0.0",
        "isort>=5.12.0",
        "flake8>=6.0.0",
        "mypy>=1.0.0",
    ],
    "quantization": [
        "gguf>=0.6.0",
        "accelerate>=0.25.0",
    ],
    "server": [
        "fastapi>=0.100.0",
        "uvicorn>=0.23.0",
        "pydantic>=2.0.0",
    ],
}

# Combine all extras into a 'all' option
extras_require["all"] = [
    dep for deps in extras_require.values() for dep in deps
]

setup(
    name="bitnet",
    version="0.1.0",
    author="BitNet Contributors",
    description="Efficient inference framework for 1-bit and 1.58-bit quantized language models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microsoft/BitNet",
    license="MIT",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "docs.*"]),
    python_requires=">=3.9",
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={
        "console_scripts": [
            "bitnet=bitnet.cli:main",
            "bitnet-server=bitnet.server:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "llm",
        "ization",
        "bitnet",
        "1-bit",
        "language"inference",
        "transformers",
    ],
    include_package_data=True,
    package_data={
        "bitnet": ["configs/*.yaml", "kern"],
    },
    zip_safe=False,
)
