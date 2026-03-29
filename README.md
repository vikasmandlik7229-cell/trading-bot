# Trading Bot (Binance Futures Testnet)

## About this Project

This project is a simple trading bot built using Python that connects to the Binance Futures Testnet.  
The main idea behind this project was to understand how real trading APIs work and how to structure a small but complete system.

Using this bot, I can place BUY or SELL orders directly from the command line. It supports both MARKET and LIMIT orders and includes proper validation and logging.

---

## What this Bot Can Do

- Place MARKET orders instantly
- Place LIMIT orders with a specified price
- Supports both BUY and SELL
- Takes input from command line (CLI)
- Validates inputs before placing orders
- Logs all requests, responses, and errors

---

## Tech Used

- Python  
- Binance API (Testnet)  
- dotenv (for API keys)  
- logging (for tracking activity)  

---

## Project Structure


---

## How to Run the Project

### 1. Install dependencies


---

### 2. Add your API keys

Create a `.env` file in the root folder:


---

### 3. Run the bot

#### MARKET order

---

## Things I Learned

While building this project, I understood:

- How to connect and work with real APIs
- Handling errors like timestamp sync issues
- Binance minimum order size rules
- Writing clean and modular Python code
- Logging and debugging properly

---

## Notes

- This project uses Binance **Futures Testnet**, not real money
- Orders must be above ~100 USDT (Binance rule)
- Time synchronization is handled in the client setup

---

## Final Thoughts

This project helped me understand how trading systems work at a basic level.  
It is simple, but it covers important concepts like API integration, validation, and structured coding.

This can be extended further into a full automated trading system with strategies in the future.
