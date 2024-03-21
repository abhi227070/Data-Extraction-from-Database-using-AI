from flask import Flask,render_template,request,jsonify
from backend.langchain_helper import get_langchain_output

langchain_object = get_langchain_output()
    
app = Flask(__name__,template_folder="frontend/html",static_folder="frontend/css and js")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
def predict():
    
    data = request.json
    question = data.get('question')
    answer = langchain_object.run(question)
    
    try:
        sql_query = answer['intermediate_steps'][1]
        final_answer =answer['intermediate_steps'][5]
    except:
        sql_query = "Some error occour."
        final_answer = "Some error occur."

    output_data = jsonify({'sql_query': sql_query, 'answer': final_answer})
    
    return output_data

if __name__=='__main__':
    app.run(debug=True)