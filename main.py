from fruitfolio import Security

fruitfolio = [
Security("Avocado Assets", "GUAC LN", 15.23, 'UK', 'Europe', 'GBP', 200.03, 13.7, 5.92, 25.37),
Security("Banana Billings", "BAN US", 13.29, 'USA', 'NA', 'USD', 93.44, 16.9, -3.61, 0),
Security("Coconut Corp", "COCO US", 11.07, 'USA', 'NA', 'USD', 1335.07, 2.3, 10.96, 112.32),
Security("Daikon Deliveries", "CH00989", 10.74, 'China', 'Asia', 'CNY', 34.47, 35.7, 1.17, 0),
Security("Eggplant Enterprises", "EGGY JP", 9.25, 'Japan', 'Asia', 'JPY', 18160, 28.5, 417.67, 2008),
Security("Fig Factories US", "FIGS US", 7.94, 'USA', 'NA', 'USD', 22.35, 40.8, -0.01, 0),
Security("Grape Group UK", "GG LN", 7.72, 'UK', 'Europe', 'GBP', 47.35, 51, -0.69, 0.07),
Security("Honeycrisp Holdings", 'HONY US', 6.65, 'USA', 'NA', 'USD', 103.05, 100.35, 0.47, 2.03),
Security("Imbe Intelligence", "IMBE US", 6.38, 'USA', 'NA', 'USD', 72.47, 25.05, 2.43, 0),
Security("Jackfruit Jets", "CH00123", 6.03, 'China', 'Asia', 'CNY', 68.87, 13.5, -2.34, 0),
Security("Kiwi Konglomerate", "KIWI LN", 5.7, 'UK', 'Europe', 'GBP', 2.77, 50.2, 0.09, 0)
]

p = Portfolio(45, fruitfolio)

print(p.validatePortfolioWeight())
