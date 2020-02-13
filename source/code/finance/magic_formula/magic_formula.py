import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from simfin.names import *


# Get corresponding index
def parentIndex(index, length):
    if index >= (length / 2):
        return int(index % (length / 2))
    else:
        return int(index + (length / 2))


# Is value of point 1 bigger than point 2
def isLonger(p1, p2):
    return p1.get_width() > p2.get_width()


def createFigure(
        data, x1, x2, label1, label2, filename,
        legend_loc, number_format='%.2f', hscaling=1, vscaling=1):
    order_list = data[COMPANY_NAME].tolist()

    # Create subplots
    fig, axes = plt.subplots(1, 1, squeeze=False)
    sb.set_color_codes("pastel")
    # First barplot
    sb.barplot(
        x=x1, y=COMPANY_NAME, data=data, ax=axes[0][0],
        label=label1, order=order_list, color='b')
    sb.set_color_codes("muted")
    # Second barplot
    sb.barplot(
        x=x2, y=COMPANY_NAME, data=data, ax=axes[0][0],
        label=label2, order=order_list, color='g')

    num_patches = len(axes[0][0].patches)
    # Annotate patches
    for p in axes[0][0].patches:
        p_index = parentIndex(axes[0][0].patches.index(p), num_patches)
        p_point = axes[0][0].patches[p_index]
        if isLonger(p, p_point):
            # Annotation of the longer bar plot
            axes[0][0].annotate(
                number_format % (p.get_width() - p_point.get_width()), (
                    p_point.get_width() +
                    ((p.get_width() - p_point.get_width()) / 2),
                    p.get_y() + (p.get_height() / 2)
                ),
                ha='center', va='center', xytext=(0, -1.375),
                textcoords='offset points')
        else:
            # Annotation of the shorter bar plot
            axes[0][0].annotate(
                number_format % p.get_width(), (
                    p.get_x() + p.get_width() / 2,
                    p.get_y() + (p.get_height() / 2)
                ),
                ha='center', va='center', xytext=(0, -1.375),
                textcoords='offset points')

    axes[0][0].legend(loc=legend_loc)
    axes[0][0].set_xlabel(None)
    # Set image size
    fig.set_size_inches(
        np.array([
            fig.get_size_inches()[0] * hscaling,
            fig.get_size_inches()[1] * vscaling
        ])
    )
    plt.tight_layout()
    plt.savefig(filename, format='png')


sb.set()

# Read SimFin export
df = pd.read_csv("extracted_data.csv", sep=";")

# Convert date string to datetime object
df[REPORT_DATE] = pd.to_datetime(df[REPORT_DATE])

df = df.dropna(subset=[INDUSTRY_ID])

df["Industry Short Code"] = df.get(
    INDUSTRY_ID).apply(lambda x: int(x / 1000))

# Get last financial year
df['LastReportDate'] = df.groupby(
    TICKER)[REPORT_DATE].transform("last")

print('Total figures: %d' % len(df))
df = df[df[REPORT_DATE] == df['LastReportDate']]
print('Total last figures: %d' % len(df))

# Filter market capitalization greater than 50 Mio USD
df = df[df[MARKET_CAP] > 50000000]
# Drop some industries
df = df[df['Industry Short Code'] != 104]
df = df[df['Industry Short Code'] != 105]
# Drop countries other than US
df = df[df[CURRENCY] == 'USD']

print('Total figures after market cap and industry removals: %d' % len(df))

# Calculate Working Capital
df['Net Working Capital'] = (
    df[TOTAL_CUR_ASSETS] - df[CASH_EQUIV_ST_INVEST] -
    df[TOTAL_CUR_LIAB])
# Calculate Net Fixed Assets (Ignore Intangible Assets and Goodwill)
df['Net Fixed Assets'] = df[TOTAL_ASSETS] - df[TOTAL_CUR_ASSETS]

# Calculate Return On Capital
df['ROC'] = (
    df[OP_INCOME] / (df['Net Working Capital'] + df['Net Fixed Assets'])) * 100

# Drop none available entries
df = df.dropna(subset=[EARNINGS_YIELD])
df = df.dropna(subset=['ROC'])

print('Total figures after n.a. removals: %d' % len(df))

df[EARNINGS_YIELD] = df[EARNINGS_YIELD] * 100

# Print out some statistic figures
print('Median EY: %f' % df[EARNINGS_YIELD].median())
print('Mean EY: %f' % df[EARNINGS_YIELD].mean())
print('Median ROC: %f' % df['ROC'].median())
print('Mean ROC: %f' % df['ROC'].mean())
df['EY_ROC'] = df[EARNINGS_YIELD] + df['ROC']

# Number of stocks for the Magic Formula (must be multiple of 2)
nbrOfStocks = 20

# Rank the numbers
df['EY_rank'] = df[EARNINGS_YIELD].rank(
    ascending=False, method='min')
df['ROC_rank'] = df['ROC'].rank(
    ascending=False, method='min')
df['total_rank'] = df['EY_rank'] + df['ROC_rank']

# Sort on total rank and take first ones
figure_data = df.sort_values(
    by=["total_rank"],
    ascending=True).head(nbrOfStocks)

# Create some figures
figure_data_without_zynex = figure_data.copy().set_index(['Ticker']).drop(['ZYXI'])
createFigure(
    figure_data_without_zynex, 'EY_ROC', EARNINGS_YIELD, 'Return On Capital (%)',
    'Earnings Yield (%)', 'ey_roc.png', 'lower right',
    vscaling=1.2, hscaling=2)
createFigure(
    figure_data, 'total_rank', 'EY_rank', 'Rank Return On Capital',
    'Rank Earnings Yield', 'ey_roc_rank.png', 'upper right',
    number_format='%d', vscaling=1.2, hscaling=2)

# Drop outliers
df_capped = df[df[EARNINGS_YIELD].between(
    df[EARNINGS_YIELD].quantile(0.05), df[EARNINGS_YIELD].quantile(0.95))]
df_capped = df_capped[df_capped['ROC'].between(
    df_capped['ROC'].quantile(0.05), df_capped['ROC'].quantile(0.95))]

# Save density plot
ax = sb.jointplot(EARNINGS_YIELD, 'ROC', data=df_capped, kind='kde', color="g")
ax.set_axis_labels('Earnings Yield (%)', 'Return On Capital (%)')
plt.tight_layout()
plt.savefig('density_plot.png', format='png')

plt.clf()

# Create industry histogram
ax = sb.countplot(x=SECTOR, data=figure_data, palette='Blues_d')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.set_ylabel('Amount')
ax.set_xlabel('Industry')
plt.tight_layout()
plt.savefig('industry_histogram.png', format='png')
