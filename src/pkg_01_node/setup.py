from setuptools import find_packages, setup

package_name = 'pkg_01_node'

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
    maintainer='hcy',
    maintainer_email='hcy@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'node_01 = pkg_01_node.node_01:main',
            'node_02 = pkg_01_node.node_02:main',
            'node_03 = pkg_01_node.node_03:main'
        ],
    },
)
