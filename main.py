from flask import Flask, render_template, request, redirect, session
from db import Database
import nerAPI
import os

website = Flask(__name__)
dbo = Database()
website.secret_key = os.urandom(24)

@website.route('/')
def page_1():

    return render_template('login.html')

@website.route('/register')
def page_2():
    return render_template('register.html')

@website.route('/perform_registration', methods = ['post'])
def page_3():
    user_name = request.form.get('user_cha_naav')
    user_email = request.form.get('user_cha_email')
    user_password = request.form.get('user_cha_password')
    response = dbo.insert_info(user_name,user_email,user_password)
    if response:
        return render_template('login.html', message = 'Registration Successful. Kindly Login to proceed')
    else:
        return render_template('register.html', message = 'Email already exists')

@website.route('/perform_login', methods = ['post'])
def page_4():
    user_email = request.form.get('user_cha_email')
    user_password = request.form.get('user_cha_password')
    response = dbo.check_info(user_email, user_password)
    if response:
        session['user_id'] = os.urandom(12)
        return redirect('/profile')
    else:
        return render_template('login.html', message = 'Incorrect email and/or password')

@website.route('/profile')
def page_5():
    if 'user_id' in session:
        return render_template('profile.html')
    else:
        return redirect('/')


@website.route('/ner')
def page_6():
    if 'user_id' in session:
        return render_template('NER.html')
    else:
        return redirect('/')



@website.route('/perform_ner', methods = ['post'])
def page_7():

    the_text = request.form.get('text_for_ner')
    response = nerAPI.use_of_nerAPI(the_text)
    result = ''
    for i in response['entities']:
        result = result + i['name']+ ' : ' +i['category']+"\t"
    return render_template('NER.html', result = result)

@website.route('/sentiment_analysis')
def page_8():
    if 'user_id' in session:
        return render_template('SenAna.html')
    else:
        return redirect('/')

@website.route('/perform_SA', methods = ['post'])
def page_9():
    the_text = request.form.get('text_for_SA')
    response = nerAPI.use_of_saAPI(the_text)
    result = ''
    for i in response['sentiment']:
        result =  result + i + ': '+str(response['sentiment'][i]) + '\t'
    return render_template('SenAna.html', result = result)



if __name__ == '__main__':
    website.run(debug = True,port = 5001)