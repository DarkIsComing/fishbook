from app.libs.redpirnt import Redprint

api=Redprint('book')        #红图这里已经定位到/book了

@api.route('', methods=['GET'])              #这里就不用定位了。查询数据用’GET'方法表示
def get_book():
    return 'get book'

@api.route('', methods=['POST'])              #‘POST'方法表示新增资源。
def create_book():
    return 'create book'