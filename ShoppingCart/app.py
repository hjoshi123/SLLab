from flask import Flask, request, render_template, url_for, session, redirect

app = Flask(__name__)

data = [
    { "name": "Xbox One S" },
    { "name": "PS4 Pro" },
    { "name": "PS4 Slim" }
]

@app.route("/", methods=["GET"])
def index():
    if session.get(data[0]["name"]) or session.get(data[1]["name"]) or session.get(data[2]["name"]):
        store = [
            { data[0]["name"]: session.get(data[0]["name"]) },
            { data[1]["name"]: session.get(data[1]["name"]) },
            { data[2]["name"]: session.get(data[2]["name"]) }
        ]
    else:
        session[data[0]["name"]] = 0
        session[data[1]["name"]] = 0
        session[data[1]["name"]] = 0
        store = [
            { data[0]["name"]: session.get(data[0]["name"]) },
            { data[1]["name"]: session.get(data[1]["name"]) },
            { data[2]["name"]: session.get(data[2]["name"]) }
        ]
    print (store)
    return render_template("index.html", data=data, store=store)

@app.route("/submit", methods=["POST"])
def submit():
    select = request.form.get("opt")
    quantity = request.form.get("quan")
    print (select)
    if select not in session:
        session[select] = int (quantity)
    else:
        session[select] += int(quantity)
    return redirect(url_for('index'))

@app.route("/cart", methods=["POST"])
def cart():
    cart = [
        { data[0]["name"]: session[data[0]["name"]] },
        { data[1]["name"]: session[data[1]["name"]] },
        { data[2]["name"]: session[data[2]["name"]] }
    ]
    msg = { "status" : 1, "cart": cart }
    return render_template("cart.html", msg=msg)

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    print ('Hello')    

# Always keep debug=True to debug Internal Server Error and other verbose logging
if __name__ == "__main__":
    app.secret_key = "yolo"
    app.run(host='localhost', port=8080, debug=True)