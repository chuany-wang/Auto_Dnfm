import pyautogui


def key_input():
    """
   针对消息中的每个字符执行按下键盘按键，然后释放。
   消息参数也可以是字符串列表，在这种情况下可以使用任何有效的键盘名称。
   由于这会执行一系列键盘按下操作，而不是按住按键，因此不能使用它来执行键盘快捷键。为此，请使用 hotkey() 函数。
   参数：
      消息（str，列表）：如果是字符串，则为要按下的字符。如果是列表，则为按顺序按下的按键的键名。有效名称列在 KEYBOARD_KEYS 中。
      间隔（浮点数，可选）：每次按下之间的秒数。
      默认为 0.0，表示按下之间无暂停。
    :return:
    """

    # 在当前位置输入文字text，每个字符输入间隔secs_between_keys秒
    # \n表示换行
    text = 'Hello world!\n'
    secs_between_keys = 0.1
    # pyautogui.typewrite(message=text, interval=secs_between_keys)
    # 在当前位置按下键盘各种键
    pyautogui.typewrite(['\t', 'a', 'b', 'c', 'left', 'backspace', 'enter', 'f1', '\n'], interval=secs_between_keys)
    # 查看所有支持按键
    # print(pyautogui.KEYBOARD_KEYS)


def key_up_key_down():
    """
    keydown:
        执行键盘按键而不释放。这将使该键处于按住状态。
        注意：出于某种原因，这似乎不会导致按键重复，就像键盘键在文本字段上按住时发生的情况一样。
    keyUp: 执行键盘按键释放（无需事先按下）。
    参数：
        key (str)：要按下的键。有效名称列在KEYBOARD_KEYS中。
    :return:
    """
    # 按下ctrl键
    pyautogui.keyDown('ctrl')
    # 按下v键，相当文字粘贴
    pyautogui.keyDown('v')
    # 松开ctrl键盘
    pyautogui.keyUp('ctrl')


def hot_key():
    """
    按顺序按下传递的参数上的按键，然后按相反顺序释放按键。

    效果是调用 hotkey('ctrl', 'shift', 'c') 将执行“Ctrl-Shift-C”热键/键盘快捷键按下。

    参数：
        key(s) (str)：按顺序按下的一系列按键。这也可以是要按下的按键字符串列表。
        interval (float，可选)：每次按下之间的秒数。
        默认为 0.0，表示按下之间无暂停。
    :return:
    """
    # ctrl+c 复制文字
    pyautogui.hotkey('ctrl', 'c')
    # ctrl+v 粘贴文字
    pyautogui.hotkey('ctrl', 'v')


def _press():
    """
    按下键盘按键，然后松开。

    参数：
      key (str, list): 要按下的键。有效名称列于KEYBOARD_KEYS。也可以是此类字符串的列表。
      Presses（整数，可选）：重复按下的次数。默认为 1，只需按一次。
      间隔（浮点数，可选）：每次按下之间的秒数。默认为 0.0，按下之间没有暂停。
      暂停（float，可选）：函数过程结束多少秒。默认情况下无，函数过程结束时不会暂停。
    返回：
      没有任何
    :return:
    """
    #  按下shift键
    pyautogui.keyDown('shift')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    #  松开shift键
    pyautogui.keyUp('shift')


def with_pyautogui():
    """
    上下文管理器，在进入时按下键盘按键，然后在退出时释放。
    参数：
        key (str, list)：要按下的键。有效名称列在KEYBOARD_KEYS 中。也可以是此类字符串的列表。
        pause (float，可选)：函数处理结束时需要多少秒。默认情况下为 None，表示函数处理结束时不暂停。
    :return:
    """
    # 按住shift
    with pyautogui.hold('shift'):
        # 连续按left,然后松开shift
        pyautogui.press(['left', 'left', 'left'])

    # 上面代码功能和下面代码实现功能相同
    # 按下shift键
    pyautogui.keyDown('shift')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    # 松开shift键
    pyautogui.keyUp('shift')


def alert_gui():
    # 警告窗口
    # alert_result = pyautogui.alert('点击确定返回字符串OK')
    # # 确认窗口
    # confirm_result = pyautogui.confirm('点击确定返回字符串OK，点击取消返回字符串Cancel')
    # # 点击ok保存输入的文字，点击Cancel返回None
    # prompt_result = pyautogui.prompt('输入文字')
    # # 点击ok保存输入的密码，点击Cancel返回None
    # # default默认文字，mask用什么符号代替输入的密码
    password_result = pyautogui.password(text='', title='', default='', mask='*')
    print(password_result)


def screen_shot():
    # region设置截图区域[x,y,w,h]，以(x,y)为左上角顶点，截宽w，高h的区域
    result = pyautogui.screenshot(imageFilename='result2.jpg', region=[10, 20, 100, 50])
    result.show()

    # # 截屏返回result对象
    # result = pyautogui.screenshot()
    # # result是PIL中的Image对象
    # print(type(result))
    # # 保存图像
    # result.save('result1.jpg')
    # # 展示图片
    # result.show()


if __name__ == '__main__':
    screen_shot()
