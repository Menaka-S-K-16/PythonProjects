from flask import Flask,render_template,request
import numpy as np
import pickle
import os
import smtplib
from email.message import EmailMessage
import mysql.connector

app=Flask(__name__)
pic_folder=os.path.join('static')
app.config["UPLOAD_FOLDER"]=pic_folder
recruiter_icon=os.path.join(app.config["UPLOAD_FOLDER"],"announcement.png")
candidate_icon=os.path.join(app.config["UPLOAD_FOLDER"],"resume-and-cv.png")
slide1=os.path.join(app.config["UPLOAD_FOLDER"],"img_job7.jpg")
slide2=os.path.join(app.config["UPLOAD_FOLDER"],"img_job6.png")
slide3=os.path.join(app.config["UPLOAD_FOLDER"],"img_job9.png")
nomatch=os.path.join(app.config["UPLOAD_FOLDER"],"no_match.gif")
ribbon=os.path.join(app.config["UPLOAD_FOLDER"],"rib_new.gif")
checked=os.path.join(app.config["UPLOAD_FOLDER"],"checked.png")
undrw_1=os.path.join(app.config["UPLOAD_FOLDER"],"undraw_One.png")
undrw_2=os.path.join(app.config["UPLOAD_FOLDER"],"undraw_two.png")
undrw_3=os.path.join(app.config["UPLOAD_FOLDER"],"undraw_three.png")
undrw_4=os.path.join(app.config["UPLOAD_FOLDER"],"undraw_four.png")
bg=os.path.join(app.config["UPLOAD_FOLDER"],"newbg.jpg")
#csvfile=os.path.join(app.config["UPLOAD_FOLDER"],"demoquery.csv")
model2=pickle.load(open('rfc_file_final.pkl','rb'))

@app.route('/')
def index():
   return render_template('home_tab.html',name="index",bgimg=bg)

@app.route('/auth_rec',methods=['GET','POST'])
def auth_rec():
   #to authenticate
   err_txt=""
   try:
      mylogindb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="recruiterrecommend")
      mycursor_login=mylogindb.cursor()
      email_txt=request.form.get('rec_loginmail')
      pwd_txt=request.form.get('rec_pwd')
      mycursor_login.execute("insert into loginpage values(%s,%s)",(email_txt,pwd_txt))
      #db connection to include new users for recommendation to the recruiters
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="recruiterrecommend")
      mycursor=mydb.cursor()
      mycursor.execute("select * from samplerec")
      mylist=[]
      mylist2_frontend=[]
      mylist2_backend=[]
      mylist2_mobile=[]
      mylist2_fullstack=[]
      mylist2_datascientist=[]
      for i in mycursor:
         mylist.append(i)
      #for a in range(len(mylist)):
      #  count=0
      # for ele in mylist[a]:
         # if ele=='0':
               #   count+=1
         #for c in range(count):
         # mylist[a].remove('0')
      for k in range(len(mylist)):
         list_person_detail=[]
         recommender_name=mylist[k][0]
         recommender_mail=mylist[k][1]
         recommender_url=mylist[k][2]
         recommender_skill=mylist[k][3]
         recommender_position=mylist[k][4]
         list_person_detail="Name : "+"  "+recommender_name+"%"+"  "+"Mail ID : "+"  "+recommender_mail+"%"+"  "+"Profile URL : "+recommender_url+"%"+"  "+"Skills : "+recommender_skill,"%"+"  "+"Position : "+recommender_position+"="+"^"
         if("Frontend Developer" in recommender_position):
            mylist2_frontend.append(list_person_detail)
         if("Backend Developer" in recommender_position):
            mylist2_backend.append(list_person_detail)
         if("Mobile App Developer" in recommender_position):
            mylist2_mobile.append(list_person_detail)
         if("Data Scientist" in recommender_position):
            mylist2_datascientist.append(list_person_detail)
         if("Full  stack Developer" in recommender_position):
            mylist2_fullstack.append(list_person_detail)
         
   except Exception:
      err_txt="Authentication Failed"
      return render_template("home_tab.html",error_txt=err_txt)
   finally:
      mylogindb.commit()
      mylogindb.close()
   return render_template('home_recruiter.html',slide_1=undrw_1,slide_2=undrw_2,slide_4=undrw_4,slide_3=undrw_3,r_mail=recommender_mail,r_skill=recommender_skill,r_position=recommender_position,list_recommend_frontend=mylist2_frontend,list_recommend_backend=mylist2_backend,list_recommend_fullstack=mylist2_fullstack,list_recommend_datascientist=mylist2_datascientist,list_recommend_mobile=mylist2_mobile)

@app.route('/indextemp',methods=['GET','POST'])
def indextemp():
   
   return render_template('home_tab.html',name="indextemp")

@app.route('/homerec',methods=["GET","POST"])
def homerec():
   
   #db connection to include new users for recommendation to the recruiters
   mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="recruiterrecommend")
   mycursor=mydb.cursor()
   mycursor.execute("select * from samplerec")
   mylist=[]
   mylist2_frontend=[]
   mylist2_backend=[]
   mylist2_mobile=[]
   mylist2_fullstack=[]
   mylist2_datascientist=[]
   for i in mycursor:
      mylist.append(list(i))
   #for a in range(len(mylist)):
    #  count=0
     # for ele in mylist[a]:
        # if ele=='0':
            #   count+=1
      #for c in range(count):
        # mylist[a].remove('0')
   for k in range(len(mylist)):
      list_person_detail=[]
      recommender_name=mylist[k][0]
      recommender_mail=mylist[k][1]
      recommender_url=mylist[k][2]
      recommender_skill=mylist[k][3]
      recommender_position=mylist[k][4]
      list_person_detail=[" Name : ",recommender_name,"%","Mail ID : ",recommender_mail,"%","Profile URL : ",recommender_url,"%","Skills : ",recommender_skill,"%","Position : ",recommender_position,"=","^"]
      if("Frontend Developer" in recommender_position):
           mylist2_frontend.append(list_person_detail)
      if("Backend Developer" in recommender_position):
           mylist2_backend.append(list_person_detail)
      if("Mobile App Developer" in recommender_position):
           mylist2_mobile.append(list_person_detail)
      if("Data Scientist" in recommender_position):
         mylist2_datascientist.append(list_person_detail)
      if("Full  stack Developer" in recommender_position):
         mylist2_fullstack.append(list_person_detail)
      
   return render_template('home_recruiter.html',name="homerec",slide_1=undrw_1,slide_2=undrw_2,slide_4=undrw_4,slide_3=undrw_3,r_url=recommender_url,r_mail=recommender_mail,r_skill=recommender_skill,r_position=recommender_position,list_recommend_frontend=mylist2_frontend,list_recommend_backend=mylist2_backend,list_recommend_fullstack=mylist2_fullstack,list_recommend_datascientist=mylist2_datascientist,list_recommend_mobile=mylist2_mobile)
@app.route('/homecand',methods=['POST'])
def homecand():
   try:
    err_ctxt=""
    email_ctxt=request.form.get('candidatemail')
    pwd_ctxt=request.form.get('candidatepassword')
    mydb_cand=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="recruiterrecommend")
    mycursor_cand=mydb_cand.cursor()
    mycursor_cand.execute("Insert into loginpage values(%s,%s)",(email_ctxt,pwd_ctxt))
    
   except Exception:
      err_ctxt="Authentication Failed"
      return render_template("home_tab.html",errorcmsg=err_ctxt)
   finally:
      mydb_cand.commit()
      mydb_cand.close()
   return render_template('homecand.html',name="homecand",checkimg=checked,ribbonimg=ribbon,nomatchimg=nomatch,slide_1=undrw_1,slide_2=undrw_2,slide_3=undrw_3,slide_4=undrw_4)

@app.route('/signup',methods=['GET','POST'])
def signup():
   return render_template('sign_up.html',name="signup")
@app.route('/sign_up',methods=['POST'])
def sign_up():
   err=""
   try:
      mydb_signup=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="recruiterrecommend")
      mycursor_signup=mydb_signup.cursor()
      sgn_name=request.form.get('username')
      sgn_email=request.form.get('email')
      sgn_pwd=request.form.get('pwd')  
      mycursor_signup.execute("Insert into login values(%s,%s,%s)",(sgn_name,sgn_email,sgn_pwd))
      err="Registered Successfully"
   except Exception:
      err="Please,Login You Are Already Registered"
   finally:
      mydb_signup.commit()
     
   return render_template("sign_up.html",name="sign_up",errmsg=err)
@app.route('/signuppwd')
def signuppwd():
   return render_template('forgot_pwd.html',name="signuppwd")


@app.route('/mail',methods=['GET','POST'])
def mail():
   
   return render_template("mail.html",name="mail")

@app.route('/mail_send',methods=['GET','POST'])
def mail_send():
   EMAIL_ADDRESS=request.form.get('sendmailfrom')
   EMAIL_PASSWORD=request.form.get('mailpw')
   msg=EmailMessage()
   msg['Subject']=request.form.get('subject')
   msg['From']=EMAIL_ADDRESS
   msg['To']=request.form.get('sendmailto')
   msg.set_content(request.form.get('mailcnt'))
  
   with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg) 
   return render_template("mail.html",name="mail")
@app.route('/predicts',methods=['POST'])
def predictt():
    prediction=""
    html_var=0
    css_var=0
    js_var=0
    php_var=0
    django_var=0
    flask_var=0
    wordpress_var=0
    adobe_var=0
    bootstrap_var=0
    angular_var=0       
    vue_var=0
    asp_var=0
    java_var=0
    sql_var=0
    oracle_var=0
    sqlite_var=0
    node_var=0
    mysql_var=0
    ms_var=0
    nosql_var=0
    rdbms_var=0
    mongo_var=0
    postgersql_var=0
    swift_var=0
    kotlin_var=0
    golang_var=0
    C_var=0
    Cpp_var=0
    scala_var=0
    android_var=0
    ios_var=0
    xml_var=0
    python_var=0
    datamining_var=0
    R_var=0
    dockerr_var=0
    azure_var=0
    cloudera_var=0
    dataexp_var=0
    matlab_var=0
    dataprep_var=0
    machine_learning_var=0
    deep_var=0
    text=""
    if request.method=='POST': #form is submmited
           
            list_skills=[]
            list_skills.append(request.form.getlist('skillset'))
            

            for i in list_skills:
                if "HTML" in i:
                   html_var+=1
                if "CSS" in i:
                   css_var+=1
                if "JavaScript" in i:
                   js_var+=1
                if "PHP" in i:
                   php_var+=1
                if "Django" in i:
                   django_var+=1
                if "Flask" in i:
                   flask_var+=1
                if "Word Press" in i:
                   wordpress_var+=1
                if "Adobe Photoshop" in i:
                   adobe_var+=1
                if "BootStrap" in i:
                  bootstrap_var+=1
                if "Angular Js" in i:
                   angular_var+=1
                if "Vue Js" in i:
                   vue_var+=1
                if "ASP.NET" in i:
                   asp_var+=1
                if "Java" in i:
                   java_var+=1
                if "SQL" in i:
                   sql_var+=1
                if "Oracle" in i:
                   oracle_var+=1
                if "SQLite" in i:
                   sqlite_var+=1
                if "Node Js" in i:
                   node_var+=1
                if "My SQL" in i:
                   mysql_var+=1
                if "MS Access" in i:
                   ms_var+=1
                if "No SQL" in i:
                   nosql_var+=1
                if "RDBMS" in i:
                   rdbms_var+=1
                if "Mongo DB" in i:
                   mongo_var+=1
                if "PostgerSQL" in i:
                   postgersql_var+=1
                if "Swift" in i:
                   swift_var+=1
                if "Kotlin" in i:
                  kotlin_var+=1
                if "GoLang" in i:
                   golang_var+=1
                if "C" in i:
                    C_var+=1
                if "C++" in i:
                   Cpp_var+=1
                if "Scala" in i:
                   scala_var+=1
                if "Android" in i:
                   android_var+=1
                if "IOS" in i:
                   ios_var+=1
                if "XML" in i:
                   xml_var+=1
                if "Python" in i:
                   python_var+=1
                if "Docker" in i:
                   dockerr_var+=1
                if "Azure" in i:
                  azure_var+=1
                if "Data Mining" in i:
                   datamining_var+=1
                if "R" in i:
                   R_var+=1
                if "Cloudera" in i:
                   cloudera_var+=1
                if "Data Exploration" in i:
                   dataexp_var+=1
                if "MATLAB" in i:
                   matlab_var+=1
                if "Data PreProcessing" in i:
                   dataprep_var+=1
                if "Machine Learning" in i:
                   machine_learning_var+=1
                if "Deep Learning" in i:
                   deep_var+=1
                #check=[html_var,css_var,js_var,php_var,django_var,flask_var,wordpress_var,adobe_var,bootstrap_var,angular_var,vue_var,asp_var,java_var,sql_var,oracle_var,sql_var,node_var,mysql_var,ms_var,nosql_var,rdbms_var,mongo_var,postgersql_var,swift_var,kotlin_var,golang_var,C_var,Cpp_var,scala_var,android_var,ios_var,xml_var,python_var,dockerr_var,azure_var,datamining_var,R_var,cloudera_var,dataexp_var,matlab_var,dataprep_var,machine_learning_var,deep_var]
                samp=np.array([html_var,css_var,js_var,php_var,django_var,flask_var,wordpress_var,adobe_var,bootstrap_var,angular_var,vue_var,asp_var,java_var,sql_var,oracle_var,sql_var,node_var,mysql_var,ms_var,nosql_var,rdbms_var,mongo_var,postgersql_var,swift_var,kotlin_var,golang_var,C_var,Cpp_var,scala_var,android_var,ios_var,xml_var,python_var,dockerr_var,azure_var,datamining_var,R_var,cloudera_var,dataexp_var,matlab_var,dataprep_var,machine_learning_var,deep_var])
                #samp=np.array([1,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,1,0,1,1])
                prediction=model2.predict(samp.reshape(1,-1))
                try:
                  error_candidatefilled=""
                  form_name=request.form.get('usr_name')
                  form_url=request.form.get('usr_url')
                  form_mailid=request.form.get('usr_mail')
                  form_pos=prediction
                  mydb1=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="recruiterrecommend")
                  mycur=mydb1.cursor()
                  mycur.execute("Insert into samplerec values(%s,%s,%s,%s,%s)",(form_name,form_mailid,form_url,str(list_skills),str(form_pos)))
                except Exception:
                   error_candidatefilled="You Already Filled The Resume"
                finally:
                   mydb1.commit()
                   mydb1.close()
                return render_template('homecand.html',name="homecand",prediction_text=prediction,error_candidate_already_filled=error_candidatefilled,rec_icon=recruiter_icon,ca_icon=candidate_icon,checkimg=checked,ribbonimg=ribbon,nomatchimg=nomatch,slide_1=undrw_1,slide_2=undrw_2,slide_3=undrw_3,slide_4=undrw_4)

    else:
        return render_template('home_tab.html',name="home",rec_icon=recruiter_icon,ca_icon=candidate_icon,slide_1=slide1,slide_2=slide2,slide_3=slide3)


        
           
            
