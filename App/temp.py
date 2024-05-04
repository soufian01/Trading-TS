import requests

def get_company_outlook(symbol, api_key):
    url = f"https://financialmodelingprep.com/api/v4/company-outlook?symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Errore nella richiesta:", response.status_code)
        return None

def print_company_outlook(data):
    if data:
        if 'symbol' in data:
            print("Symbol:", data['symbol'])
        if 'profile' in data:
            profile = data['profile']
            print("Company Name:", profile['companyName'])
            print("Price Target:", profile['priceTarget'])
            # Aggiungi altri campi di interesse per la stampa
    else:
        print("Nessun dato disponibile")

# Imposta il simbolo e la tua chiave API
symbol = "AAPL"
api_key = "4a5b0f1569f2e6952a07de4043845c54"

# Ottieni i dati dell'outlook dell'azienda
company_outlook_data = get_company_outlook(symbol, api_key)

# Stampare l'outlook dell'azienda
print_company_outlook(company_outlook_data)
