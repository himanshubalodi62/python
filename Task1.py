import logging
logging.basicConfig(filename="list.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(message)s')

class list_task:

# reverse list....
    def list_reverse(self , rev_list):
        logging.info("I am trying to reverse the entire list")
        self.rev_list = rev_list
        try:
            if len(rev_list) == 0:
                raise ValueError("Empty list")
                logging.error("Empty list")
            else:
                l = rev_list[::-1]
                print("reverse",l)
                logging.info("reverse list is %s:",l)
                return l
        except Exception as e:
            logging.exception(e)

# extract ..
    def list_extract(self,ext_list):
        logging.info("I am trying to extract 234 in the list")
        self.ext_list = ext_list
        try:
            if len(ext_list) == 0:
                raise ValueError("empty list")
                logging.error("empty list")
            else:
                l = ext_list[5][1]
                logging.info("Extract list is %s:",l)
                return l

        except Exception as e:
            logging.exception(e)

    def list_extract(self,ext_list):
        logging.info("I am trying to extract himu in the list")
        self.ext_list = ext_list
        try:
            if len(ext_list) == 0:
                raise ValueError("empty list")
                logging.error("empty list")
            else:
                l = ext_list[8]['key1']
                logging.info("Extract list is %s",l)
                return l
        except Exception as e:
            logging.exception(e)


    def list_extract(self, ext_list):
        logging.info("I am trying to extract 456 in the list")
        self.ext_list = ext_list
        try:
            if len(ext_list) == 0:
                raise ValueError("empty list")
                logging.error("empty list")
            else:
                l = ext_list[8]['key1']
                logging.info("Extract list is %s",l)
                return l
        except Exception as e:
            logging.exception(e)


r_list = list_task()
rev_l = r_list.list_reverse([3,4,5,6,7 ,[23,456,67,8,78,78],[345,56,87,8,98,9],(234,657,6),{"key1":"himu",234:[23,45,657]}])
print(rev_l)
e_list = list_task()
ext_l = e_list.list_extract([3,4,5,6,7 ,[23,456,67,8,78,78],[345,56,87,8,98,9],(234,657,6),{"key1":"himu",234:[23,45,657]}])
print(ext_l)
q_list = list_task()
ext_l = q_list.list_extract([3,4,5,6,7 ,[23,456,67,8,78,78],[345,56,87,8,98,9],(234,657,6),{"key1":"himu",234:[23,45,657]}])
print(ext_l)
m_list = list_task()
ext_l = m_list.list_extract([3,4,5,6,7 ,[23,456,67,8,78,78],[345,56,87,8,98,9],(234,657,6),{"key1":"himu",234:[23,45,657]}])
print(ext_l)


