import asyncio
from yahoo_fin.stock_info import get_day_gainers, get_day_losers, get_day_most_active
from concurrent.futures import ThreadPoolExecutor

def abbrevia_numero(numero):
    if numero >= 1000000000:
        return str(round(numero / 1000000000, 2)) + 'B'
    elif numero >= 1000000:
        return str(round(numero / 1000000, 2)) + 'M'
    elif numero >= 1000:
        return str(round(numero / 1000, 2)) + 'k'
    else:
        return str(round(numero, 2))

async def fetch_data():
    with ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        gainers_task = loop.run_in_executor(executor, get_day_gainers)
        losers_task = loop.run_in_executor(executor, get_day_losers)
        most_active_task = loop.run_in_executor(executor, get_day_most_active)

        gainers, losers, most_active = await asyncio.gather(gainers_task, losers_task, most_active_task)
    #rename the columsn name
    gainers = gainers.rename(columns={"Symbol": "symbol", "Price (Intraday)": "price", "Change": "change", "% Change": "percent_change", "Name": "name", "Market Cap": "market_cap", "PE Ratio (TTM)": "pe_ratio", "Volume": "volume"})
    losers = losers.rename(columns={"Symbol": "symbol", "Price (Intraday)": "price", "Change": "change", "% Change": "percent_change", "Name": "name", "Market Cap": "market_cap", "PE Ratio (TTM)": "pe_ratio", "Volume": "volume"})
    most_active = most_active.rename(columns={"Symbol": "symbol", "Price (Intraday)": "price", "Change": "change", "% Change": "percent_change", "Name": "name", "Market Cap": "market_cap", "PE Ratio (TTM)": "pe_ratio", "Volume": "volume"})
    



    gainers.fillna("N/A", inplace=True)
    losers.fillna("N/A", inplace=True)
    most_active.fillna("N/A", inplace=True)

    gainers = gainers.to_dict(orient="records")
    losers = losers.to_dict(orient="records")
    most_active = most_active.to_dict(orient="records")

    return gainers, losers, most_active

async def main():
    gainers, losers, most_active = await fetch_data()
    return gainers, losers, most_active

