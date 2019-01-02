from flask import Flask, url_for, redirect, render_template, session, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    try:
        balance = session["balance"]
    except KeyError:
        balance = session["balance"] = 8000
    
    if request.method == "GET":
        return render_template("index.html", balance=balance, msg="")
    
    if request.method == "POST":
        if request.form["amount"] == "":
            msg = "Amount is required"
            return render_template("index.html", balance=balance, msg=msg)

        if request.form["action"] == "Withdraw":
            if int(request.form["amount"]) > session["balance"] :
                msg = "Cannot withdraw amount greater than balance"
                return render_template("index.html", balance=balance, msg=msg)

			# Checks if amount is greater than 5000
            elif int(request.form["amount"]) > 5000 :
                msg = "Cannot withdraw amount greater than 5000"
                return render_template("index.html", balance=balance, msg=msg)

			# Deducts amount entered from balance and stores in session
            else:
                balance = balance - int(request.form["amount"])
                session["balance"] = balance
                msg = "Money Withdrawn"
                return render_template("index.html", balance=balance, msg=msg)
    
        elif request.form["action"] == "Deposit":
            if (int(request.form["amount"]) < 0):
                msg = "Deposit amount cannot be negative"
                return render_template("index.html", balance=balance, msg=msg)
            
            balance = balance + int(request.form["amount"])
            session["balance"] = balance
            msg = "Money Deposited"
            return render_template("index.html", balance=balance, msg=msg)

if __name__ == '__main__':
    app.secret_key = "luke_skywalker"
    app.run(host="localhost", port=8080, debug=True)
