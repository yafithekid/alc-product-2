from mail.models import Mail

class ConfirmationEmail(Mail):
  def __init__(self,email,token):
    FROM = 'no-reply@yafisquare.com'
    SUBJECT = 'Account Confirmation'
    TEXT = 'please click this link: ' + token
    super().__init__(self,FROM,email,SUBJECT,TEXT):