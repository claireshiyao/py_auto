# author by claire
from common.db_handler import DBHandler
from middlerware.helper import Context
from middlerware.read_yml import yaml_data


class DB1:

    def __init__(self):
        self.db = DBHandler(host=yaml_data['database']['host'],
                                port=yaml_data['database']['port'],
                                user=yaml_data['database']['user'],
                                password=yaml_data['database']['password'],
                                database=yaml_data['database']['database'],
                                charset=yaml_data['database']['charset'])
        self.member_id = Context().member_id
    def query1(self):

        res = self.db.query('update member set leave_amount = 20000 where id = %s;', args=[self.member_id, ])
        return res

if __name__ == '__main__':
    db = DB1()
    print(db.member_id)
    print(db.query1())
