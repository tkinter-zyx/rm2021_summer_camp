# Robomaster 2021 Task 使用说明
***
_姓名：张宇轩  组别：5组  方向：算法_

## Task 2.1

开发耗时：约9h

预期效果：生成三只乌龟在画布上，以它们的位置确定一个圆，三只乌龟绕着圆匀速行进，当键盘控制其中一只移动后，轨迹随即发生变化，它们沿着新的轨迹继续行进

完成情况：由于从下午5：00左右才开始着手编写程序（之前写简历时制作的程序看样子并不符合要求），时间关系没有解决当前这个奇怪的bug，整体逻辑没有太大问题，也可以运行，只是无法达到预期效果

使用方法：下载功能包并编译后进入工作空间文件夹下输入以下命令

    source devel/setup.bash
    rosrun tourtlesim tourtlesim_node
    rosrun task2 turtle_forma

## Task 2.2

使用方法：下载功能包并进入工作空间文件夹下输入以下命令

    source devel/setup.bash
    cd ./rm2021_summer_camp/task2/launch/
    roslaunch remap.launch

实际效果：turtle2出现在画布左下角，终端新开一标签页可用于控制turtle2

## Task4

使用方法：下载功能包并编译后进入工作空间文件夹下输入以下命令

    roslaunch task4 start.launch 

实际效果：出现在摄像头视野内的二维码可被识别，二维码自身坐标系显示在rviz可视化界面上

错误解决：若出现以下报错信息

    [ERROR] [1626876251.212798002]: VIDIOC_S_FMT error 22, Invalid argument
    [usb_cam-3] process has died [pid 65032, exit code 1

请打开`task4/launch/usb_cam-test.launch`文件，将第3行`value`的值改为当前系统下的设备名称