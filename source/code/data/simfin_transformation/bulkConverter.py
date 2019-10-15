import calendar
import csv
from extractor import *


def getSharePrice(dataset, indicator, index):
    if (
        dataset.timePeriodsDates[index].weekday() == calendar.SATURDAY and
        indicator.values[index-1] is not None
    ):
        return float(indicator.values[index-1])
    elif (
        dataset.timePeriodsDates[index].weekday() == calendar.SUNDAY and
        indicator.values[index-2] is not None
    ):
        return float(indicator.values[index-2])


def isEndOfMonth(actualDate):
    lastDayOfMonth = calendar.monthrange(actualDate.year, actualDate.month)[1]
    return lastDayOfMonth == actualDate.day


def checkHasNoValue(indicatorName, indicator, index):
    if type(indicatorName) is list:
        return (indicator.name in indicatorName and
                indicator.values[index] is None)
    else:
        return (indicator.name == indicatorName and
                indicator.values[index] is None)


def checkValuesOneYearBack(indicator, index):
    start_index = max(0, index - 365)
    one_year_back = reversed(range(start_index, index))
    for year_index in one_year_back:
        if indicator.values[year_index] is not None:
            return float(indicator.values[year_index])

    return None


dataset = SimFinDataset('output-semicolon-wide.csv', 'semicolon')

pre_header = ['Name', 'Ticker', 'Industry Code', 'Date', 'FinYearMonthEnd']

fieldsShares = [
          'Common Shares Outstanding',
          'Avg. Basic Shares Outstanding',
          'Avg. Diluted Shares Outstanding',
]
fieldsPrice = [
          'Share Price',
          'Market Capitalisation'
]
fieldsInEveryRow = fieldsPrice + fieldsShares


with open('extracted_data.csv', 'w') as csvfile:
    writer = csv.DictWriter(
        csvfile, delimiter=";",
        quoting=csv.QUOTE_MINIMAL,
        fieldnames=(pre_header + [x.name for x in dataset.companies[0].data])
    )
    writer.writeheader()
    for company in dataset.companies:
        try:
            # Go through every observation
            for i in range(0, len(dataset.timePeriodsDates)):
                # Check if end of month
                if isEndOfMonth(dataset.timePeriodsDates[i]):
                    row = dict()
                    row[pre_header[0]] = company.name
                    row[pre_header[1]] = company.ticker
                    row[pre_header[2]] = company.industryCode
                    row[pre_header[3]] = dataset.timePeriodsDates[i].date()
                    row[pre_header[4]] = company.finYearMonthEnd
                    hasValues = False

                    # Go through every indicator
                    for indicator in company.data:
                        indicatorName = indicator.name
                        indicatorValue = indicator.values[i]
                        # Special treatment for share price
                        if checkHasNoValue('Share Price', indicator, i):
                            row[indicatorName] = getSharePrice(dataset,
                                                               indicator,
                                                               i)
                        # Special treatment for outstanding shares
                        if checkHasNoValue(fieldsShares, indicator, i):
                            value = checkValuesOneYearBack(indicator, i)
                            if value:
                                row[indicatorName] = value

                        # Check if value was found for the given indicator
                        if indicatorName not in row.keys():
                            if indicatorValue is not None:
                                row[indicatorName] = float(indicatorValue)
                                if indicatorName not in fieldsInEveryRow:
                                    hasValues = True
                            else:
                                row[indicatorName] = None

                    if hasValues:
                        writer.writerow(row)
        except ValueError as e:
            print(e)
            continue
