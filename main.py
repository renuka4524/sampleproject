from flask import Flask, render_template,request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
col = db['bookings']


@app.route('/')
def home():
    return render_template('first.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    destination = request.form['destination']
    date = request.form['date']

    booking = {
        'name': name,
        'email': email,
        'phone': phone,
        'destination': destination,
        'date': date
    }

    col.insert_one(booking)

    return 'Booking submitted!'


@app.route('/book-ticket', methods=['POST'])
def book_ticket():
    # Get user inputs
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    date = request.form['date']
    time = request.form['time']
    seat_type = request.form['seat-type']
    # Check availability and book ticket
    if is_ticket_available(date, time, seat_type):
        book_ticket(name, email, phone, date, time, seat_type)
        return "<script>document.getElementById('booking-form').style.display='none'; document.getElementById('confirmation-message').style.display='block';</script>"
    else:
        return "Sorry, the ticket is not available for the selected date and time."

def is_ticket_available(date, time, seat_type):
    # Implement ticket availability checking logic here
    return True # Example implementation

def book_ticket(name, email, phone, date, time, seat_type):
    # Implement ticket booking logic here
    pass # Example implementation


if __name__ == '__main__':
    app.run(debug=True)
