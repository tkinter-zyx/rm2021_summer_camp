# Robomaster 2021 Task2 使用说明
***
_姓名：张宇轩  组别：5组  方向：算法_
## 三龟列阵

开发耗时：约9h

预期效果：生成三只乌龟在画布上，以它们的位置确定一个圆，三只乌龟绕着圆匀速行进，当键盘控制其中一只移动后，轨迹随即发生变化，它们沿着新的轨迹继续行进

完成情况：由于从下午5：00左右才开始着手编写程序（之前写简历时制作的程序看样子并不符合要求），时间关系没有解决当前这个奇怪的bug，整体逻辑没有太大问题，也可以运行，只是无法达到预期效果

使用方法：下载功能包并编译后进入工作空间文件夹下输入以下命令

    source devel/setup.bash
    rosrun tourtlesim tourtlesim_node
    rosrun task2 turtle_forma

## 再来一龟

使用方法：下载功能包并进入工作空间文件夹下输入以下命令

    source devel/setup.bash
    cd ./rm2021_summer_camp/task2/launch/
    roslaunch remap.launch

实际效果：turtle2出现在画布左下角，终端新开一标签页可用于控制turtle2

## 里程发送

由于今天做三龟列阵过于投入，不知不觉竟已经将近凌晨四点，于是我遗憾地打算先睡为妙