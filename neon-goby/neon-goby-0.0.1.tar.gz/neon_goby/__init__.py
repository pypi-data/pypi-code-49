from neon_goby.clean import clean
from neon_goby.split import split

class NeonGoby(object):
  @staticmethod
  def parse(text):
    return split(clean(text))
