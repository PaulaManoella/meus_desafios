import requests
res_d = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
res_e = requests.get("http://economia.awesomeapi.com.br/json/last/EUR-BRL")
reqd_json= res_d.json()
reqe_json= res_e.json()
cotacao_d= float(reqd_json["USDBRL"]["bid"])
cotacao_e= float(reqe_json["EURBRL"]["bid"])
print('dolar:',cotacao_d,'  euro:',cotacao_e)

valor = float(input('digite um valor real para converter p dolar e euro:'))
valord= valor/cotacao_d
valore= valor/cotacao_e
print(f'{valor} em dolar é: {valord:.2f} \n{valor} em euro é: {valore:.2f}')