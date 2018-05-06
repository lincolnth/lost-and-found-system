import kivy
kivy.require("1.8.0")
import re
import pymysql
from KivyCalendar import CalendarWidget
import random
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.layout import Layout
from kivy.properties import OptionProperty, VariableListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.core.window import Window
Window.clearcolor = (.2,.3,.4,.1)
# database connection
con = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     db='lostandfounduz')

if con.open:
    try:
        class MyManager(ScreenManager):
            pass

        class Homepage(Screen):
            pass

        class LogIn(Screen):
            def login_insert(self):
                username= self.ids.username.text 
                password= self.ids.password.text

            
                        
        class SignIn(Screen):

            def SignIn_insert(self):
                reg_num = self.ids.reg_num.text 
                first_name = self.ids.first_name.text 
                last_name = self.ids.last_name.text  
                email_address = self.ids.email_address.text  
                phone_number = self.ids.phone_number.text  
                password = self.ids.password.text 

                cur = con.cursor()
                insert = """INSERT INTO users(reg_num,first_name,last_name,email_address,phone_number,password)\
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(reg_num, first_name, last_name, email_address, phone_number,password)
                cur.execute(insert)
                con.commit()
        

        class IFoundPage(Screen):
            def submitFound(self):
                founder_reg = self.ids.reg_num.text
                #found_item_code =  self.found_item_code.text  
                item_category = self.ids.item_category.text  
                item_name = self.ids.item_name.text  
                item_pic =  self.ids.item_pic.text 
                date_found =  self.ids.date_found.text 

                if item_category == 'cellphone':
                    found_item_code = "CELL" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    found_item_report= """INSERT INTO found_items(reg_num,found_item_code,item_category,item_name,item_pic,date_found) \
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(founder_reg,found_item_code,item_category,item_name,item_pic,date_found)
                    cur.execute(found_item_report)
                    con.commit()


                if item_category == 'computer':
                    found_item_code = "COMP" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    found_item_report= """INSERT INTO found_items(reg_num,found_item_code,item_category,item_name,item_pic,date_found)\
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(founder_reg,found_item_code,item_category,item_name,item_pic,date_found)
                    cur.execute(found_item_report)
                    con.commit()

                if item_category == 'other gadgets':
                    found_item_code = "OTGA" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    found_item_report= """INSERT INTO found_items(reg_num,found_item_code,item_category,item_name,item_pic,date_found)\
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(founder_reg,found_item_code,item_category,item_name,item_pic,date_found)
                    cur.execute(found_item_report)
                    con.commit()

                if item_category == 'locks':
                    found_item_code = "LOCK" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    found_item_report= """INSERT INTO found_items(reg_num,found_item_code,item_category,item_name,item_pic,date_found)\
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(founder_reg,found_item_code,item_category,item_name,item_pic,date_found)
                    cur.execute(found_item_report)
                    con.commit()

                if item_category == 'bank cards':
                    found_item_code = "BACA" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    found_item_report= """INSERT INTO found_items(reg_num,found_item_code,item_category,item_name,item_pic,date_found)\
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(founder_reg,found_item_code,item_category,item_name,item_pic,date_found)
                    cur.execute(found_item_report)
                    con.commit()

                if item_category == 'id cards':
                    found_item_code = "IDCA" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    found_item_report= """INSERT INTO found_items(reg_num,found_item_code,item_category,item_name,item_pic,date_found)\
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(founder_reg,found_item_code,item_category,item_name,item_pic,date_found)
                    cur.execute(found_item_report)
                    con.commit()

                if item_category == 'stationary':
                    found_item_code = "STAT" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    found_item_report= """INSERT INTO found_items(reg_num,found_item_code,item_category,item_name,item_pic,date_found)\
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(founder_reg,found_item_code,item_category,item_name,item_pic,date_found)
                    cur.execute(found_item_report)
                    con.commit()

                if item_category == 'clothing':
                    found_item_code = "CLOT" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    found_item_report= """INSERT INTO found_items(reg_num,found_item_code,item_category,item_name,item_pic,date_found)\
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(founder_reg,found_item_code,item_category,item_name,item_pic,date_found)
                    cur.execute(found_item_report)
                    con.commit()

                    
        class Settings(Screen):
            pass
            
                  
                            
        class my_Activity(Screen):
            pass
            
        class ITDet(Screen):
            pass
        class showItems(Screen):
            pass
            
            
                
        class ILostPage(Screen):

            def submitLost(self):

                def Picker(self):
                    self.laDate = self.datepicker.text
                    self.datepicked = datetime.datetime.strptime(self.laDate, '%d.%m.%Y').strftime('%d/%m/%Y')
                    self.myLabel.text = str(self.datepicked)


                
                looser_reg =  self.ids.reg_num.text
                #lost_item_code =  self.lost_item_code.text 
                item_category = self.ids.item_category.text 
                item_name= self.ids.item_name.text 
                item_description =  self.ids.item_description.text 
                date_lost =  self.ids.date_lost.text 

                if item_category == 'cellphone':
                    lost_item_code = "CELL" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    lost_item_report = """INSERT INTO lost_items(reg_num,lost_item_code,item_category,item_name,item_description,date_lost)
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(looser_reg,lost_item_code,item_category,item_category,item_description,date_lost)
                    cur.execute(lost_item_report)
                    con.commit()


                if item_category == 'computer':
                    lost_item_code = "COMP" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    lost_item_report = """INSERT INTO lost_items(reg_num,lost_item_code,item_category,item_name,item_description,date_lost)
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(looser_reg,lost_item_code,item_category,item_category,item_description,date_lost)
                    cur.execute(lost_item_report)
                    con.commit()

                if item_category == 'other gadgets':
                    lost_item_code = "OTGA" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    lost_item_report = """INSERT INTO lost_items(reg_num,lost_item_code,item_category,item_name,item_description,date_lost)
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(looser_reg,lost_item_code,item_category,item_category,item_description,date_lost)
                    cur.execute(lost_item_report)
                    con.commit()

                if item_category == 'locks':
                    lost_item_code = "LOCK" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    lost_item_report = """INSERT INTO lost_items(reg_num,lost_item_code,item_category,item_name,item_description,date_lost)
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(looser_reg,lost_item_code,item_category,item_category,item_description,date_lost)
                    cur.execute(lost_item_report)
                    con.commit()

                if item_category == 'bank cards':
                    lost_item_code = "BACA" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    lost_item_report = """INSERT INTO lost_items(reg_num,lost_item_code,item_category,item_name,item_description,date_lost)
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(looser_reg,lost_item_code,item_category,item_category,item_description,date_lost)
                    cur.execute(lost_item_report)
                    con.commit()

                if item_category == 'id cards':
                    lost_item_code = "IDCA" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    lost_item_report = """INSERT INTO lost_items(reg_num,lost_item_code,item_category,item_name,item_description,date_lost)
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(looser_reg,lost_item_code,item_category,item_category,item_description,date_lost)
                    cur.execute(lost_item_report)
                    con.commit()

                if item_category == 'stationary':
                    lost_item_code = "STAT" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    lost_item_report = """INSERT INTO lost_items(reg_num,lost_item_code,item_category,item_name,item_description,date_lost)
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(looser_reg,lost_item_code,item_category,item_category,item_description,date_lost)
                    cur.execute(lost_item_report)
                    con.commit()

                if item_category == 'clothing':
                    lost_item_code = "CLOT" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    lost_item_report = """INSERT INTO lost_items(reg_num,lost_item_code,item_category,item_name,item_description,date_lost)
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(looser_reg,lost_item_code,item_category,item_category,item_description,date_lost)
                    cur.execute(lost_item_report)
                    con.commit()

                if item_category == 'other':
                    lost_item_code = "OTHE" + str(random.randint(1000,9999))

                    cur = con.cursor()
                    lost_item_report = """INSERT INTO lost_items(reg_num,lost_item_code,item_category,item_name,item_description,date_lost)
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(looser_reg,lost_item_code,item_category,item_category,item_description,date_lost)
                    cur.execute(lost_item_report)
                    con.commit()

      


        class MatchingItems(Screen):
            pass
        class Matchfinder(Screen):

            def itemTracker(self):
                item_code = self.ids.item_code.text
                if len(item_code) == 8:
                    try:

                        item_details = """SELECT reg_num,item_category,item_name, date_lost FROM lost_items WHERE lost_item_code = '{}' """.format(item_code)
                        cur = con.cursor()
                        cur.execute(item_details)
                        con.commit

                        for (reg_num, item_category, item_name , date_lost) in cursor:
                            print("{}, {} was hired on {}".format(
                            reg_num, item_category, item_name , date_lost))
                    except:
                        pass

                        

        class LandFApp(App):

            def build(self):
                return MyManager()
    except:
        pass
else:
    con.close()
    
if __name__=="__main__":
    LandFApp().run()