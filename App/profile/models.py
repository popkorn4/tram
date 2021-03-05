from .. import db

class tablet(db.Document):
     picture=db.StringField()
     Tablet_Id=db.SequenceField()
     Name=db.StringField()
     About=db.StringField()
     category=db.StringField()
     price = db.StringField()

 class categories(db.Document):
     head_id=db.SequenceField()
     name=db.StringField()

 class orders(db.Document):
     order_id = db.SequenceField()
     Name = db.StringField()
     Maile = db.StringField()
     tel = db.StringField()
     adress = db.StringField()
     tablets_id = db.ListField(db.EmbeddedDocumentField('tablet'))
