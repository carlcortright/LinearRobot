from setuptools import setup 

setup(
	name='LinearRobotControlInterface',
	version='0.1',
	description='Control interface for the Gilroy Lab Linear Robot.',
	url='https://github.com/GilroyLabRobots/linearRobot',
	author='Carl Cortright',
	author_email='ckcortright@gmail.com',
	license='GPL',
	packages=['LinearRobotControlInterface'],
	install_requires=['pyserial',],
	zip_safe=True
	)