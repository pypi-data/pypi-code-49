import webbrowser

import tkinter as tk

help_sections = (
  {
    'title': 'Connecting to the robot',
    'content': ' '.join((
      'To connect to the robot, go to the  Skriware  menu and choose',
      ' Select interpreter . The interpreter should be automatically',
      'set to "MicroPython (ESP32)". Then you should choose the port.',
      'If no port is available, check if the robot is turned on and',
      'connected to the computer. If you still cannot see any ports,',
      'you should download and install USB drivers from',
      'https://www.ftdichip.com/Drivers/VCP.htm'
    )),
    'tags': {
      'hl': (' Skriware ', ' Select interpreter '),
    },
    'urls': {
      'ftdi': 'https://www.ftdichip.com/Drivers/VCP.htm'
    }
  },
)

class HelpWindow(tk.Toplevel):
  def __init__(self, *args, parent=None, **kwargs):
    super().__init__(*args, **kwargs)

    self.parent = parent

    self.protocol('WM_DELETE_WINDOW', self.close)
    self.wm_title('Help')
    self.wm_geometry('640x480+300+50')
    content_frame = tk.Frame(self, padx=10, pady=10)
    nav_frame = tk.Frame(self, padx=10, pady=10)

    i = 0
    for section in help_sections:
      title_lbl = tk.Label(
        content_frame, text=section['title'], font=(None,24), justify=tk.LEFT)
      title_lbl.grid(row=i, column=0, sticky='w')

      content_text = tk.Text(
        content_frame,
        height=5,
        padx=5,
        pady=5,
        wrap=tk.WORD,
        font=(None, '11'),
        width=75,
        background='white'
      ) 
      content_text.insert(tk.INSERT, section['content'])

      for tag, needles in section['tags'].items():
        for needle in needles:
          idx = section['content'].index(needle)
          content_text.tag_add(
            tag,
            '1.{}'.format(idx),
            '1.{}'.format(idx + len(needle))
          )
      
      for url_name, url in section['urls'].items():
        idx = section['content'].index(url)

        content_text.tag_add(
          'url_{}'.format(url_name),
          '1.{}'.format(idx),
          '1.{}'.format(idx + len(url))
        )

        content_text.tag_config(
          'url_{}'.format(url_name), foreground='blue', underline=1)

        content_text.tag_bind(
          'url_{}'.format(url_name),
          '<Button-1>',
          lambda e: webbrowser.open_new_tab(url)
        )

        content_text.tag_bind(
          'url_{}'.format(url_name),
          '<Enter>',
          lambda e, ct=content_text: ct.config(cursor='hand2')
        )

        content_text.tag_bind(
          'url_{}'.format(url_name),
          '<Leave>',
          lambda e, ct=content_text: ct.config(cursor='arrow')
        )

      content_text.tag_config('hl', foreground='green')
      content_text.config(state=tk.DISABLED)
      content_text.grid(row=i+1, column=0, sticky='w')
      i += 2

    ok_button = tk.Button(nav_frame, text='OK', command=self.close, width=15, height=2)
    ok_button.grid(row=0, column=0, sticky='w')
    content_frame.grid(row=0, column=0)
    nav_frame.grid(row=1, column=0)

  def close(self):
    self.parent.help_window = None
    self.destroy()
