from setuptools import setup, find_packages
import YesssSMS.const as const

setup(
    name='YesssSMS',
    version=const.VERSION,
    description=const.DESC,
    long_description=const.LONG_DESC,
    url='https://github.com/flowolf/yessssms',
    author='Florian Klien',
    author_email='flowolf@klienux.org',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Communications :: Telephony',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    platforms='any',
    keywords=['SMS', 'Yesss', 'messaging'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # List run-time dependencies here.  These will be installed by pip
    install_requires=['requests'],
    python_requires='>=3.3',

    # TODO
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'yessssms=yessssms:main',
    #     ],
    # },
)
