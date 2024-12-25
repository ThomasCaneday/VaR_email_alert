import calculate_var

def check_risk(data, max_loss_threshold, max_leverage, current_portfolio_value):
    alerts = []
    for symbol, df in data.items():
        var = calculate_var(df)
        # Example metrics: Assume each stock contributes to 100% leverage
        current_price = df['close'].iloc[-1]
        if var > max_loss_threshold:
            alerts.append(f"{symbol}: VaR exceeds loss threshold! VaR: ${var:.2f}")
        
        leverage = current_price / current_portfolio_value
        if leverage > max_leverage:
            alerts.append(f"{symbol}: Leverage too high! Current Leverage: {leverage:.2f}")
    return alerts

# from connect import *
# from calculate_var import *
# symbols = ['AAPL', 'MSFT', 'NVDA']
# data = get_realtime_data(symbols)
# print(data)

# test_data = {symbol: data[symbol] for symbol in symbols}
# alerts = check_risk(test_data, max_loss_threshold=-5000, max_leverage=150000, current_portfolio_value=10000)
# print(alerts)
