"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='lindenmayer-systems',  # Required
    version='0.0.1',  # Required
    description='Explores Lindenmayer systems',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/umayrh/lindenmayer-systems',  # Optional
    author='Umayr Hassan',  # Optional
    author_email='umayrh@gmail.com',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='l-systems, algorithmic botany, formal languages',  # Optional
    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.6, <4',
    install_requires=['matplotlib'],  # Optional
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    #package_data={  # Optional
    #    'sample': ['package_data.dat'],
    #},
    #data_files=[('my_data', ['data/data_file'])],  # Optional
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    #entry_points={  # Optional
    #    'console_scripts': [
    #        'sample=sample:main',
    #    ],
    #},
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/umayrh/lindenmayer-systems/issues',
        'Source': 'https://github.com/umayrh/lindenmayer-systems',
    },
)
