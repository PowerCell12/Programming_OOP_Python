class EmailValidator:

  def __init__(self, min_length, mails, domains):
    self.min_length = min_length
    self.mails = mails
    self.domains = domains


  def __is_name_valid(self, name):

    if len(name) >= self.min_length:
      return True
    else:
      return False



  def __is_mail_valid(self, mail):

    if mail in self.mails:
      return True
    else:
      return False



  def __is_domain_valid(self, domain):
    if domain in self.domains:
      return True
    else:
      return False


  def validate(self, email):

    name1, other = email.split("@")

    mail1, domain1 = other.split(".")


    
    first = self.__is_name_valid(name1)
    second = self.__is_mail_valid(mail1)
    third = self.__is_domain_valid(domain1)

    if first and second and third:
      return True
    else: 
      return False
