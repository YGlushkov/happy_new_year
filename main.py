from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def happy_new_year():
    now = datetime.datetime.now()

    current_year = now.year

    # Print a message welcoming the new year
    print("Happy New Year!")
    # Calculate the number of days until New Year's Day of the next year
    new_year = datetime.datetime(current_year + 1, 1, 1)
    delta = new_year - now
    days_until_new_year = delta.days

    # Print the number of days until New Year's Day
    # return f"There are {days_until_new_year} days until New Year's Day."
    return render_template("base.html",  days=days_until_new_year, hours=delta.seconds // 60 // 60)


if __name__ == "__main__":
    app.run(debug=True)