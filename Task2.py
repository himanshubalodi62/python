import logging
logging.basicConfig(
    filename="list1.log",
    level= logging.INFO,
    format='%(levelname)s %(asctime)s %(message)s')


class list_task:
    def __init__(self,list_x):
        self.list_x = list_x

    def extract_list(self):
        logging.info("I am trying to extract list ")
        try:
            output = []
            for value in self.list_x:
                if type(value)== list:
                    output.append(value)
                    logging.info(f"the extracted list is {output}")
            return output
        except Exception as e:
            logging.exception(e)

    def extract_tuple(self):
        logging.info("I am trying to extract tuple ")
        try:
            output = []
            for value in self.list_x:
                if type(value)== tuple:
                    output.append(value)
                    logging.info(f"The extracted tuple is {output}")
            return output
        except Exception as e:
            logging.exception(e)

    def extract_dict(self):
        logging.info("I am trying to dict ")
        try:
            output = []
            for value in self.list_x:
                if type(value)== dict:
                    output.append(value)
                    logging.info(f"The extracted dict is {output}")
            return output
        except Exception as e:
            logging.exception(e)

    def extract_alphanum(self):
        logging.info("I am trying to extract numeric alphanum value")
        try:
            l1 = []
            for i in self.list_x:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                            if type(i) == dict:
                                for k in i.items():
                                    for g in k:
                                        if type(g) == int:
                                            l1.append(g)
            logging.info(f"The extracted alphanum is {l1}")
            return l1
        except Exception as e:
            logging.exception(e)

    def extract_odd(self):
        logging.info("I am trying to extract odd value ")
        try:
            l1 = []
            for i in self.list_x:
                if type(i) == tuple or type(i) == list or type(i) == dict or type(i) == (set):
                    for j in i:
                        if type(j)== int:
                            l1.append(i)
                            if j % 2 == 0:
                                pass
                            else:
                                print(j)
            logging.info(f"The extracted odd value is {l1}")
            return l1
        except Exception as e:
            logging.exception(e)

    def extract_ineuron(self):
        logging.info("I am trying to extract ineuron this list")
        try:
            l1 = []
            for i in self.list_x:
                if type(i) == tuple or type(i) == list or type(i)== set:
                    for j in i :
                        if j == "ineuron":
                            l1.append(j)
                if type(i)== dict:
                    for k in i.items():
                        for g in k:
                            if g == "ineuron":
                                l1.append(g)
            logging.info(f"The extract str is {l1}")
            return l1
        except Exception as e:
            logging.exception(e)


    def extract_data(self):
       logging.info("I am trying to how many num of occurrence of data")
       try:
           l1 = []
           for i in self.list_x:
               if type(i) == list or type(i) == tuple or type(i) == set:
                   for j in i:
                       if type(j) == int or type(j) == str:
                           l1.append(j)
               if type(i) == dict:
                   for k in i.items():
                       for g in k:
                           if type(g) == int or type(g) == str:
                                l1.append(g)
           logging.info(f"occurrence of data is {l1}")
           return l1
       except Exception as e:
           logging.exception(e)

    def multiplication(self):
        logging.info("I am trying to multiplication of all the numeric data")
        try:
            for i in self.list_x:
                m = 1
                if type(i) == tuple or type(i) ==list or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            m *= j
                    print("Multiplication of ",type(i),'is',m)
                if type(i) == dict:
                    for k,v in i.items():
                        if type(k)== int and type(v)== int:
                            m = m * k
                            m = m * v
                    print("Multiplication of",type(i),'is',m)
            logging.info(f"Multiplication of the data is {m}")
            return m
        except Exception as e:
            logging.exception(e)




list_1 = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 5]),
         {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]

e_list = list_task(list_1)
lists = e_list.extract_list()
print(lists)
y_tuple = list_task(list_1)
tuples = y_tuple.extract_tuple()
print(tuples)
a_dict = list_task(list_1)
dicts = a_dict.extract_dict()
print(dicts)
m_alphanum = list_task(list_1)
alphanums = m_alphanum.extract_alphanum()
print(alphanums)
o_odd = list_task(list_1)
odd_value = o_odd.extract_odd()
print(odd_value)
n_ineuron = list_task(list_1)
ineurons = n_ineuron.extract_ineuron()
print(ineurons)
r_occurence = list_task(list_1)
ocurences = r_occurence.extract_data()
print(ocurences)
q_multi = list_task(list_1)
multiplications = q_multi.multiplication()
print(multiplications)
