'''
Solution by Jack Klika 2020/11/05
'''

from collections import defaultdict

# FX Rates for each currency from USD: e.g. $100 USD * .85 = 85 GBP
fxFromUsdDict = {'USD': 1, 'GBP': .85, 'CNY': 6.35, 'JPY': 0.015}

# Reporting currency
RCURR = 'USD'

class Security: # represents a security in a holding; a 'stock'
    def __init__(self, name, ticker, weight, country, region, currency, price, totalshares, eps, dps):
        self.name = name
        self.ticker = ticker
        self.weight = weight  # weight of this stock in the portfolio
        self.country = country
        self.region = region
        self.currency = currency  # local currency code
        self.price = price  # price is in the local currency 
        self.tso = totalshares  #tso: total shares outstanding ## Shouldn't this be an integer?
        self.eps = eps  # earnings per share
        self.dps = dps  # dividend per share

        # Converts all prices to USD (local value * FX)
        ## Creating "usdprice" attribute since other values are calculated from local currency
        self.usdprice = self.price * fxFromUsdDict[self.currency]

        self.tmv = self.price*self.tso # Total Market Value (Price * Total Shares Outstanding) # Local currency
        self.per = self.price / self.eps # Price/Earnings ratio for each Security (Price / Earnings Per Share (EPS))
        self.dy = self.dps / self.price # Dividend Yield (Dividend Per Share (DPS) / Price)

    def __str__(self): # python-native 'tostring()' method
        return f"""{self.ticker} ({self.region}/{self.country})
        Total Market Value: ${self.tmv:.2f}
        Price ({self.currency}): {self.price:.2f}
        P/E Ratio: {self.per:.2f}
        EPS: {self.eps:.2f}
        """

class Portfolio:
    def __init__(self, portid, securitylist):
        self.portid = portid
        self.securitylist = securitylist

    def groupBy(self, attribute):
        """Groups the collection of positions by attribute as a dict, for example country or region"""
        retdict = defaultdict(list) # 'defaultdict'sets default dict value to a list so we can immediately add values
    
        try:
            [retdict[getattr(s, attribute)].append(s) for s in self.securitylist]
        except AttributeError:
            print(f"ERROR: Attribute '{attr}' not found")
    
        return retdict

    def positiveEpsOnly(self):
        """ Filter the collection to show only the positions with a positive EPS """ 
        return [sec for sec in self.securitylist if sec.eps >= 0]
        #print("EPS > 0:")
        #[print(f"\t{sec.ticker}: {sec.currency}${sec.eps}") for sec in pos_eps]

    def greaterThanOneMillionUSD(self):
        """ Filter the collection to show only positions with a total market value > one million """
        return [sec for sec in self.securitylist if sec.tmv*fxFromUsdDict[sec.currency] > 1e6]
        #print(f"Total Market Value > $1,000,000:")
        #[print(f"\t{sec.ticker}: ${sec.tmv:.2f}") for sec in tmv_gt_1m]

    def validatePortfolioWeight(self):
        """Validate portfolio weight sums to 100 within 12 decimal point precision"""

        # I round here because otherwise the floating point calculations
        # may return a number such as '100.00000000000001'
        return round(sum(sec.weight for sec in self.securitylist), 12) == 100


class SecurityGrouping:
    def __init__(self, portfolio, attribute):
        self.gdict = portfolio.groupBy(attribute)

    def __str__(self):
        """Print a grouping: A defaultdict of lists with a key of the grouping and value of a list of securities or single security"""
        for g in self.gdict:
            print(f"{g}:")
            if isinstance(self.gdict[g], list):
                for sec in self.gdict[g]: print("\t"+str(sec))
            else:
                print("\t"+str(self.gdict[g]))

    def largestWeightInGroup(self):
        gdict = self.gdict # shallow copy
        """Returns dict with keys of regions and value of security with largest weight"""
        for r in gdict: gdict[r] = max(gdict[r], key=lambda sec: sec.weight)
        return gdict
        #lwig = largestWeightInGroup(groupBy(fruitfolio, 'region'))
        #[print(f"\t{r}: {lwig[r].ticker} ({lwig[r].weight})") for r in lwig]

    def totalMarketValueByGroup(self):
        """Returns dict with keys of attribute and value total market value for that region"""
        gdict = self.gdict

        # Converting to and reporting with USD since I'm not going to mix currencies
        for r in gdict: gdict[r] = sum(sec.tmv*fxFromUsdDict[RCURR] for sec in gdict[r])
        return(ddict)
        #print("Total Market Value per Region:")
        #tmvpr = totalMarketValuePerRegion(groupBy(fruitfolio, "region"))
        #[print(f"\t{r}: ${tmvpr[r]:.2f}") for r in tmvpr]
