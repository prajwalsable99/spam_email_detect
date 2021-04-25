from flask import Flask,render_template,request
import pickle 
import joblib


model=joblib.load('final.pkl')

# x=model.predict(["money  free congrats"])
# print(x)
app=Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/predict',methods=['POST'])

def predict():
    d1=request.form['message']

    d1=str(d1)
    d1=d1.lower()
    d1.replace("\n",' ')

    if len(d1)==0:
        pred=-1
    
    else:
        inp=[d1]

        pred=model.predict(inp)
  
    #print(inp,pred)

    return render_template('result.html',data=pred)


if __name__=='__main__':
    app.run(debug=True)