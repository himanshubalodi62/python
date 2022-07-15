import logging

class logrec :

    def __init__(self,filename,level,format):
        self.filename = filename
        self.level = level
        self.format = format
        logging.basicConfig(filename=self.filename,level=level,format=self.format)

    def log(self,message,method):
        '''logging the message based on the method passed inthe function in the file'''

        if method == "INFO":
            logging.info(message)
        else:
            logging.error(message)



    def student_total(self):
        '''this method is used in id of the student '''
        try:
            self.logger_list.log("total count of the student", "INFO")
            return self.student_count
        except Exception as e:
            self.logger_list.log("Exception counted of the student", "ERROR")

class oneNeuron:

    def __init__(self,neuron_cost,neuron_type):
        self.neuron_cost = neuron_cost
        self.neuron_type = neuron_type
        self.student_count = 10000
        self.logger_list = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_oneNeuron = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')

    def neuron_register(self):
        '''this method is used to createn the type of neuron on one neuron'''
        try :
            self.logger_oneNeuron.log("build new version neuron plateform","INFO")
            message = "new neuron is builded"
            self.logger_oneNeuron.log("Neuron is created","INFO")
            return message

        except Exception as e :
            self.logger_oneNeuron.log("building Neuron failed","ERROR")

    def neuron_costing(self,neuron_type):
        '''this method is return neuron cost type '''

        try :
            self.logger_oneNeuron.log("cost affordable started for a neuron","INFO")
            cost = self.neuron_cost
            self.logger_oneNeuron.log("cost of neuron is returned","INFO")
            return cost

        except Exception as e :
            self.logger_oneNeuron.log("Exception calculating cost","ERROR")

# create objects:

o = oneNeuron(4500,"new_type")
#print(o.student_welcome())
#print("Total student counts are ",o.student_total())
print(o.neuron_register())
print("cost of tech neuron is ",o.neuron_costing("tech"))

class techNeuron :

    def __init__(self):
        self.logger_techNeuron = logrec('log_file,txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
    def course_list(self,instructor_name):
        '''this method return is the list of the course for a particular instructor'''

        try :
            self.logger_techNeuron.log("build list of course for an instructor","INFO")
            opt_list = ["Python","Java","c++","Javascript",]
            self.logger_techNeuron.log("course list created and returned","INFO")
            return opt_list
        except Exception as e :
            self.logger_techNeuron.log("creating course list encountered mistake","ERROR")

    def course_cost(self,course_name):
        '''this method is used to return the cost of course '''

        try :
            self.logger_techNeuron.log("cost started foa a course","INFO")
            cost = 17700
            self.logger_techNeuron.log("cost of course is reeturned","INFO")
            return cost

        except Exception as e :
            self.logger_techNeuron.log("Exception calculating cost of course","ERROR")

class instructor(techNeuron) :

    def __init__(self,instructor_name,instructor_age,instructor_skills):
        self.instructor_name = instructor_name
        self.instructor_age = instructor_age
        self.instructor_skills = instructor_skills
        self.logger_techNeuron = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_instructor = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')

    def instructor_registration(self):
        '''this method is used to register the instructor in neuron '''

        try :
            self.logger_instructor.log("starting registration of an instructor","INFO")
            result = "succesfully you registered in an instructor "
            self.logger_instructor.log("Instructor registration done","INFO")
            return result
        except Exception as e :
            self.logger_instructor.log("Instructor encountered mistake","ERROR")
ins = instructor("Alok",35,"SQL,PHP,C#")
print("course list Instructor Nitin teaches are ",ins.course_list("Nitin"))
print("cost of the Datascience course in tech neuron is ",ins.course_list("data science"))
print(ins.instructor_registration())

class course :
    def __init__(self,main_course_name,sub_course_name):
        self.main_course_name = main_course_name
        self.sub_course_name = sub_course_name
        self.logger_courses = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')

    def new_course_creation(self):
        '''this method is used to create a new sub course in main course in ineuron plateform'''

        try:
            self.logger_courses.log("sub course registration is done","INFO")
            result = "New course is registered"
            self.logger_courses.log("sub course is done","INFO")
            return result
        except Exception as e :
            self.logger_courses.log("course registration is failed","ERROR")

    def sub_course_count(self,main_course_name):
        '''this method is return the count of sub courses in main course in ineuron plateform'''

        try :
            self.logger_courses.log("starting counting of sub courses","INFO")
            count = 12
            self.logger_courses.log("sub course counted is done","INFO")
            return count

        except Exception as e :
            self.logger_courses.log("sub course counting is failed","ERROR")
    def sub_course_deletion(self,sub_course_name):
        '''this method is used to delete a new sub course in main course in ineuron plateform'''

        try :
            self.logger_courses.log("starting a deletion of a new course","INFO")
            count = 10
            self.logger_courses.log("deleted is completed","INFO")
            return count

        except Exception as e :
            self.logger_courses.log("deletion is failled ","ERROR")

class student(course) :
    def __init__(self,student_name,student_emailid,student_mub,student_password,main_course_name,sub_course_name):
        super().__init__(main_course_name,sub_course_name)
        self.student_name = student_name
        self.student_emailid = student_emailid
        self.student_mub = student_mub
        self.student_password = student_password
        self.logger_courses = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_student = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')

    def student_registration(self):
        '''this method is used to register a new student in ineuron plateform'''

        try:
            self.logger_student.log("registrating a new student", "INFO")
            bool = False
            if not bool:
                result = "student is registered "
            else:
                result = "student is already present"
            self.logger_student.log("student registration is completed", "INFO")
            return result

        except Exception as e:
            self.logger_student.log("student registration is failed", "ERROR")

    def student_emailid_update(self, emailid, student_name):
        '''this method is update of the  emailid of student in ineuron plateform'''

        try:
            self.logger_student.log("updating the emailid of the student", "INFO")
            if student_name:
                self.emailid = emailid
                result = "emailid is updated"
            else:
                result = "student is absent"
            self.logger_student.log("emailid updation is done", "INFO")
            return result
        except Exception as e:
            self.logger_student.log("emailid updation is failed", "ERROR")

s = student("Kartik",7055876391,"Kartik@gmail.com","23424","Data science","Python programming")
print(s.new_course_creation())
print("now total sub course under data science are",s.sub_course_count("data science"))
print("After deleting,total sub course under data science are",s.sub_course_deletion("data analytics"))
print(s.student_registration())
print("yeh kartik your",s.student_emailid_update(99900000000,"kartik"))

class blog :
    def __init__(self):
        self.logger_blog = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')

    def blog_creation(self,blog_type,blog_title,blog_content):
        '''this method is store blog database'''

        try :
            self.logger_blog.log("creation the blog","INFO")
            blog_id = 11
            self.logger_blog.log("blog is stored ","INFO")
            return blog_id
        except Exception as e :
            self.logger_blog.log("blog regestration failed","ERROR")

    def blog_types(self):
        '''this method is used return different types of blog in database'''

        try:
            self.logger_blog.log("fetching the blog types","INFO")
            opt_dabase = ['Data science','Big data','Blockchain']
            self.logger_blog.log("blog types list is done","INFO")
            return opt_dabase
        except Exception as e :
            self.logger_blog.log("fetching time the blog is failed","ERROR")
class affilliate(instructor):
    def __init__(self,instructor_name,instructor_age,instructor_skills):
        super().__init__(instructor_name,instructor_age,instructor_skills)
        self.logger_affiliate = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_instructor = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')

    def bank_update(self, bank_name, account_number, change_barcode, pancard):
        '''this method is uesd update the bank details become the affilate member  in ineuron'''

        try:
            self.logger_affiliate.log("updating the bank details", "INFO")
            Update = [bank_name, account_number, change_barcode, pancard]
            message = "bank updated"
            self.logger_affiliate.log("bank updated is succesfully", "INFO")
            return message
        except Exception as e:
            self.logger_affiliate.log("updation is not completed", "ERROR")

    def create_affiliate_eligible(self, name):
        '''this method is used to check affiliate can be created in ineuron '''

        try:
            self.logger_affiliate.log("starting the affiliate process", "INFO")
            if False:
                message = "Yes"
            else:
                message = "No"
            self.logger_affiliate.log("Affiliation verified ", "INFO")
            return message

        except Exception as e:
            self.logger_affiliate.log("affiliate checking time is failed", "ERROR")

afl1 = affilliate("Alok",35,"SQL,PHP,C#")
print(ins.instructor_registration())
print("kartik is eligible for affiliation",afl1.create_affiliate_eligible("kartik"))
print("affiliation is ready for kartik as ",afl1.bank_update(35345,"kartik","PNB34242","uytrewq"))

class jobs :
    def __init__(self):
        self.logger_jobs = logrec('log_file.txt','INFO','%(levelname) %(asctime)s %(level) %(message)s')

    def jobs_search(self,job_type):
        '''this method is used to seach the job type'''
        try :
            self.logger_jobs.log("starting to searhing for job","INFO")
            if job_type == 'Contract' :
                opt = ['Data science at amzone','data anaylyst at sumsung ']
            elif job_type == 'Full time':
                opt = 'Full time'
            else :
                opt = 'Part time'
            self.logger_jobs.log("list genrated for given job type","INFO")
            return opt
        except Exception as e :
            self.logger_jobs.log("try again ! not find the job list","ERROR")

class contact :
    def __init__(self):
        self.logger_contact = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')

    def create_query(self,name,emailid,mob,message,type):
        ''''this method is used to crate the query for ineuron '''

        try :
            self.logger_contact.log("stor the query","INFO")
            query = [name,emailid,mob,message,type]
            opt = 'Query created'
            self.logger_contact.log("Query created","INFO")
            return opt
        except Exception as e :
            self.logger_contact.log("query creating time mistake","ERROR")

class library :
    def __init__(self):
        self.logger_lib = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')

    def lib_course(self):
        '''this method is used to return the course present in library'''

        try :
            self.logger_lib.log("fetching the courses the from library","INFO")

            opt = ['SQL commmunity class',"Javascript merathon"]

            self.logger_lib.log("list generated for courses ","INFO")
            return opt
        except Exception as e :
            self.logger_lib.log("please try again!,not able to get the list","ERROR")

class lib_neuron(library):
    def __init__(self):
        self.student_count = 10000
        self.logger_jobs = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_lib = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')

class blog_jobs(blog,jobs):
    def __init__(self):
        self.logger_jobs = logrec('log_file.txt',"INFO",'%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_blog = logrec('log_file.txt',"INFO",'%(levelname)s %(asctime)s %(name)s %(message)s')


    def test12(self):
        self.blog_creation('data anayltics','data analytics','quite essay')


class language :
    def __init__(self):
        self.logger_lang = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
    def language_types(self):
        '''this method is used return the language of course'''

        try :
            self.logger_lang.log("returning the courses language","INFO")
            opt = ['English',"Hindi"]
            self.logger_lang.log("created the list of language","INFO")
            return  opt

        except Exception as e :
            self.logger_lang.log("mistake during check language","ERROR")

    def add_language(self,lang):
        ''''this method is add the new language course'''
        try :
            self.logger_lang.log("building the course languages","INFO")
            opt = ["spanish"]
            self.logger_lang.log("new language is created","INFO")
            return "language created"

        except Exception as e :
            self.logger_lang.log("mistake during check new language","ERROR")

class lang_neuron(language,techNeuron):
    def __init__(self):
        self.logger_lang = logrec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_lang = logrec('log_file.txt','info','%(levelname)s %(asctime)s %(name)s %(message)s')

    def new_method(self):
        '''this method is used to verify the tech neuron course language'''

        try :
            self.logger_lang.log("verifyin the tech neuron language","INFO")
            opt = self.language_types()
            op1 = self.course_list("Alok")
            self.logger_lang.log("language verified","INFO")
            return "language are verified"

        except Exception as e :
            self.logger_lang.log("mistake during verified ","ERROR")

ln = lang_neuron()
print(ln.new_method())

#ln = lib_neuron()
#print(ln.student_welcome())

blg = blog()
print("blog created with id as ",blg.blog_creation('data science','welcome to data science','its very essay'))
print("decent blog types are ",blg.blog_types())

jbs = jobs()

print("contract jobs are ",jbs.jobs_search("contract"))


cnt = contact()
print(cnt.create_query("kartik","kartik@gmail.com","99000000000","ok when i can join course","course enquiry"))


