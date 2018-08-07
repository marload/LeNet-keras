This repo is implemented in Tensorflow

# CNN Architecture
|Architecture | Framework | Link |
|:---:|:---:|:---:|
| LeNet-5 | keras(using tensorflow) | [HERE](https://github.com/olramde/LeNet-keras) |
| AlexNet | Tensorflow | - |
|GoogLeNet | - | - |
|ResNet | - | -|

# LeNet-5 with keras
LeNet-5 Architecture is perhaps the most widely known CNN architecture. This architecture 
was made by Yann LeCun. This architecture consist of the following layers.




| Layer | Feature Map | Size | Kernel Size | Stride | Activation |
|:---:|:---:|:---:|:---:|:---:|:---:|
| FC | - | 10 | - | - | softmax |
| FC | - | 84 | - | - | tanh |
| Conv2d| 120|1x1 | 5x5 | 1 | tanh |
|Average Pooling | 16 | 5x5 | 2x2 | 2 | tanh |
|Conv2d | 16 | 10x10 | 5x5 | 1 | tanh|
|Average Pooling | 6 | 14x14 | 2x2 | 2 | tanh |
|Conv2d | 6 | 28x28 | 5x5 | 1 | tanh |
|Input | 1 | 32x32 | - | - | - |

* MNIST Image is 28x28 pixel, but it was 32x32 pixel because of applied zero padding.

# code

`data.py` is class for MNIST Data preprocessing<br/>
`lenet.py` is LeNet model implemented with keras<br/>
`plot.py` is function for loss visualization<br>
If you want to test, run `main.py`