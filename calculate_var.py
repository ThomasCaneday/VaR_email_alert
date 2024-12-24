from scipy.stats import norm

def calculate_var(data, confidence_level=0.95):
    # Calculate daily returns
    data['daily_return'] = data['close'].pct_change().dropna()

    # Mean and standard deviation of returns
    mu = data['daily_return'].mean()
    sigma = data['daily_return'].std()

    # VaR calculation (parametric method)
    z_score = norm.ppf(1 - confidence_level)
    var = -z_score * sigma * data['close'].iloc[-1]
    
    return var

# from connect import *
# symbols = ['AAPL', 'MSFT', 'NVDA']
# data = get_realtime_data(symbols)
# print(data)


# symbol = 'NVDA'
# sample_data = data[symbol]
# var = calculate_var(sample_data)
# print(f"{symbol} VaR: ${var:.2f}")