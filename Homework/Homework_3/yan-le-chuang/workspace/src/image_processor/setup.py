from setuptools import find_packages, setup

package_name = 'image_processor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ylc',
    maintainer_email='2264026818@qq.com',
    description='TODO: Package description',
    license='Apache2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'image_processor_node = image_processor.image_processor_node:main',
        ],
    },
)
