from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'parcial1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jhon',
    maintainer_email='jhon_edw.gonzalez@uao.edu.co',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'color = parcial1.color_detector_:main',
            'frames = parcial1.frames_publisher:main',
            'gui = parcial1.gui:main',
            'suscriber = parcial1.frames_suscriber:main',
            'person = parcial1.person_detection:main',
            'filter = parcial1.filter:main',
        ],
    },
)
