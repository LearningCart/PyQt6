# Context Menu
# Context menus are small context-sensitive menus which typically appear 
# when right clicking on a window. Qt has support for generating these menus, 
# and widgets have a specific event used to trigger them.

# In the following example we are going to intercept the .contextMenuEvent a QMainWindow. 
# This event is fired whenever a context menu is about to be shown, and is passed 
# a single value event of type QContextMenuEvent.

# To intercept the event, we simply override the object method with our new method 
# of the same name. So in this case we can create a method on our MainWindow subclass 
# with the name contextMenuEvent and it will receive all events of this type.

import                      sys;
from PyQt6.QtCore    import Qt;
from PyQt6.QtGui     import QAction;
from PyQt6.QtWidgets import QMenu;
from PyQt6.QtWidgets import QMainWindow;
from PyQt6.QtWidgets import QApplication;


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

# signal-based approach to creating context menus.
class NewWindow(MainWindow):
    def __init__(self):
        super().__init__()
        self.show()

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))

        # This will give context menu at top left corner
        # context.exec();

        # Below will give context menu where it is clicked relative to QMainWindow
        context.exec(self.mapToGlobal(pos));


app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

window = NewWindow();
window.show();

app.exec()
