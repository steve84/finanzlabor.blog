import calendar
import csv
from extractor import *

dataset = SimFinDataset('output-semicolon-wide.csv','semicolon')

pre_header = ['Name', 'Ticker', 'Industry Code', 'Date', 'FinYearMonthEnd']

with open('extracted_data.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=";", quoting=csv.QUOTE_MINIMAL, fieldnames=(pre_header + [x.name for x in dataset.companies[0].data]))
    writer.writeheader()
    for company in dataset.companies:
        try:
            for i in range(0, len(dataset.timePeriodsDates)):
                if calendar.monthrange(dataset.timePeriodsDates[i].year, dataset.timePeriodsDates[i].month)[1] == dataset.timePeriodsDates[i].day:
                    row = dict()
                    row[pre_header[0]] = company.name
                    row[pre_header[1]] = company.ticker
                    row[pre_header[2]] = company.industryCode
                    row[pre_header[3]] = dataset.timePeriodsDates[i].date()
                    row[pre_header[4]] = company.finYearMonthEnd
                    hasValues = False

                    for indicator in company.data:
                        if indicator.name == 'Share Price' and indicator.values[i] is None:
                            if dataset.timePeriodsDates[i].weekday() == calendar.SATURDAY and indicator.values[i-1] is not None:
                                row[indicator.name] = float(indicator.values[i-1])
                            elif dataset.timePeriodsDates[i].weekday() == calendar.SUNDAY and indicator.values[i-2] is not None:
                                row[indicator.name] = float(indicator.values[i-2])

                        if indicator.name == 'Common Shares Outstanding' and indicator.values[i] is None:
                            start_index = i - 365
                            if start_index < 0:
                                start_index = 0
                            one_year_back = reversed(range(start_index, i))
                            for year_index in one_year_back:
                                if indicator.values[year_index] is not None:
                                    row[indicator.name] = float(indicator.values[year_index])
                                    break

                        if indicator.name not in row.keys():
                            if indicator.values[i] is not None:
                                row[indicator.name] = float(indicator.values[i])
                                if indicator.name not in ['Share Price','Common Shares Outstanding','Avg. Basic Shares Outstanding','Avg. Diluted Shares Outstanding','Market Capitalisation']:
                                    hasValues = True
                            else:
                                row[indicator.name] = None

                    if hasValues:
                        writer.writerow(row)
        except ValueError as e:
            print(e)
            continue
