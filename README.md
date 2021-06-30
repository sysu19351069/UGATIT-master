**本次程序运行需要在Anaconda环境下的$JupyterLab$ 上运行**

注：文件名采用相对路径即可

运行环境要求：

python3.7

pytorch>=1.16

dlib（先要安装Cmake, Boost），建议按下面命令安装

```
conda install -c conda-forge dlib
```

其他常见的库



实验的权重保存在logs中的ugatit和ugatit_plus，表示用了两种不同的方法训练得到，其中ugatit保存了训练了100轮和200轮的权重，ugatit_plus保存了训练了100个epoch的权重

如果想要测试几张图片对比两种方法的效果，直接在终端输入以下命令

##### 测试ugatit

```
python tool/demo_ugatit.py --type ugatit --resume logs/ugatit/99.pt --input images --saved-dir save --anime
```

##### 测试ugatit_plus

```
python tool/demo_ugatit.py --type ugatit --resume logs/ugatit/99.pt --input images --saved-dir save --anime
```

##### 如果想要查看加入Facealignment的效果

```
python tool/demo_ugatit.py --type ugatit --resume logs/ugatit/99.pt --input images --saved-dir save --align --anime
 python tool/demo_ugatit.py --type ugatit_p --resume logs/ugatit_plus/99.pt --input images --saved-dir save --align --anime
```

##### 如果想要通过电脑摄像头实时查看转换的效果

直接CTRL+Enter运行  **run.ipynb**

默认的设置是用训练了200轮的ugatit权重

![image-20210629200251549](C:\Users\25478\AppData\Roaming\Typora\typora-user-images\image-20210629200251549.png)

其中model_type是 'ugatit​' 或 'ugatit_p'

resume是对应的权重文件路径

align为是否用Facealignment

anime设置为True即可