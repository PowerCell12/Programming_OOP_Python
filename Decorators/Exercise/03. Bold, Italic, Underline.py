def make_bold(function):
  def wraper(*args):

    return f"<b>{function(*args)}</b>"


  return wraper

def make_italic(function):
  def wraper(*args):
    return f"<i>{function(*args)}</i>"

  return wraper


def make_underline(function):
  def wraper(*args):
    return f"<u>{function(*args)}</u>"

  return wraper
