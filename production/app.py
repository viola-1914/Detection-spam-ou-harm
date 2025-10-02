from flask import Flask, render_template, request
import pickle

model = None
filename = "models/mail_spam_model_live.sav"

service = Flask("""Spam prediction""")

@service.route("/")
def render_default():
    return render_template("index.html", pred="")


@service.route("/api/predict", methods=["POST"])
def predict():
    # "GET", 
    text = request.form.get("mail", None)
    clas = 'Define mail param'

    print("mail:", text)
    if text is not None:
        cls = model.predict([text])[0]
        clas = 'Spam' if cls==1 else 'Not Spam'
    
    return render_template("index.html", 
                           pred=clas)

if __name__ == "__main__":
 
    model = pickle.load(open(filename, 'rb'))
    service.run(host="0.0.0.0", port=5002, 
                threaded=True, debug=True)
    # 192.168.1.129