from setuptools import find_packages, setup

package_name = 'pkg_02_topic'

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
    maintainer_email='3492726416@qq.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'topic_01_pub = pkg_02_topic.topic_01_pub:main',
            'topic_01_sub = pkg_02_topic.topic_01_sub:main',
        ],
    },
)
