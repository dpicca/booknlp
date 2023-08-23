from setuptools import setup, find_packages

setup(name='booknlp', 
	version='1.0.7', 
	packages=find_packages(),
	py_modules=['booknlp'],
	url="https://github.com/dbamman/book-nlp",
	author="David Bamman",
	author_email="dbamman@berkeley.edu",
	include_package_data=True, 
	license="MIT",
	install_requires=open('requirements.txt').readlines(),

	)
