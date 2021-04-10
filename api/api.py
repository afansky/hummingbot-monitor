from flask import Flask
from flask import request
import mysql.connector

mydb = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="hummingbot"
)

app = Flask(__name__)


@app.route('/', methods=['POST'])
def store():
    json = request.get_json()

    print("got a request")

    mycursor = mydb.cursor()

    sql = "INSERT INTO bots (name, trades) VALUES (%s, %s)"
    val = (json.name, json.trades)
    mycursor.execute(sql, val)
    mydb.commit()

    return """
    {
        success: true
    }
    """


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
