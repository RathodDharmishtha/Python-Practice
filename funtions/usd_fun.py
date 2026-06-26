def usd_to_inr(usd):
    inr = usd * 83  # Example exchange rate
    return inr

usd = float(input("Enter amount in USD: "))
print("INR =", usd_to_inr(usd))