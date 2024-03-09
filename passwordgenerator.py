###########################################################################
# Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
# http://www.wxformbuilder.org/
#
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
# Автор Клинцов Сергей © 2024
# e-mail:
###########################################################################

import wx
import wx.xrc
from string import digits, ascii_lowercase, ascii_uppercase, punctuation
import password
import time


###########################################################################
# Class MyFramePG
###########################################################################

class MyFramePG(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self,
                          parent,
                          id=wx.ID_ANY,
                          title=u"Генератор паролей.",
                          pos=wx.DefaultPosition,
                          size=wx.Size(480, 530),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.Size(480, 530), wx.DefaultSize)

        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))
        self.clipboard = wx.Clipboard()

        ###########################################################################
        # bSizer_window
        ###########################################################################

        bSizer_window = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap1 = wx.StaticBitmap(self,
                                         id=wx.ID_ANY,
                                         bitmap=wx.Bitmap(u"images/screensaver.png",
                                                          wx.BITMAP_TYPE_ANY),
                                         pos=wx.DefaultPosition,
                                         size=wx.DefaultSize,
                                         style=0)
        bSizer_window.Add(self.m_bitmap1,
                          proportion=0,
                          flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL,
                          border=5)

        ###########################################################################
        # bSizer_window / bSizer_entry
        ###########################################################################

        bSizer_entry = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_entry_parole = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl_parole = wx.TextCtrl(self,
                                             id=wx.ID_ANY,
                                             value=wx.EmptyString,
                                             pos=wx.DefaultPosition,
                                             size=wx.Size(300, 30),
                                             style=wx.TE_READONLY)
        self.m_textCtrl_parole.SetFont(wx.Font(pointSize=14,
                                               family=wx.FONTFAMILY_DEFAULT,
                                               style=wx.FONTSTYLE_NORMAL,
                                               weight=wx.FONTWEIGHT_NORMAL,
                                               underline=False,
                                               faceName=wx.EmptyString))

        bSizer_entry_parole.Add(self.m_textCtrl_parole,
                                proportion=0,
                                flag=wx.ALIGN_CENTER_VERTICAL,
                                border=5)

        ###########################################################################################################
        self.m_textCtrl_parole_hide = wx.TextCtrl(self,
                                                  id=wx.ID_ANY,
                                                  value=wx.EmptyString,
                                                  pos=wx.DefaultPosition,
                                                  size=wx.Size(300, 30),
                                                  style=wx.TE_PASSWORD | wx.TE_READONLY)
        self.m_textCtrl_parole_hide.SetFont(wx.Font(pointSize=14,
                                                    family=wx.FONTFAMILY_DEFAULT,
                                                    style=wx.FONTSTYLE_NORMAL,
                                                    weight=wx.FONTWEIGHT_NORMAL,
                                                    underline=False,
                                                    faceName=wx.EmptyString))
        self.m_textCtrl_parole_hide.Hide()

        bSizer_entry_parole.Add(self.m_textCtrl_parole_hide,
                                proportion=0,
                                flag=wx.ALIGN_CENTER_VERTICAL,
                                border=5)
        ###########################################################################################################

        bSizer_entry.Add(bSizer_entry_parole,
                         proportion=0,
                         flag=wx.ALIGN_CENTER_VERTICAL,
                         border=5)

        ###########################################################################################################

        self.m_button_visible = wx.ToggleButton(self,
                                                id=wx.ID_ANY,
                                                label=wx.EmptyString,
                                                pos=wx.DefaultPosition,
                                                size=wx.DefaultSize,
                                                style=0)

        self.m_button_visible.SetBitmap(wx.Bitmap(u"icons/outline_visibility_black_24dp.png",
                                                  type=wx.BITMAP_TYPE_ANY))
        self.m_button_visible.SetBitmapPressed(wx.Bitmap(u"icons/outline_visibility_off_black_24dp.png",
                                                         type=wx.BITMAP_TYPE_ANY))
        self.m_button_visible.SetMinSize(wx.Size(width=40, height=40))
        self.m_button_visible.SetToolTip(u"Скрыть/показать пароль.")

        bSizer_entry.Add(self.m_button_visible,
                         proportion=0,
                         flag=wx.ALIGN_CENTER_VERTICAL,
                         border=10)

        self.m_button_regenerate = wx.Button(self,
                                             id=wx.ID_ANY,
                                             label=wx.EmptyString,
                                             pos=wx.DefaultPosition,
                                             size=wx.DefaultSize,
                                             style=0)

        self.m_button_regenerate.SetBitmap(wx.Bitmap(u"icons/outline_restart_alt_black_24dp.png",
                                                     type=wx.BITMAP_TYPE_ANY))
        self.m_button_regenerate.SetMinSize(wx.Size(width=40, height=40))
        self.m_button_regenerate.SetToolTip(u"Создать пароль.")
        self.m_button_regenerate.SetFocus()

        bSizer_entry.Add(self.m_button_regenerate,
                         proportion=0,
                         flag=wx.ALIGN_CENTER_VERTICAL,
                         border=10)

        self.m_button_copy = wx.Button(self,
                                       id=wx.ID_ANY,
                                       label=wx.EmptyString,
                                       pos=wx.DefaultPosition,
                                       size=wx.DefaultSize,
                                       style=0)

        self.m_button_copy.SetBitmap(wx.Bitmap(u"icons/outline_content_copy_black_24dp.png",
                                               type=wx.BITMAP_TYPE_ANY))
        self.m_button_copy.SetMinSize(wx.Size(width=40, height=40))
        self.m_button_copy.SetToolTip(u"Копировать пароль в буфер обмена.")

        bSizer_entry.Add(self.m_button_copy,
                         proportion=0,
                         flag=wx.ALIGN_CENTER_VERTICAL,
                         border=10)

        bSizer_window.Add(bSizer_entry,
                          proportion=1,
                          flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL,
                          border=5)
        ###########################################################################

        self.m_static_line_one = wx.StaticLine(self,
                                               id=wx.ID_ANY,
                                               pos=wx.DefaultPosition,
                                               size=wx.DefaultSize,
                                               style=wx.LI_HORIZONTAL)
        bSizer_window.Add(self.m_static_line_one,
                          proportion=0,
                          flag=wx.EXPAND | wx.ALL,
                          border=5)

        ###########################################################################
        # bSizer_window / bSizer_lenght
        ###########################################################################

        bSizer_lenght = wx.BoxSizer(wx.HORIZONTAL)

        self.m_slider1 = wx.Slider(self,
                                   id=wx.ID_ANY,
                                   value=15,
                                   minValue=1,
                                   maxValue=100,
                                   pos=wx.DefaultPosition,
                                   size=wx.Size(width=300, height=-1),
                                   style=wx.SL_HORIZONTAL)
        self.m_slider1.SetToolTip(u"Количество символов в пароле.")
        bSizer_lenght.Add(self.m_slider1,
                          proportion=0,
                          flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                          border=5)

        self.m_bitmap2 = wx.StaticBitmap(self,
                                         id=wx.ID_ANY,
                                         bitmap=wx.Bitmap(u"icons/outline_password_black_24dp.png",
                                                          type=wx.BITMAP_TYPE_ANY),
                                         pos=wx.DefaultPosition,
                                         size=wx.DefaultSize,
                                         style=0)
        bSizer_lenght.Add(self.m_bitmap2,
                          proportion=0,
                          flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                          border=5)

        self.m_textCtrl2 = wx.TextCtrl(self,
                                       id=wx.ID_ANY,
                                       value=wx.EmptyString,
                                       pos=wx.DefaultPosition,
                                       size=wx.DefaultSize,
                                       style=wx.TE_READONLY)
        self.m_textCtrl2.SetValue(str(self.m_slider1.GetValue()))

        bSizer_lenght.Add(self.m_textCtrl2,
                          proportion=0,
                          flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                          border=5)

        bSizer_window.Add(bSizer_lenght,
                          proportion=1,
                          flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL,
                          border=5)

        ###########################################################################

        self.m_static_line_two = wx.StaticLine(self,
                                               id=wx.ID_ANY,
                                               pos=wx.DefaultPosition,
                                               size=wx.DefaultSize,
                                               style=wx.LI_HORIZONTAL)
        bSizer_window.Add(self.m_static_line_two,
                          proportion=0,
                          flag=wx.EXPAND | wx.ALL,
                          border=5)

        ###########################################################################
        # bSizer_window / bSizer_symbols
        ###########################################################################

        bSizer_symbols = wx.BoxSizer(wx.HORIZONTAL)

        self.m_toggleBtn_digit = wx.ToggleButton(self,
                                                 id=wx.ID_ANY,
                                                 label=u"0-9",
                                                 pos=wx.DefaultPosition,
                                                 size=wx.DefaultSize,
                                                 style=0)

        self.m_toggleBtn_digit.SetMinSize(wx.Size(width=100, height=-1))
        self.m_toggleBtn_digit.SetToolTip(u"включить в набор цифры")
        self.m_toggleBtn_digit_var = ""

        bSizer_symbols.Add(self.m_toggleBtn_digit,
                           proportion=0,
                           flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                           border=5)

        self.m_toggleBtn_lower = wx.ToggleButton(self,
                                                 id=wx.ID_ANY,
                                                 label=u"a-z",
                                                 pos=wx.DefaultPosition,
                                                 size=wx.DefaultSize,
                                                 style=0)
        self.m_toggleBtn_lower.SetMinSize(wx.Size(width=100, height=-1))
        self.m_toggleBtn_lower.SetToolTip(u"Включить в набор прописные буквы.")
        self.m_toggleBtn_lower_var = ""

        bSizer_symbols.Add(self.m_toggleBtn_lower,
                           proportion=0,
                           flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                           border=5)

        self.m_toggleBtn_upper = wx.ToggleButton(self,
                                                 id=wx.ID_ANY,
                                                 label=u"A-Z",
                                                 pos=wx.DefaultPosition,
                                                 size=wx.DefaultSize,
                                                 style=0)
        self.m_toggleBtn_upper.SetMinSize(wx.Size(width=100, height=-1))
        self.m_toggleBtn_upper.SetToolTip(u"Включить в набор заглавные буквы.")
        self.m_toggleBtn_upper_var = ""

        bSizer_symbols.Add(self.m_toggleBtn_upper,
                           proportion=0,
                           flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                           border=5)

        self.m_toggleBtn_special = wx.ToggleButton(self,
                                                   id=wx.ID_ANY,
                                                   label=u"@#$%&",
                                                   pos=wx.DefaultPosition,
                                                   size=wx.DefaultSize,
                                                   style=0)
        self.m_toggleBtn_special.SetMinSize(wx.Size(width=100, height=-1))
        self.m_toggleBtn_special.SetToolTip(u"Включить в набор спецсимволы.")
        self.m_toggleBtn_special_var = ""

        bSizer_symbols.Add(self.m_toggleBtn_special,
                           proportion=0,
                           flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                           border=5)

        bSizer_window.Add(bSizer_symbols,
                          proportion=1,
                          flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL,
                          border=5)

        ###########################################################################
        # Layout() / bSizer_window
        ###########################################################################

        self.SetSizer(bSizer_window)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(number=1,
                                                 style=wx.STB_SIZEGRIP,
                                                 id=wx.ID_ANY)
        self.timer = wx.Timer(self)
        self.timer.Start(milliseconds=1000, oneShot=wx.TIMER_CONTINUOUS)

        self.Centre(wx.BOTH)

        ###########################################################################
        # events
        ###########################################################################

        self.m_button_visible.Bind(event=wx.EVT_TOGGLEBUTTON,
                                   handler=self.visible_sicret)
        self.m_button_regenerate.Bind(event=wx.EVT_BUTTON,
                                      handler=self.password_regenerate)
        self.m_button_copy.Bind(event=wx.EVT_BUTTON,
                                handler=self.password_copy)
        self.m_slider1.Bind(event=wx.EVT_SLIDER,
                            handler=self.slider_to_entry)
        self.m_toggleBtn_digit.Bind(event=wx.EVT_TOGGLEBUTTON,
                                    handler=self.char_digit)
        self.m_toggleBtn_lower.Bind(event=wx.EVT_TOGGLEBUTTON,
                                    handler=self.char_lower)
        self.m_toggleBtn_upper.Bind(event=wx.EVT_TOGGLEBUTTON,
                                    handler=self.char_upper)
        self.m_toggleBtn_special.Bind(event=wx.EVT_TOGGLEBUTTON,
                                      handler=self.char_special)
        self.Bind(wx.EVT_TIMER, self.on_timer)

    def __del__(self):
        pass

    ###########################################################################
    # Обработчики событий
    ###########################################################################

    def visible_sicret(self, event):
        """Скрытие поля с символами пароля."""
        if self.m_button_visible.GetValue():
            self.m_textCtrl_parole.Hide()
            self.m_textCtrl_parole_hide.Show()
            self.m_textCtrl_parole_hide.SetValue(str(self.m_textCtrl_parole.GetValue()))
            self.m_textCtrl_parole_hide.SetFocus()
            self.m_textCtrl_parole_hide.GetParent().Layout()
        else:
            self.m_textCtrl_parole.Show()
            self.m_textCtrl_parole_hide.Hide()
            self.m_textCtrl_parole.SetValue(str(self.m_textCtrl_parole_hide.GetValue()))
            self.m_textCtrl_parole.SetFocus()
            self.m_textCtrl_parole.GetParent().Layout()
        event.Skip()

    def password_regenerate(self, event):
        """Генерация пароля."""
        top = (len(self.m_toggleBtn_digit_var) +
               len(self.m_toggleBtn_lower_var) +
               len(self.m_toggleBtn_upper_var) +
               len(self.m_toggleBtn_special_var))
        if top != 0:
            self.m_textCtrl_parole.SetValue(password.create_new(lenght=self.m_slider1.GetValue(),
                                                                characters=self.character_set()))
            self.m_textCtrl_parole_hide.SetValue(str(self.m_textCtrl_parole.GetValue()))
        else:
            self.m_textCtrl_parole.SetValue("Нужно выбрать символы.")
        event.Skip()

    def password_copy(self, event):
        """Копирование пароля в буфер обмена."""
        if self.clipboard.Open():
            self.clipboard.SetData(wx.TextDataObject(str(self.m_textCtrl_parole.GetValue())))
            self.clipboard.Close()
        else:
            self.clipboard.Open()
            self.clipboard.SetData(wx.TextDataObject(str(self.m_textCtrl_parole.GetValue())))
            self.clipboard.Close()
        event.Skip()

    def slider_to_entry(self, event):
        """Сопоставление положения слайдера и числа в строке"""
        self.m_textCtrl2.SetValue(str(self.m_slider1.GetValue()))
        event.Skip()

    def char_digit(self, event):
        """Добавление/исключение набора цифр в строку генерации пароля."""
        if self.m_toggleBtn_digit.GetValue():
            self.m_toggleBtn_digit_var = digits
        else:
            self.m_toggleBtn_digit_var = ""
        event.Skip()

    def char_lower(self, event):
        """Добавление/исключение набора строчных букв в строку генерации пароля."""
        if self.m_toggleBtn_lower.GetValue():
            self.m_toggleBtn_lower_var = ascii_lowercase
        else:
            self.m_toggleBtn_lower_var = ""
        event.Skip()

    def char_upper(self, event):
        """Добавление/исключение набора прописных букв в строку генерации пароля."""
        if self.m_toggleBtn_upper.GetValue():
            self.m_toggleBtn_upper_var = ascii_uppercase
        else:
            self.m_toggleBtn_upper_var = ""
        event.Skip()

    def char_special(self, event):
        """Добавление/исключение набора спецсимволов в строку генерации пароля."""
        if self.m_toggleBtn_special.GetValue():
            self.m_toggleBtn_special_var = punctuation
        else:
            self.m_toggleBtn_special_var = ""
        event.Skip()

    def character_set(self):
        """Объединение наборов в строку генерации пароля."""
        CHAR = "".join(self.m_toggleBtn_digit_var +
                       self.m_toggleBtn_lower_var +
                       self.m_toggleBtn_upper_var +
                       self.m_toggleBtn_special_var)
        return CHAR

    def on_timer(self, event):
        """Размещение в строке статуса текущего времени."""
        tl = time.localtime()
        mt = ("января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября",
              "декабря")
        wd = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
        str_status_bar_time = ("  " + wd[tl.tm_wday] + " " + str(tl.tm_mday) + " " + mt[tl.tm_mon] + " " + str(
            tl.tm_year) + " года. " + str(tl.tm_hour) + ":" + str(tl.tm_min) + ":" + str(tl.tm_sec))
        self.m_statusBar1.SetStatusText(str_status_bar_time, 0)


if __name__ == "__main__":
    app = wx.App(0)
    win = MyFramePG(None)
    win.Show()
    app.MainLoop()
