import csv

from flask import Flask, request, render_template

from data import get_data

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def currency_calculator():
    code, bid, ask = get_data()
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
    app.run()
