import schedule
import time
from connect import get_realtime_data
import check_risk
import send_email_alerts

MAX_LOSS_THRESHOLD = 50  # Example: $50 daily loss
MAX_LEVERAGE = 1.5       # Example: 1.5x leverage
PORTFOLIO_VALUE = 10000  # Example portfolio value
symbols = ['AAPL', 'MSFT', 'NVDA'] # Example stock symbols

def monitor_stocks():
    stock_data = get_realtime_data(symbols)
    alerts = check_risk(stock_data, MAX_LOSS_THRESHOLD, MAX_LEVERAGE, PORTFOLIO_VALUE)
    if alerts:
        send_email_alerts(alerts)

monitor_stocks()
# Schedule the task every hour
# schedule.every().hour.do(monitor_stocks)

# while True:
#     schedule.run_pending()
#     time.sleep(1)