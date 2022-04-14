"""
files saved in the 'data.json' is as follows:
1st line is a user info dic
2nd line is a questions list
3rd line is a answers list
"""
import json
class Survey():
    """A survey maker"""

    def __init__(self,name,user_info=[],questions=[],responses=[],results=[]):
        self.name = name
        self.user_info = {}
        self.questions = []
        self.responses = []

    def collect_user_info(self):
        """Collects user info"""
        switch_1 = True
        while switch_1:
            f_name = input("What's your first name ?\n\t-")
            l_name = input("What's your last name ?\n\t-")
            age = input("How old are you ?\n\t-")
            gender = input("What gender do you identify as ?\n\t-")
            self.user_info["f_name"] = f_name
            self.user_info["l_name"] = l_name
            self.user_info["age"] = age
            self.user_info["gender"] = gender
            with open("user_data.json","w") as target:
                json.dump(self.user_info, target)
            switch_1 = False

    def add_questions(self,qn):
        qn = int(qn) + 1
        print("Start Adding Questions Now.")
        for number in range(1,int(qn)):
            question = input("-")
            self.questions.append(question)
        with open("questions.json","w") as file_obj:
            file_obj.write("\n")
            json.dump(self.questions, file_obj)

    def show_questions(self):
        for q in self.questions:
            print("-" + q)

    def start_survey(self):
        with open("user_data.json") as user_data_file:
            ud_dic = json.load(user_data_file)

    def save_results(self):
        with open("data.json","a") as f_obj:
            f_obj.write("\n")
            json.dump(self.responses, f_obj)
