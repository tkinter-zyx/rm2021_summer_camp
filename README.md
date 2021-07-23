# Robomaster 2021 Task 使用说明
***
_姓名：张宇轩  组别：5组  方向：算法_

## Task 2.1

### 预期效果

生成三只乌龟在画布上，以它们的位置确定一个圆，三只乌龟绕着圆匀速行进，当键盘控制其中一只移动后，轨迹随即发生变化，它们沿着新的轨迹继续行进

### 完成情况

由于从下午5：00左右才开始着手编写程序（之前写简历时制作的程序看样子并不符合要求），时间关系没有解决当前这个奇怪的bug，整体逻辑没有太大问题，也可以运行，只是无法达到预期效果

### 使用方法

下载功能包并编译后进入工作空间文件夹下输入以下命令

    source devel/setup.bash
    rosrun tourtlesim tourtlesim_node
    rosrun task2 turtle_forma

## Task 2.2

### 使用方法

下载功能包并进入工作空间文件夹下输入以下命令

    source devel/setup.bash
    cd ./rm2021_summer_camp/task2/launch/
    roslaunch remap.launch

### 实际效果

turtle2出现在画布左下角，终端新开一标签页可用于控制turtle2

## Task 3

### 使用方法

下载功能包并进入工作空间文件夹下输入以下命令

    source devel/setup.bash
    roslaunch task3 start.launch

### 实际效果

可以看到rviz中的两个tf坐标系，odom坐标系随时间变化

### 疑似缺陷

坐标系的轨迹看起来不是很正常，但又排查不出错误的地方

## Task 4

### 使用方法

下载功能包并编译后进入工作空间文件夹下输入以下命令

    source devel/setup.bash
    roslaunch task4 start.launch 

### 实际效果

出现在摄像头视野内的二维码可被识别，二维码自身坐标系显示在rviz可视化界面上

### 错误解决

若出现以下报错信息

    [ERROR] [1626876251.212798002]: VIDIOC_S_FMT error 22, Invalid argument
    [usb_cam-3] process has died [pid 65032, exit code 1

请打开`task4/launch/usb_cam-test.launch`文件，将第3行`value`的值改为当前系统下的设备名称

## Task 5

### 使用方法

下载功能包主分支并编译后进入工作空间文件夹下输入以下命令

    source devel/setup.bash
    roslaunch task5 start.launch

### 实际效果

弹出一个窗口显示画面，画面中出现面部时眼睛与面部会被圈出，画面延时巨大

### 改进尝试

因疑似opencv显示图像时的延时函数导致画面延时，因此在分支`task5`中尝试在话题`/viewer`中发布图像，用usb_cam的显示节点重映射后显示图像，但依然存在延时，原因尚未查明，使用方法同上。

## Task 6

### 实现方法

由于多次尝试仍无法解决依赖问题，无法成功运行例程，因此尝试其他方法。在solidoworks中制作完成两轴平面机械臂的模型，使用插件导出为urdf，转移到ros下编译运行。

### 完成情况

完成建模并导出功能包，但还有错误未解决，未成功运行。