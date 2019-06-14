from flask import request
from app.libs.redpirnt import Redprint
from app.validators.forms import ClientForm ,UserEmailForm
from app.libs.enums import ClientTypeEnum
from app.models.user import User
api=Redprint('client')

@api.route('/register', methods=['POST'])
def create_client():
    form=ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return 'Success'
@staticmethod
def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)