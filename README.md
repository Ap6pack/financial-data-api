# 📊 Financial Data API

A FastAPI-based microservice that aggregates **free financial data** from multiple sources, including **Yahoo Finance, Alpha Vantage, Financial Modeling Prep, and Quandl (Nasdaq Data Link)**. This API provides **historical stock prices, fundamental data, technical indicators, and macroeconomic data** in a unified format.

---

## 🚀 Features
✅ Unified API for fetching stock market data  
✅ Integrates multiple free data sources  
✅ Includes **caching** to optimize performance  
✅ **Microservices-based**, scalable for deployment  
✅ **Dockerized** for easy deployment  

---

## 🛠 Tech Stack
- **FastAPI** (Lightweight & high-performance API framework)
- **yfinance** (Yahoo Finance data)
- **Alpha Vantage API** (Technical indicators)
- **Financial Modeling Prep API** (Fundamental data)
- **Quandl/Nasdaq Data Link API** (Macroeconomic data)
- **Uvicorn** (ASGI server)
- **Cachetools** (In-memory caching for efficiency)
- **Docker** (For containerization & easy deployment)

---

## 📂 Project Structure
```
/financial-data-api
│── src/
│   ├── api.py               # FastAPI application
│   ├── data_fetcher.py      # Handles API requests
│   ├── config.py            # Stores API keys
│   ├── cache.py             # Implements request caching
│── requirements.txt         # Dependencies
│── Dockerfile               # Docker containerization
│── README.md                # Project documentation
```

---

## 🚀 Installation & Setup
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Ap6pack/financial-data-api.git
cd financial-data-api
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the API**
```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload
```

### 4️⃣ **Test in Browser**
- Visit: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** (Swagger UI)
- Try: **[http://127.0.0.1:8000/stock/AAPL](http://127.0.0.1:8000/stock/AAPL)**

---

## 🔗 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API health check |
| `/stock/{ticker}` | GET | Get historical stock prices, fundamentals, and technical indicators |
| `/macro` | GET | Get macroeconomic data (e.g., GDP) |

Example response for `/stock/AAPL`:
```json
{
  "history": { "2024-03-01": {"close": 150.3} },
  "fundamentals": { "pe_ratio": 24.3, "debt_to_equity": 0.5 },
  "technical": { "SMA": { "50-day": 148.9, "200-day": 145.2 } }
}
```

---

## 🐳 Deploy with Docker
**1️⃣ Build the Docker Image**
```bash
docker build -t financial-data-api .
```
**2️⃣ Run the Container**
```bash
docker run -p 8000:8000 financial-data-api
```

---

## 📜 License
This project is licensed under the **Apache 2.0 License**. See the `LICENSE` file for details.

---

## 📧 Contact
For questions, reach out to **adamslinuxemail@gmail.com** or open an issue.

---

### **🚀 Ready to Take Your Trading AI to the Next Level?**
This API is a foundation for **AI-driven hedge fund strategies**. Connect it to your **AI hedge fund project** and build powerful trading bots! 🚀