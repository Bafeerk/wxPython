import wx


APP_EXIT = 1
class ContextMenu(wx.Menu):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        it_min = self.Append(wx.ID_ANY, 'Минимизировать')
        it_max = self.Append(wx.ID_ANY, 'Распахнуть')
        self.Bind(wx.EVT_MENU, self.onMinimize, it_min)
        self.Bind(wx.EVT_MENU, self.onMaximize, it_max)


    def onMinimize(self, event):
        self.parent.Iconize()

    def onMaximize(self, event):
        self.parent.Maximize()


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()


        fileMenu.Append(wx.ID_NEW, '&Новый\tCtrl+N')
        fileMenu.Append(wx.ID_OPEN, '&Открыть\tCtrl+O')
        fileMenu.Append(wx.ID_SAVE, '&Сохранить\tCtrl+S')
        fileMenu.AppendSeparator()
        item = wx.MenuItem(fileMenu, APP_EXIT, 'Выход\tCtrl+Q', 'Выход из приложения')
        fileMenu.Append(item)

        viewMenu = wx.Menu()


        menubar.Append(fileMenu, '&File')

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)

        self.ctx = ContextMenu(self)
        self.Bind(wx.EVT_RIGHT_DOWN, self.onRightDown)

        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, 'Выход', wx.Bitmap('vk.png'))
        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)
        toolbar.Realize()


    def onQuit(self, event):
        self.Close()

    def onRightDown(self, event):
        self.PopupMenu(self.ctx, event.GetPosition())




app = wx.App()
frame = MyFrame(None, title='Hello world!')
frame.Show()
app.MainLoop()