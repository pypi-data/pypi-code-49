from thonny.workbench import (BasicUiThemeSettings, CompoundUiThemeSettings,
                              SyntaxThemeSettings)

class SkriwareTheme:
  @staticmethod
  def theme_image_map():
    return {
      #'run-current-script': 'media-playback-start48.png',
      #'stop': 'process-stop48.png',
      #'new-file': 'document-new48.png',
      #'open-file': 'document-open48.png',
      #'save-file': 'document-save48.png',
      #'debug-current-script': 'debug-run48.png',
      #'step-over': 'debug-step-over48.png',
      #'step-into': 'debug-step-into48.png',
      #'step-out': 'debug-step-out48.png',
      #'run-to-cursor': 'debug-run-cursor48.png',
      #'tab-close': 'window-close.png',
      #'tab-close-active': 'window-close-act.png',
      #'resume': 'resume48.png',
      #'zoom': 'zoom48.png',
      #'quit': 'quit48.png',
    }

  @staticmethod
  def theme() -> CompoundUiThemeSettings:
    '''This will be a long method'''
    return [
      {
        #'.': {'configure': {'background': '#00c7e1'}},
        'Menu': {
          'configure': {
            'background': '#f00'
          }
        },
        'Menubar': {
          'configure': {
            'foreground': '#f00'
          }
        }
      },
    ]

  @staticmethod
  def syntax_theme():
    return {}
