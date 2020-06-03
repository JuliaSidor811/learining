from flask import Flask, request, render_template
import csv
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def currency_calculator():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    currency_list = data[0]['rates']

    with open('currency.csv', 'w', newline='', encoding='UTF-8') as csvfile:
        fieldnames = ['currency', 'code', 'bid', 'ask']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for dana in currency_list:
            writer.writerow(
                {'currency': str(dana['currency']),
                 'code': str(dana['code']),
                 'bid': float(dana['bid']),
                 'ask': float(dana['ask'])}
            )
    code = []
    bid = []
    ask = []
    with open('currency.csv', 'r', newline='', encoding='UTF-8') as csvfileload:
        read = csv.DictReader(csvfileload, delimiter=';')
        for row in read:
            code.append(row['code'])
            ask.append(row['ask'])
            bid.append(row['bid'])
    csvfileload.close()

    if request.method == 'POST':
        choosen_currency = request.form.get('currency')
        choosen_acction = request.form.get('opperation')
        choosen_amount = request.form.get('amount')

        if len(choosen_amount) == 0:
            return "You didn't enter amount of money"

        if not choosen_amount.isdigit():
            return "You didn't enter digits"

        if choosen_acction == 'buy':
            index_in_code = code.index(choosen_currency)
            price = float(ask[index_in_code])
            total = float(choosen_amount) * price
            return f" You have to pay: {total:.2f} PLN"

        elif choosen_acction == 'sell':
            index_in_code = code.index(choosen_currency)
            price = float(bid[index_in_code])
            total = float(choosen_amount) * price
            return f" You recive: {total:.2f} PLN"

    return render_template("currency_calc.html", codes=code)


if __name__ == '__main__':
    app.run(debug=True)
