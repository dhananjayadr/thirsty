from flask import Flask, request

app = Flask(__name__)

@app.route('/flask', methods=['POST'])
def store_flask():
    data = request.get_json()
    num_bottles = data['bottles']
    drink = data['drink']
    date = data['date']
    thread = data['thread']
    
    plural_bottles = "bottle" if int(num_bottles) == 1 else "bottles"
    print(" There are %s %s of %s in the cabinet. Date=%s Thread=%s" % (num_bottles, plural_bottles, drink, date, thread))
    
    return "cheers!"

if __name__ == '__main__':
    app.run(debug=True, port=9999)
