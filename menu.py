import wx


APP_EXIT = 1
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        expMenu = wx.Menu()

        expMenu.Append(wx.ID_ANY, 'Экспорт изображения')
        expMenu.Append(wx.ID_ANY, 'Экспорт видео')
        expMenu.Append(wx.ID_ANY, 'Экспорт данных')

        fileMenu.Append(wx.ID_NEW, '&Новый\tCtrl+N')
        fileMenu.Append(wx.ID_OPEN, '&Открыть\tCtrl+O')
        fileMenu.Append(wx.ID_SAVE, '&Сохранить\tCtrl+S')
        fileMenu.AppendSubMenu(expMenu, '&Экспорт')
        fileMenu.AppendSeparator()
        item = wx.MenuItem(fileMenu, APP_EXIT, 'Выход\tCtrl+Q', 'Выход из приложения')
        fileMenu.Append(item)

        viewMenu = wx.Menu()
        self.vStatus = viewMenu.Append(VIEW_STATUS, 'Статусная строка', kind=wx.ITEM_CHECK)
        self.vRgb = viewMenu.Append(VIEW_RGB, 'Тип RGB', 'Тип RGB', kind=wx.ITEM_RADIO)
        self.vSrgb = viewMenu.Append(VIEW_SRGB, 'Тип sRGB', 'Тип sRGB', kind=wx.ITEM_RADIO)

        menubar.Append(fileMenu, '&File')
        menubar.Append(viewMenu, '&Вид')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)
        self.Bind(wx.EVT_MENU, self.onStatus, id=VIEW_STATUS)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_RGB)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_SRGB)

    def onQuit(self, event):
        self.Close()

    def onStatus(self, event):
        if self.vStatus.IsChecked():
            print('Показать статусную строку')
        else:
            print('Скрыть статусную строку')

    def onImageType(self, event):
        if self.vRgb.IsChecked():
            print('Режим RGB')
        elif self.vSrgb.IsChecked():
            print('Режим sRGB')


app = wx.App()
frame = MyFrame(None, title='Hello world!')
frame.Show()
app.MainLoop()