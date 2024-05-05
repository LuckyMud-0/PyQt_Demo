from abc import abstractmethod
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

COLOR_GRAY = QtGui.QColor(128, 128, 128)
COLOR_RED  = QtGui.QColor(255, 0, 0)
COLOR_GREEN = QtGui.QColor(0, 255, 0)
COLOR_BLUE = QtGui.QColor(0, 0, 255)
COLOR_WHITE = QtGui.QColor(255, 255, 255)
COLOR_BLACK = QtGui.QColor(0, 0, 0)

class Test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Demo")
        
        self.timer = QtCore.QBasicTimer()
        self.fps = 2
        self.delay = 1000 // self.fps
        self.is_show = False
        
    def set_fps(self, fps):
        self.delay = 1000 // fps
        self.fps = fps
        if self.timer.isActive():
            self.timer.stop()
            self.timer.start(self.delay, self)
        
    def timerEvent(self, event):
        if not self.is_show:
            self.timer.stop()
        else:
            self.on_time_event(event)
        
        self.repaint()
        
    @abstractmethod
    def on_time_event(self):
        pass
        
    @abstractmethod
    def draw_content(self, qp: QtGui.QPainter):
        pass
    
    def paintEvent(self, event: QtGui.QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw_content(qp)
        qp.end()
        
    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
            return
        elif event.key() == QtCore.Qt.Key_F2:
            if not self.is_show:
                self.start_show()
                return
        elif event.key() == QtCore.Qt.Key_F1:
            self.is_show = False
            
        super().keyPressEvent(event)
        
    def start_show(self):
        self.is_show = True
        self.timer.start(self.delay, self)
        
    @classmethod
    def start(cls):
        app = QtWidgets.QApplication(sys.argv)
        # 创建cls的对象
        test = cls()
        test.start_show()
        test.show()
        # while (1): 
        # app.exec_()
        sys.exit(app.exec_())