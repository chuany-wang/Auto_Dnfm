import pyautogui


def get_screen_size():
    # 获取当前屏幕尺寸
    x = pyautogui.size()
    print(x)  # Size(width=2560, height=1440)
    print(x[0])  # 2560
    print(x[1])  # 1440
    print(type(x))  # <class 'pyautogui.Size'>


def get_mouse_position():
    # 获取当前鼠标位置
    x = pyautogui.position()
    print(x)  # 坐标的距离通过像素计算，如果你的屏幕分辨率是1920 x 1080，右下角的像素将是1919, 1079（因为坐标从0开始，而不是1）


def judge_position_on_screen():
    # 判断坐标是否在当前屏幕中
    res = pyautogui.onScreen(x=2890, y=1556)
    print(res)
    res2 = pyautogui.onScreen(x=1890, y=556)
    print(res2)


def mouse_move():
    # 用n秒时间将鼠标从当前位置移动到(x,y)位置

    x = 0
    y = 0
    n = 2
    pyautogui.moveTo(x, y, duration=n)


def mouse_move_offset():
    # 用n秒将鼠标从当前位置向右向左移动 xoffset 像素,向下/向上移动 yoffset 像素, 如果 n = 0 ,则立即移动
    xOffset = -150
    yOffset = -150
    n = 2
    pyautogui.moveRel(xOffset=xOffset, yOffset=yOffset, duration=n)


def mouse_drag():
    # 此外，为了防止程序出问题，当鼠标移动到屏幕左上角，会引发pyautogui.FailSafeException错误进而中止程序。关闭命令如下（不建议关闭）
    pyautogui.FAILSAFE = False
    # 单击之后拖动
    # 用n秒时间将鼠标从当前位置拖动到(x,y)位置
    x = 0
    y = 0
    n = 2
    pyautogui.dragTo(x, y, duration=n)


def mouse_drag_offset():
    xOffset = 150
    yOffset = 150
    n = 2
    pyautogui.dragRel(xOffset=xOffset, yOffset=yOffset, duration=n)


def mouse_click():
    """
    当没有传递任何参数时，在鼠标光标的当前位置单击主鼠标按钮。
    参数解释:
        x = 目标位置 x 坐标
        y = 目标位置 y 坐标
        clicks = 单击次数
        interval = 每次单击间隔次数
        button = 'left'左键单击，'middle'中键单击，'right'右键单击
    :return: 
    """
    x = 1230
    y = 720
    clicks = 3
    interval = 2
    button = 'right'
    # pyautogui.click(x=x, y=y, clicks=clicks, interval=interval, button=button)
    pyautogui.click()


def other_click():
    moveToX = 10
    moveToY = 20
    # 右键单击
    pyautogui.rightClick(x=moveToX + 50, y=moveToY)
    # 中键单击
    pyautogui.middleClick(x=moveToX + 50, y=moveToY)
    # 左键双击
    pyautogui.doubleClick(x=moveToX + 50, y=moveToY)
    # 左键三击
    pyautogui.tripleClick(x=moveToX + 50, y=moveToY)


def scroll_down():
    """
    执行鼠标滚轮的滚动。垂直滚动还是水平滚动取决于底层操作系统。
    x 和 y 参数详细说明鼠标事件发生的位置。如果为 None，则使用当前鼠标位置。如果为浮点值，则向下舍入。如果超出屏幕边界，则事件发生在屏幕边缘。
    参数：
        clicks (int, float)：要执行的滚动量。
        x (int, float, None, tuple, 可选)：发生点击的屏幕上的 x 位置。默认情况下为 None。如果为 tuple，则用于 x 和 y。
        y (int, float, None, 可选)：发生点击的屏幕上的 y 位置。默认情况下为 None。
    :return:
    """

    moveToX = 100
    moveToY = 200
    # 鼠标在当前位置向下滑动100格
    # pyautogui.scroll(clicks=1000)
    # 鼠标移动到(moveToX,moveToY)位置，然后向上滚动150格
    pyautogui.scroll(clicks=1500, x=moveToX, y=moveToY)


def pause_down():

    """
    移动到目标位置执行按下鼠标按钮（但不松开）的操作。
    x 和 y 参数详细说明鼠标事件发生的位置。如果为 None，则使用当前鼠标位置。如果为浮点值，则向下舍入。如果超出屏幕边界，则事件发生在屏幕边缘。

    参数：
        x（整数、浮点、无、元组、可选）：鼠标按下时在屏幕上的 x 位置。默认情况下为 None。如果为元组，则将其用于 x 和 y。
        如果 x 是字符串，则将其视为图像的文件名，使用locateOnScreen()在屏幕上查找并单击其中心。
        y（整数、浮点、无、可选）：鼠标按下时在屏幕上的 y 位置。默认情况下为 None。
        button（字符串、整数、可选）：按下的鼠标按钮。
    :return:
    """
    x = 1230
    y = 720
    pyautogui.mouseDown(x=x, y=y, button='left')


if __name__ == '__main__':
    pause_down()
