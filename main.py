from base import words
import random, os
from flask import Flask,url_for,render_template,request

app=Flask(__name__)
app.static_folder='static'

def rand_help(word_count):
    rand_numbers=[]
    test_words=[]
    count=0
    while count<word_count:
        rand=random.randrange(len(words))
        if rand not in rand_numbers:
            rand_numbers.append(rand)
            test_words.append(words[rand])
            count+=1
    return test_words

@app.route('/')
def index():
    user=os.environ.get("USERNAME")
    return render_template('index.html',user_name=user)

@app.route('/all_tests')
def all_tests():
	return render_template('all_tests.html')

@app.route('/all_tests/test1', methods=['POST'])
def test1():
    questions = int(request.form['questionnumbers'])
    global test1_words
    ttime=questions*12
    test1_words=rand_help(questions)
    label_names=['word'+str(id) for id in range(questions)]
    return render_template('test1.html',
                           displayed_words=test1_words,
                           names=label_names,
                           test_time=ttime,
                           question_num=questions,
                           lang1='английски',
                           lang2='български')

@app.route('/all_tests/checktest', methods=['GET','POST'])
def answer1():
    
    errors=0
    if request.method=='POST':
        result=request.form
        
        for each in range(0,len(result)):
            w='word' + str(each)
            if result[w] !=test1_words[each][1]:
                errors+=1
    return render_template('answer1.html',answer=str(errors))

@app.route('/all_tests/test2', methods=['POST'])
def test2():
    questions = int(request.form['questionnumbers'])
    global test1_words
    ttime=questions*12
    test1_words=rand_help(questions)
    test1_words = [x[::-1] for x in test1_words]
    label_names=['word'+str(id) for id in range(questions)]
    return render_template('test1.html',
                           displayed_words=test1_words,
                           names=label_names,
                           test_time=ttime,
                           question_num=questions,
                           lang1='български',
                           lang2='английски')

if __name__=='__main__' :
    app.run(debug=True,host='127.0.0.1')