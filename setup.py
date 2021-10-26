from setuptools import setup

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='Python-TBot-calendar',
    packages=['TBot_calendar'],
    version='0.0.1',
    license='MIT',
    description='Календарь на python для telegram ботов',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Artem Moskalenko',
    author_email='shamandok22@gmail.com',
    url='https://github.com/shamandok/Python-TBot-calendar',
    keywords=['calendar', 'telegram', 'bot', 'telegram bot'],
    install_requires=[
        'python-dateutil',
    ],
    extras_require={
        'telethon': ['telethon']
    },
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
