from app.libs.redpirnt import Redprint

api=Redprint('user')

@api.route('', methods=['GET'])
def get_user():
    return 'get user'

@api.route('', methods=['POST'])
def create_user():
    return 'create user'