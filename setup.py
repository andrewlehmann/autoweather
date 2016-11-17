from distutils.core import setup, find_packages


with open('LICENSE') as f:
	license1 = f.read()

setup(name = 'autoWeather',
	version= '1.0',
	description = 'automatically text you the weather at 8am',
	author='Andrew Lehmann',
	author_email='andrew@arlehmann.com',
	url='https://github.com/andrewlehmann/autoweatherd',
	license = license1,
	packages=find_packages(exclude='tests')