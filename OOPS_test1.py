import logging
logging.basicConfig(filename="string.log",level=logging.INFO,format='%(asctime)s %(levelname)s %(name)s %(message)s')
class string_task:



# extract string
    def string_extract(self,ext_string):
        logging.info("I extract to string index one to 300 with in jump of 3")
        self.ext_string = ext_string
        try:
            if len(ext_string) == 0:
                raise ValueError("empty string")
                logging.error("empty string")
            else:
                str = ext_string[::3]
                logging.info("extracted string is %s:" , str)
                return str
        except Exception as e:
            logging.exception(e)

# reverse string
    def string_reverse(self,rev_string):
        logging.info("create about to reverse string")
        self.rev_string  = rev_string
        try:
            if len(rev_string) == 0:
                raise ValueError("empty string")
                logging.error("empty string")
            else:
                str = rev_string[::-1]
                logging.info("reverse string is %s:",str)
                return str
        except Exception as e:
            logging.Exception(e)

#Split string
    def string_split(self,_string):
        logging.info("create about to split string")
        self._sting = _string
        try:
            if len(_string) == 0 :
                raise ValueError("empty string")
                logging.error("empty string")
            else:
                str = _string.upper()
                str1 = str.split()
                logging.info("split string is %s:",str1)
                return str1
        except Exception as e :
            logging.Exception(e)

#lower string
    def string_lower(self,_lstring):
        logging.info("we are about to lower string")
        self._sting = _lstring
        try:
            if len (_lstring) == 0 :
                raise ValueError("empty string")
                logging.error("empty string")
            else:
                str = _lstring.lower()
                logging.info("lower string is %s:",str)
                return str
        except Exception as e:
            logging.exception(e)

#captilize string
    def string_split(self,_Cstring):
        logging.info("we are about captilize string")
        self._Cstring = _Cstring
        try:
            if len (_Cstring) == 0 :
                raise ValueError("empty string")
                logging.error("empty string")
            else:
                str = _Cstring.titel()
                logging.info("Titel string is %s:",str)
                return str
        except Exception as e :
            logging.exception(e)

e_string = string_task()
output_str =e_string.string_extract("this is My First Python programming class and i am learNING python string and its function")
print(output_str)

e_string = string_task()
output_str = e_string.string_extract("")
print(output_str)

r_string = string_task()
rev_st = r_string.string_reverse("this is My First python programming class an i am python learNING python string and its function")
print(rev_st)

s_string = string_task()
split_St = s_string.string_split("this is My First Python programming class and i am learNING python string and its function")
print(split_St)










