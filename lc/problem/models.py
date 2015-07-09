class Problem(Document):
  MULTIPLE_CHOICE = 'MC'
  SHORT_ANSWER = 'SA'
  TYPES = (MULTIPLE_CHOICE,'Multiple Choice',SHORT_ANSWER,'Short Answer')
  
  slug = StringField(max_length=255,unique=True)
  title = StringField(max_length=255,required=True)
  created_at = DateTimeField(default=datetime.datetime.now)
  updated_at = DateTimeField(default=datetime.datetime.now)
  description = StringField()
  author = ReferenceField(User)
  problem_type = StringField(max_length=2,default=MULTIPLE_CHOICE,choices=TYPES)
  subject = ReferenceField('Subject')