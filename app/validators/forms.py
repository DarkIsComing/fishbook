from app.validators.base import BaseForm as Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, Regexp,length
from app.libs.enums import ClientTypeEnum
class ClientForm(Form):
    account=StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=32)])
    secret=StringField()
    type=IntegerField(validators=[DataRequired()])

    def validate_type(self,value):
            try:
                client=ClientTypeEnum(value.data)       #如果value中的值不是ClientTypeEnum枚举类中定义的属性的值，那么会报valueError错误。
            except ValueError as e:
                raise e
            self.type.data=client

class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])
