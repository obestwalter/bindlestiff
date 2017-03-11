import itertools
from setuptools import setup


def get_extra_dependencies():
    extras = dict(tests=['tox', 'flake8', 'pytest', 'pytest-watch'],
                  docs=['mkdocs', 'mkdocs-material'])
    extras.update(dict(all=list(itertools.chain(*extras.values()))))
    return extras

settings = dict(
    name='bindlestiff',
    author='Oliver Bestwalter',
    url='https://github.com/obestwalter/bindlestiff',
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'pytest-runner'],
    tests_require=['pytest'],
    packages=['bindlestiff'],
    license='MIT',
    install_requires=[],
    extras_require=get_extra_dependencies(),
    entry_points={'console_scripts': [
        'bindlestiff = bindlestiff.cli:main'
    ]}
)

if __name__ == '__main__':
    setup(**settings)
