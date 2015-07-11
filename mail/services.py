from .models import Mail

import hashlib

# class for user confirmation
class MailService:
  @staticmethod
  def sendMail(mail:Mail):
    print("stub send mail")
    # requests.post(
    #     "https://api.mailgun.net/v3/samples.mailgun.org/messages",
    #     auth=("api", "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"),
    #     data={"from": mail.getFrom(),
    #           "to": mail.getTo(),
    #           "subject": mail.getSubject(),
    #           "text": mail.getText()}
