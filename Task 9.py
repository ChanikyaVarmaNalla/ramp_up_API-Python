import csv

def average_close_prices(filename):
    company_close_prices = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            date = row['Date']
            company = row['Company']
            close_price = float(row['Close'])
            month = date.split('-')[1]

            if (company, month) in company_close_prices:
                company_close_prices[(company, month)].append(close_price)
            else:
                company_close_prices[(company, month)] = [close_price]
    for (company, month), prices in company_close_prices.items():
        average_price = round(sum(prices) / len(prices), 2)
        yield f"{company} average close price for {month}th month is {average_price}"

for result in average_close_prices('stock_data.csv'):
    print(result)
