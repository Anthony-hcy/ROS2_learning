# ROS2_learning

## pkg_01_node

### 创建工作空间

```bash
mkdir -p ~/ros_ws/src
```
![[Pasted image 20260816124446.png]]

### 创建功能包并编译

```bash
cd ~/ros_ws/src
ros2 pkg create pkg_01_node --build-type ament_python --license Apache-2.0
cd ~/ros_ws
colcon build
```

![[Pasted image 20260816124821.png]]
![[Pasted image 20260816125028.png]]


### 生效环境变量

```bash
echo "source ~/ros_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

![[Pasted image 20260816125151.png]]

### 编写代码

在/ros_ws/src/pkg_01_node/pkg_01_node下新建node_01.py
```python
import rclpy
from rclpy.node import Node

def main():
    rclpy.init()
    node = Node('node_01')
    node.get_logger().info('Hello Ros2 !')
    node.get_logger().warn('Hi Ros2 !')
    rclpy.spin(node)
    rclpy.shutdown()
```

![[Pasted image 20260816125831.png]]

### 配置依赖

setup.py
```python
entry_points={
        'console_scripts': [
            'node_01 = pkg_01_node.node_01:main'
        ],
    },
```
![[Pasted image 20260816125427.png]]

package.xml
```xml
<depend>rclpy</depend>
```
![[Pasted image 20260816125529.png]]

### 编译运行

```bash
colcon build
ros2 run pkg_01_node node_01
```
![[Pasted image 20260816125931.png]]
新开终端，`ros2 node list`即可查看当前运行的节点
![[Pasted image 20260816130303.png]]


## pkg_02_topic

### 创建发布者（Publisher）

#### 创建功能包并编译

```bash
cd ~/ros_ws/src
ros2 pkg create pkg_02_topic --build-type ament_python --license Apache-2.0
cd ~/ros_ws
colcon build
```

![[Pasted image 20260817112852.png]]

%% ### 生效环境变量

```bash
echo "source ~/ros_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
%%

#### 编写代码

在/ros_ws/src/pkg_02_topic/pkg_02_topic下新建topic_01_pub.py
```python
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Publisher(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info(f"{node_name}, 启动")
        self.publisher_ = self.create_publisher(String,'topic',10)
        self.count_ = 0
        self.timer_ = self.create_timer(0.5,self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = f"Hell, ROS 2! {self.count_}"
        self.count_ += 1
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main():
    rclpy.init()
    node = Publisher('topic_pub')
    rclpy.spin(node)
    rclpy.shutdown()
```

![[Pasted image 20260817144930.png]]

#### 配置依赖

setup.py
```python
    entry_points={
        'console_scripts': [
            'topic_01_pub = pkg_02_topic.topic_01_pub:main',
        ],
    },
```
![[Pasted image 20260817122936.png]]

package.xml
```xml
  <depend>rclpy</depend>
  <depend>example_interfaces</depend>
```
![[Pasted image 20260817123114.png]]

#### 编译运行

```bash
colcon build
ros2 run pkg_02_topic topic_01_pub
```
![[Pasted image 20260817123251.png]]

新开终端，`ros2 topic list`即可查看当前运行的话题，`ros2 topic echo /topic`即可查看话题的内容
![[Pasted image 20260817123634.png]]

---

### 创建订阅者（Subscriber）

%% #### 创建功能包并编译

```bash
cd ~/ros_ws/src
ros2 pkg create pkg_02_topic --build-type ament_python --license Apache-2.0
cd ~/ros_ws
colcon build
```

 #### 生效环境变量

```bash
echo "source ~/ros_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
%%

#### 编写代码

在/ros_ws/src/pkg_02_topic/pkg_02_topic下新建topic_01_sub.py
```python
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Subscriber(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info(f"{node_name}, 启动")
        self.subscriber_ = self.create_subscription(String,'topic',self.Sub_callback,100)
        self.get_logger().info("Waiting pub...")

    def Sub_callback(self,msg):
        self.get_logger().info(f"收到：'{msg.data}'")

def main():
    rclpy.init()
    node = Subscriber('topic_sub')
    rclpy.spin(node)
    rclpy.shutdown()
```

![[Pasted image 20260817145109.png]]

#### 配置依赖

setup.py
```python
    entry_points={
        'console_scripts': [
            'topic_01_pub = pkg_02_topic.topic_01_pub:main',
            'topic_01_sub = pkg_02_topic.topic_01_sub:main',
        ],
    },
```
![[Pasted image 20260817145152.png]]

package.xml
```xml
  <depend>rclpy</depend>
  <depend>example_interfaces</depend>
```
![[Pasted image 20260817123114.png]]

#### 编译运行

```bash
colcon build
ros2 run pkg_02_topic topic_01_sub
```

当Publisher未启动时，Subscriber处于等待中
![[Pasted image 20260817145358.png]]

新开终端，`ros2 run pkg_02_topic topic_01_pub`发布话题
![[Pasted image 20260817145645.png]]

同样，`ros2 topic list`即可查看当前运行的话题，
`ros2 topic echo <topic_name>`即可查看话题的数据
`ros2 topic info <topic_name>`查看话题信息
`ros2 topic pub <topic_name> <msg_type> <msg_data>`发布话题信息


## pkg_03_service

### 创建服务端（Server）

#### 创建功能包并编译

```bash
cd ~/ros_ws/src
ros2 pkg create pkg_03_service --build-type ament_python --license Apache-2.0
cd ~/ros_ws
colcon build
```

![[Pasted image 20260817180701.png]]

%% #### 生效环境变量

```bash
echo "source ~/ros_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
%%

#### 编写代码

在/ros_ws/src/pkg_03_service/pkg_03_service下新建service_01_srv.py
```python
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Server(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.srv = self.create_service(AddTwoInts,'add_two_ints',self.callback)
        self.get_logger().info(f'{node_name}已启动，等待请求...')

    def callback(self,request,response):
        response.sum = request.a + request.b
        self.get_logger().info(f'收到：{request.a} + {request.b} = {response.sum}')
        return response

def main():
    rclpy.init()
    node = Server('service_server')
    rclpy.spin(node)
    rclpy.shutdown()
```

![[Pasted image 20260817182524.png]]

#### 配置依赖

setup.py
```python
    entry_points={
        'console_scripts': [
            'service_01_srv=pkg_03_service.service_01_srv:main',
        ],
    },
```
![[Pasted image 20260817181750.png]]

package.xml
```xml
  <depend>rclpy</depend>
  <depend>example_interfaces</depend>
```
![[Pasted image 20260817181842.png]]

#### 编译运行

```bash
colcon build
ros2 run pkg_03_service service_01_srv
```
![[Pasted image 20260817182459.png]]

新开终端，
`ros2 node list`           查看当前运行的节点，
`ros2 service list`      查看当前运行的服务，
`ros2 service type <service_name> `  查看服务类型
`ros2 service call <service_name> <service_type> <service_data>`发送服务请求
输入`ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 10,b: 20}"`发送服务请求
![[Pasted image 20260817183102.png]]

---

### 创建客户端（Client）

%% #### 创建功能包并编译

```bash
cd ~/ros_ws/src
ros2 pkg create pkg_02_topic --build-type ament_python --license Apache-2.0
cd ~/ros_ws
colcon build
```

 #### 生效环境变量

```bash
echo "source ~/ros_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
%%

#### 编写代码

在/ros_ws/src/pkg_03_service/pkg_03_service下新建service_01_cli.py
```python
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import sys

class Client(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.cli = self.create_client(AddTwoInts,'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1):
            self.get_logger().info('等待服务启动...')
        self.req = AddTwoInts.Request()

    def call_service(self,a,b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req) 
        #rclpy.spin_until_future_complete(self, self.future)   
        #return self.future.result()                           
        while rclpy.ok():
            rclpy.spin_once(self)          
            if self.future.done():         
                if self.future.result() is not None:
                    return self.future.result()
                else:
                    return None

def main():
    rclpy.init()
    node = Client('service_client')
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    response = node.call_service(a, b)
    node.get_logger().info(f'{a} + {b} = {response.sum}')
    rclpy.shutdown()
```

![[Pasted image 20260817192344.png]]

#### 配置依赖

setup.py
```python
    entry_points={
        'console_scripts': [
            'service_01_srv=pkg_03_service.service_01_srv:main',
            'service_01_cli=pkg_03_service.service_01_cli:main',
        ],
    },
```
![[Pasted image 20260817185100.png]]

package.xml
```xml
  <depend>rclpy</depend>
  <depend>example_interfaces</depend>
```
![[Pasted image 20260817181842.png]]

#### 编译运行

```bash
colcon build
ros2 run pkg_03_service service_01_cli 3 6
```
![[Pasted image 20260817185443.png]]
当服务端未启动时，客户端处于等待中
新开终端，`ros2 run pkg_03_service service_01_srv`启动服务端
![[Pasted image 20260817191804.png]]


## pkg_04_interface

### 创建话题接口（.msg）

#### 创建功能包

```bash
cd ~/ros_ws/src
ros2 pkg create pkg_04_interface --build-type ament_cmake --license Apache-2.0
cd pkg_04_interface
rm -rf include src
mkdir msg
cd msg
touch Learningmsg.msg
```

![[Pasted image 20260818124445.png]]

#### 编写代码

在/ros_ws/src/pkg_04_interface/msg下编辑Learningmsg.msg
```msg
int32 counter
string message
```

![[Pasted image 20260818125422.png]]

#### 配置依赖

CMakeLists.txt
```python
find_package(rosidl_default_generators REQUIRED)  
set(msg_files
  "msg/Learningmsg.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
)
```
![[Pasted image 20260818130036.png]]

package.xml
```xml
  <buildtool_depend>rosidl_default_generators</buildtool_depend>
  <exec_depend>rosidl_default_runtime</exec_depend>
  <member_of_group>rosidl_interface_packages</member_of_group>
```
![[Pasted image 20260818130150.png]]

#### 编译运行

```bash
colcon build
ros2 interface show pkg_04_interface/msg/Learningmsg
```
![[Pasted image 20260818130928.png]]
可以看到自定义的新接口已经正确生效

---

### 创建服务接口（.srv）

#### 编写代码

在/ros_ws/src/pkg_04_interface/srv下编辑Learningsrv.srv
```srv
int64 a
int64 b
---
int64 sum
```
![[Pasted image 20260818131602.png]]


#### 配置依赖

CMakeLists.txt
```python
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)  
set(msg_files
  "msg/Learningmsg.msg"
)

set(srv_files
  "srv/Learningsrv.srv"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
  ${srv_files}
)
```
![[Pasted image 20260818131945.png]]

package.xml
```xml
  <buildtool_depend>rosidl_default_generators</buildtool_depend>
  <exec_depend>rosidl_default_runtime</exec_depend>
  <member_of_group>rosidl_interface_packages</member_of_group>
```
![[Pasted image 20260818130150.png]]


#### 编译运行

```bash
colcon build
ros2 interface show pkg_04_interface/srv/Learningsrv
```
![[Pasted image 20260818132132.png]]
可以看到自定义的新接口已经正确生效

> [!attention]
>  ROS 2 中，主题名称和消息类型必须同时匹配才能进行通信。
> 主题名称：'topic'这种
> 消息类型：pkg_04_interface/msg/Learningmsg和example_interfaces/msg/String这种