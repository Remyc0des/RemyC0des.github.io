from flask import Flask, render_template, send_from_directory
import datetime 
import calendar
app = Flask(__name__, static_folder="Remyc0des.github.io")
days = 0
last_updated = None
index = 'index.html'
@app.route("/")
def home():
    global days, last_updated, index
    start_date = datetime.datetime(2024,7,1)
    current_date =  datetime.datetime.now()
    x = current_date.weekday() + 1
    if last_updated is None or last_updated.date() != current_date.date():
        if x in range(1,5):
            days += 1 
            print("day",days)
        else:
            print("not a program day")
            print("day:",days)

        last_updated = current_date
        print(last_updated)
    return send_from_directory(path=index, day_num=days)

if __name__ == "__main__":
  app.run()