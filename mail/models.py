from mongoengine import *
import datetime

class Mail:
  def __init__(self,_from,to,subject,text):
    self._from = _from
    self._to = to
    self.subject = subject
    self.text = text

  def getFrom(self):
    return self._from

  def getTo(self):
    return self._to

  def getSubject(self):
    return self._subject

  def getText(self):
    return self._text