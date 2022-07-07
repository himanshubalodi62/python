import logging

logging.basicConfig(filename="tuple.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(name)s %(message)s')

class tuple_s:
    logging.info("open the tuple class")

    def __init__(self,l):
        self.l = l

    def extract_tuple(self):
        """ To extract tuple from a collection"""
        logging.info("extract_tuple")
        try:
            for i in self.l :
                if type(i) == tuple:
                    logging.info(i)
                    print(i)
        except Exception as e :
            logging.error(e)
l = [[1,2,3,4], (2,3,4,5,6),(3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),
     {'k1':"sudh", 'k2':"ineuron", 'k3':"kumar", 3:6,7:8}]
tup_var = tuple_s(l)
tup_var.extract_tuple()



