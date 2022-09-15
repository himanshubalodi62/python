import logging
logging.basicConfig(
    filename="example.log",
    level=logging.INFO,
    format='%(levelname)s %(asctime)s %(message)s')

class List_task:
    def __init__(self, list_x):
        self.list_x = list_x

    def reverse_list(self):
        if len(self.list_x) != 0:
            return self.list_x[::-1]
        else:
            raise ValueError("List is empty")

    def extract_info(self):
        if len(self.list_x) != 0:
            return self.list_x[7][0]
        else:
            raise IndexError("index is out of range")
    def extract_info(self):
        if len(self.list_x) != 0:
            return self.list_x[5][1]
        else:
            raise IndexError("index is out of range")
    def extract_info(self):
        if len(self.list_x)!= 0:
            return self.list_x[8]['key1']
        else:
            raise IndexError("index is out of the range")
    def extract_info(self):
        if len(self.list_x)!= 0:
            return self.list_x[8].keys()
    def extract_info(self):
        if len(self.list_x)!= 0:
            return self.list_x[8].values()


def get_list_info(data):
    try:
        obj = List_task(list_x=data)
        # result = obj.reverse_list()
        # logging.info(f"reversed result: {result}")
        extracted_result = obj.extract_info()
        logging.info(f"extracted result: {extracted_result}")
        extracted_result = obj.extract_info()
        logging.info(f"extracted result: {extracted_result}")
        extracted_result = obj.extract_info()
        logging.info(f"extracted result: {extracted_result}")
        extracted_result = obj.extract_info()
        logging.info(f"extracted result: {extracted_result}")
        extracted_result = obj.extract_info()
        logging.info(f"extracted result: {extracted_result}")
    except Exception as e:
        logging.exception(e)

data = [3,4,5,6,7 ,[23,456,67,8,78,78],[345,56,87,8,98,9],(234,657,6),{"key1":"himu",234:[23,45,657]}]
data1 = []
data2 = []
data3 = []
data4 = []
data5 =[]
get_list_info(data)
get_list_info(data1)
get_list_info(data2)
get_list_info(data3)
get_list_info(data4)
get_list_info(data5)