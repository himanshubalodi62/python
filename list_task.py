import  logging
logging.basicConfig(filename="test_list.log",level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')

class list_task :
    logging.info("log for list class")
#reverse list
    def extract_list(self,l):
        """ extract list entity from the data collection"""
        logging.info("we are in the extract_list")
        try:
            self.l = 1
            for i in self.l:
                if type(i) == list:
                    print(i)
        except Exception as e:
            logging.exception(e, "please enter itrable collection like : lists,tuples,set,dictionary")

    def extract_ineuron(self,m):
        """ extract ineuron from the string collection"""
        logging.info("extract_ineuron ")
        try:
            self.m = m
            for i in self.m :
                if type(i) != dict :
                    for j in i :
                        if j == 'ineuron':
                            logging.info(j)
                            return j
                else:
                    for j in i :
                        if i[j] == 'ineuron':
                            logging.info(i[j])
                            return  i[j]
        except Exception as e:
            logging.exception(e)


    def flat_list(self,l):
        """ To create a flat list from the data collection"""
        logging.info("flat_list")
        try:
            self.l = l
            self.p = []
            for i in l:
                if type(i) != dict:
                    logging.info("data is %s:" ,i)
                    self.p.extend(i)
                else:
                    logging.info("value inside dict is %s:",i)
                    self.p.extend(i.keys())
                    self.p.extend(i.values())
            return self.p
            logging.info("output %s:",p)
        except Exception as e:
            logging.exception(e)
            return e

    def print_prime(self):
        """   To create a list of prime number 1 to 1000"""
        logging.info("print_prime")
        try:
            self.l = []
            for i in range(1,1000):
                n = 0
                for j in range(2,i):
                    if i % j == 0:
                        n = 1
                if n != 1:
                    self.l.append(i)
            logging.info("output is %s:",self.l)
            return self.l
        except Exception as e:
            logging.exception(e)
            return e


l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
     {'k1': "sudh", 'k2': "ineuron", 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]

list_var = list_task()
print(list_var.extract_ineuron(l))
print(list_var.print_prime())






