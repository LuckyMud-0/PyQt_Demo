from z_game import Test
from PyQt5 import QtWidgets, QtGui, QtCore
import math
import random

class Point:
    point_list = [
        [0,   0], 
        [30,  0],
        [60,  0],
        [90,  0],
        [120, 0], 
        [150, 0], 
        [180, 0], 
        [210, 0], 
        [240, 0], 
        [270, 0], 
        [300, 0], 
        [330, 0],
        [360, 0],
    ]
    p_width = 10
    p_height = 10
    def __init__(self, angle, distance, w, h):
        self.w = w
        self.h = h
        self.x = Demo.width / 2 + (distance * Demo.w_rate) * math.cos(math.radians(angle)) - w / 2
        self.y = Demo.height / 2 - (distance * Demo.h_rate) * math.sin(math.radians(angle)) - h / 2
    
    # def __str__(self) -> str:
    #     return "({}, {}, {}, {})".format(self.x, self.y, self.w, self.h)
        
    # def draw(self, qp: QtGui.QPainter):
    #     qp.drawEllipse(self.x, self.y, self.w, self.h)
    
    @classmethod
    def draw_points(cls, qp: QtGui.QPainter): 
        qp.setBrush(QtGui.QColor(255, 0, 0, 128))
        # qp.setPen(QtGui.QColor(255, 0, 0))
        if Line.angle == 360:
            cls.point_list[0] = [0, 0]
        if Line.angle == 0:
            cls.point_list[len(cls.point_list) - 1] = [360, 0]
        for point in cls.point_list: 
            if point[0] == Line.angle: 
                # 
                point[1] = random.randint(2, 400)
            #
            if point[1] <= 2: 
                continue
            if Line.first and point[0] > Line.angle: 
                continue
            else: 
                p = cls(point[0], point[1], cls.p_width, cls.p_height)
                # print(p)
                qp.drawEllipse(p.x, p.y, p.w, p.h)
        # print(cls.point_list)   
             
    @classmethod
    def generate_points(cls): 
        for i in range(len(cls.point_list)): 
            cls.point_list[i][1] = random.randint(2, 400)
    
class Line:
    angle = 0
    step = 10
    dir = 1
    first = True
    # def __init__(self, angle, c):
    #     self.x = Demo.width // 2 + Demo.width // 2 * math.cos(math.radians(angle))
    #     self.y = Demo.height // 2 - Demo.width // 2 * math.sin(math.radians(angle))
    #     self.color = c
    
    @classmethod
    def draw(cls, qp: QtGui.QPainter):
        qp.setPen(QtGui.QColor(255, 0, 0))
        x = Demo.width // 2 + Demo.width // 2 * math.cos(math.radians(cls.angle))
        y = Demo.height // 2 - Demo.width // 2 * math.sin(math.radians(cls.angle))
        # print(Line.angle, Line.dir)
        qp.drawLine(Demo.width // 2, Demo.height // 2, x, y)

class Demo(Test): 
    
    width = 600
    height = 600
    
    # max_distance = 400
    w_rate =  width / 2 / 400
    h_rate =  height / 2 / 400
    
    def __init__(self):
        super().__init__()
        # 设置宽度高度属性
        self.setFixedSize(Demo.width, Demo.height)
        # 
        print(Demo.w_rate, Demo.h_rate)
        # 
        self.set_fps(30)
    
    def on_time_event(self, event):
        Line.angle += Line.step * Line.dir
        # print(Line.angle)
        if Line.angle >= 360: 
            Line.first = False
            Line.dir = -1
        elif Line.angle <= 0: 
            Line.dir = 1
        
    
    def draw_content(self, qp: QtGui.QPainter):
        # 设置背景颜色
        qp.setBrush(QtGui.QColor(0, 255, 0, 128))
        qp.drawRect(0, 0, Demo.width, Demo.height)
        # 以画面中心为坐标原点，画一个圆形
        qp.setPen(QtGui.QColor(255, 0, 0))
        # qp.drawEllipse(0, 0, Demo.width, Demo.height)
        for i in range(4): 
            qp.drawEllipse(Demo.width // 2 // 4 * i, Demo.height // 2 // 4 * i, 
                           Demo.width // 4 * (4 - i), Demo.height // 4 * (4 - i))
        # 
        qp.setPen(QtGui.QColor(200, 200, 200))
        # 
        for i in range(6): 
            angle = 30 * i
            if i == 3:
                qp.drawLine(Demo.width // 2, 0, 
                    Demo.width // 2, Demo.height)
            else:
                qp.drawLine(0, Demo.height // 2 + Demo.width // 2 * math.tan(math.radians(angle)), 
                    Demo.width, Demo.height // 2 - Demo.width // 2 * math.tan(math.radians(angle)))
        # 
        qp.setPen(QtGui.QColor(255, 0, 0))
        for i in range(12): 
            angle = 30 * i
            x = Demo.width // 2 + Demo.width // 2 * math.cos(math.radians(angle))
            y = Demo.height // 2 - Demo.width // 2 * math.sin(math.radians(angle))
            # print(Line.angle, Line.dir)
            if angle == 90:
                qp.drawText(x, y + 20, "90°")
            elif angle == 0:
                qp.drawText(x - 20, y, "0°")
            else: 
                qp.drawText(x, y, "{}°".format(angle))
        # 
        qp.setPen(QtGui.QColor(255, 0, 0))
        qp.drawText(20, 20, "Esc 退出")
        qp.drawText(20, 40, "F1 暂停")
        qp.drawText(20, 60, "F2 继续")
        # 
        Point.draw_points(qp)
        # 
        Line.draw(qp)
    
    def start_show(self):
        super().start_show()

if __name__ == '__main__': 
    Demo.start()
