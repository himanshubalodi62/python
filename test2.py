import logging
logging.basicConfig(filename="list1.log",level=logging.DEBUG,format='%(asctime)s, %(levelname)s, %(name)s, %(message)s')

l = [3,4,5,6,7 ,[23,456,67,8,78,78],[345,56,87,8,98,9],(234,657,6),{"key1":"himu",234:[23,45,657]}]
try:
    print(l[::-1])
    logging.info("reverse the entire list")
    logging.info("successfully reverse the list")
except Exception as e:
    logging.exception(e)
