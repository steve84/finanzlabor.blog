import pandas as pd
import simfin as sf
from simfin.names import *
import calendar
from datetime import timedelta


def getDate(d):
    if d.weekday() == calendar.SATURDAY:
        return d - timedelta(days=1)
    elif d.weekday() == calendar.SUNDAY:
        return d - timedelta(days=2)
    else:
        return d


# Wohin sollen die temporären Daten geladen werden
sf.set_data_dir('~/simfin_data/')
# API-Schlüssel, welcher nach kostenloser Registrierung verfügbar ist
sf.set_api_key(api_key='YOUR_API_KEY')

# Die möglichen Datensätze
datasets = ['income', 'balance', 'cashflow']
postfixes = ['', '-banks', '-insurance']

df_markets = sf.load_markets()
# Eine Liste aller verfügbaren Märkte
market_list = df_markets.index.values.tolist()

df_list = list()
# Alle Datensätze durchgehen
for ds in datasets:
    frames = list()
    for pst in postfixes:
        # Alle Märkte
        for mkt in market_list:
            # Lade den Datensatz für den aktuellen Markt
            print('Load dataset %s%s for market %s' % (ds, pst, mkt))
            try:
                frames.append(sf.load(dataset='%s%s' % (ds, pst), variant='annual',
                                    market=mkt, index=[SIMFIN_ID, REPORT_DATE],
                                    parse_dates=[REPORT_DATE, PUBLISH_DATE]))
            except:
                print('No data available for dataset %s%s and market %s' % (ds, pst, mkt))
    df_list.append(pd.concat(frames))

companies_list = list()
for mkt in market_list:
    # Lade alle Firmen
    companies_list.append(sf.load_companies(index=SIMFIN_ID, market=mkt))

df_companies = pd.concat(companies_list)
df_companies[SIMFIN_ID] = df_companies.index

# Lade alle Branchen
df_industries = sf.load_industries()

# Füge die einzelnen Teilstücke rechts aneinander
df_all = pd.concat(df_list, axis=1)
df_all[REPORT_DATE] = df_all.index.get_level_values(REPORT_DATE)
# Entferne mögliche Duplikate
df_all = df_all.loc[:, ~df_all.columns.duplicated()]
# Füge die Branche dazu
df_all = df_all.merge(
    df_companies.merge(
        df_industries,
        how='left',
        on=INDUSTRY_ID).set_index(SIMFIN_ID),
    how='left',
    on=SIMFIN_ID).drop(
    TICKER + '_y',
    axis=1)
df_all[TICKER] = df_all[TICKER + '_x']
df_all = df_all.drop(TICKER + '_x', axis=1)

df_all = df_all.set_index([TICKER, REPORT_DATE])
fin_sig_list = list()
for mkt in market_list:
    hub = sf.StockHub(market=mkt, refresh_days=30, refresh_days_shareprices=1)
    # Lade die Finanzsignale für den aktuelle Markt
    fin_sig_list.append(hub.fin_signals(variant='quarterly'))

df_all = pd.concat([df_all, pd.concat(fin_sig_list)], axis=1)


fin_price_list = list()
for mkt in market_list:
    hub = sf.StockHub(market=mkt, refresh_days=30, refresh_days_shareprices=1)
    try:
        # Lade die Aktienpreise für den aktuelle Markt
        fin_price_list.append(hub.load_shareprices(variant='daily'))
    except:
        print('Cannot load share prices for market %s' % mkt)

fin_prices = pd.concat(fin_price_list)

df_all = df_all.reset_index(level=[REPORT_DATE])
df_all['Share Price Date'] = df_all[REPORT_DATE].apply(getDate)

# Füge die Aktienpreise rechts als neue Spalten an
df_all = pd.merge(
    df_all, fin_prices, how='left', left_on=[
        TICKER, 'Share Price Date'], right_on=[
            TICKER, 'Date'])

val_signals_list = list()
for mkt in market_list:
    hub = sf.StockHub(market=mkt, refresh_days=30, refresh_days_shareprices=1)
    try:
        # Lade die Wertesignale für den aktuelle Markt
        val_signals_list.append(hub.val_signals(variant='daily'))
    except:
        print('Cannot load value signals for market %s' % mkt)

val_signals = pd.concat(val_signals_list)

df_all['Value Signals Date'] = df_all[REPORT_DATE].apply(getDate)
# Füge die Wertsignale rechts als neue Spalten an
df_all = pd.merge(
    df_all, val_signals, how='left', left_on=[
        TICKER, 'Value Signals Date'], right_on=[
            TICKER, 'Date'])

# Preis-Signale (price_signals), Volumen-Signale (volume_signals) und
# Wachstums-Signale können analog der Werte-Signale noch
# hinzugefügt werden

# Verwerfe Einträge welche kein Jahresabschluss sind
df_all = df_all.dropna(subset=[FISCAL_YEAR])

# Exportiere die Daten in ein CSV
df_all.to_csv('extracted_data.csv', sep=';')
