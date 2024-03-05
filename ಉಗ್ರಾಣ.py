from flask import Flask, request

app = Flask(__name__)

@app.route('/flask', methods=['POST'])
def store_flask():
    data = request.get_json()
    num_bottles = data['bottles']
    drink = data['drink']
    date = data['date']
    thread = data['thread']
    
    plural_bottles = "ಬಾಟಲಿ" if int(num_bottles) == 1 else "ಬಾಟಲಿಗಳು"
    print("ಕಪಾಟಿನಲ್ಲಿ %s %s  %s. Date=%s Thread=%s" % (num_bottles, drink, plural_bottles, date, thread))
    
    return "ಚೀರ್ಸ್"

if __name__ == '__main__':
    app.run(debug=True, port=9999)
