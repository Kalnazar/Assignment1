import congif
from congif import *

cryptoList = []
cryptoNumber = int(input('Enter the number of Cryptocurrencies: '))

def imp(x):
    for i in range(x):
        cryptoList.append((int(report[i]['market_cap']), report[i]['name']))

def out(x):
    for i in range(x):
        print("Name of", i + 1, "cryptocurrency and market cap:")
        print(cryptoList[i][1], cryptoList[i][0], "\n")

if __name__ == '__main__':
    imp(cryptoNumber)
    print("Result cryptocurrencies, from maximum to minimum: \n")
    out(cryptoNumber)