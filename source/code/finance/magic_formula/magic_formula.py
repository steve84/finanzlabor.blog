import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


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
    order_list = data['Name'].tolist()

    # Create subplots
    fig, axes = plt.subplots(1, 1, squeeze=False)
    sb.set_color_codes("pastel")
    # First barplot
    sb.barplot(
        x=x1, y="Name", data=data, ax=axes[0][0],
        label=label1, order=order_list, color='b')
    sb.set_color_codes("muted")
    # Second barplot
    sb.barplot(
        x=x2, y="Name", data=data, ax=axes[0][0],
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
# Read SimFin instustries
df_industries = pd.read_csv("simfin_industries_20180709.csv", sep=",")

# Merge both datasets
df["Industry Short Code"] = df.get(
    "Industry Code").apply(lambda x: int(x / 1000))
df_industries.columns = ["Industry Short Code", "Branch Name"]
df = df.merge(df_industries, how="left", on="Industry Short Code")

df_industries.columns = ["Industry Code", "Industry Name"]
df = df.merge(df_industries, how="left", on="Industry Code")

# Convert date string to datetime object
df["Date"] = pd.to_datetime(df["Date"])

df['Year'] = df['Date'].map(lambda x: x.year)
# Calculate fiscal year
df['FiscalYear'] = df.apply(
    lambda x: x['Year'] if x['FinYearMonthEnd'] == 12
    else int(x['Year']) - 1, axis=1)
df['Month'] = df['Date'].map(lambda x: x.month)
df['MonthYear'] = df['Date'].map(lambda x: str(x.month) + ' ' + str(x.year))
# Get last financial year
df['LastFinYear'] = df[df['Month'] == df['FinYearMonthEnd']].groupby(
    "Ticker").Date.transform("last")

df['Sector'] = df['Industry Code'].map(lambda x: int(x / 1000))

print('Total figures: %d' % len(df))
df = df[df['Date'] == df['LastFinYear']]
print('Total last figures: %d' % len(df))

# Filter market capitalization greater than 50 Mio USD
df = df[df['Market Capitalisation'] > 50]
# Drop some industries
df = df[df['Industry Short Code'] != 104]
df = df[df['Industry Short Code'] != 105]
print('Total figures after market cap and industry removals: %d' % len(df))

# Calculate Earnings Yield
df['EY'] = (df['EBIT'] / df['Enterprise Value']) * 100
df['Net Working Capital'] = (
    df['Current Assets'] - df['Cash & Cash Equivalents'] -
    df['Current Liabilities'])
df['Net Fixed Assets'] = (
    df['Total Assets'] - df['Current Assets'] -
    df['Intangible Assets'] - df['Goodwill'])

# Calculate Return On Capital
df['ROC'] = (
    df['EBIT'] / (df['Net Working Capital'] + df['Net Fixed Assets'])) * 100

# Drop none available entries
df = df.dropna(subset=['EY'])
df = df.dropna(subset=['ROC'])

print('Total figures after n.a. removals: %d' % len(df))

# Print out some statistic figures
print('Median EY: %f' % df['EY'].median())
print('Mean EY: %f' % df['EY'].mean())
print('Median ROC: %f' % df['ROC'].median())
print('Mean ROC: %f' % df['ROC'].mean())
df['EY_ROC'] = df['EY'] + df['ROC']

# Number of stocks for the Magic Formula (must be multiple of 2)
nbrOfStocks = 20

# Rank the numbers
df['EY_rank'] = df['EY'].rank(
    ascending=False, method='min')
df['ROC_rank'] = df['ROC'].rank(
    ascending=False, method='min')
df['total_rank'] = df['EY_rank'] + df['ROC_rank']

# Sort on total rank and take first ones
figure_data = df.sort_values(
    by=["total_rank"],
    ascending=True).head(nbrOfStocks)

# Create some figures
createFigure(
    figure_data[1:], 'EY_ROC', 'EY', 'Return On Capital (%)',
    'Earnings Yield (%)', 'ey_roc.png', 'lower right',
    vscaling=1.2, hscaling=2)
createFigure(
    figure_data, 'total_rank', 'EY_rank', 'Rank Return On Capital',
    'Rank Earnings Yield', 'ey_roc_rank.png', 'upper right',
    number_format='%d', vscaling=1.2, hscaling=2)

# Drop outliers
df_capped = df[df['EY'].between(
    df['EY'].quantile(0.05), df['EY'].quantile(0.95))]
df_capped = df_capped[df_capped['ROC'].between(
    df_capped['ROC'].quantile(0.05), df_capped['ROC'].quantile(0.95))]

# Save density plot
ax = sb.jointplot('EY', 'ROC', data=df_capped, kind='kde', color="g")
ax.set_axis_labels('Earnings Yield (%)', 'Return On Capital (%)')
plt.tight_layout()
plt.savefig('density_plot.png', format='png')

plt.clf()

# Create industry histogram
ax = sb.countplot(x='Branch Name', data=figure_data, palette='Blues_d')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.set_ylabel('Amount')
ax.set_xlabel('Industry')
plt.tight_layout()
plt.savefig('industry_histogram.png', format='png')
