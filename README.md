# 📊 Excel ChatBot

A Streamlit-based data visualization application that uses AI (OpenAI + LIDA) to automatically generate insightful charts and summaries from CSV and Excel files. Includes a local fallback for monthly bar charts when LLM services are unavailable.

## ✨ Features

- **📁 Data Summarization**: Upload CSV/XLSX files and get automatic summaries with AI-generated visualization suggestions
- **🔍 Query-Based Graph Generation**: Ask natural language questions (e.g., "Draw a barchart for each month") and get visualizations
- **🛡️ Graceful Fallback**: If OpenAI quota is exceeded or the API key is missing, the app automatically falls back to local monthly bar chart generation
- **📈 Support for Multiple Formats**: Works with CSV and Excel (.xlsx) files
- **🎨 Multiple Chart Types**: Seaborn-based visualizations with interactive Streamlit interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git
- OpenAI API key (optional — local fallback works without it)

### Local Installation & Running (macOS/Linux/WSL)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AreefSyam/excelChatBot.git
   cd excelChatBot
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # macOS/Linux/WSL
   # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project root (or in the `app/` folder if using the old structure):

   ```env
   OPENAI_API_KEY=sk-your-openai-api-key-here
   ```

   Or, export it in your shell:

   ```bash
   export OPENAI_API_KEY="sk-your-openai-api-key-here"
   ```

   **Note**: If you don't set an API key, the app will still work using local plotting for monthly aggregations.

5. **Run the app:**

   ```bash
   streamlit run app.py --server.port=8501 --server.enableCORS=false
   ```

6. **Open in your browser:**
   ```
   http://localhost:8501
   ```

## 🐳 Docker Installation & Running

1. **Build the Docker image:**

   ```bash
   docker build -t excelchatbot:latest .
   ```

2. **Run the container:**

   ```bash
   docker run --rm --env-file .env -p 8501:8501 excelchatbot:latest
   ```

   Or, pass the API key directly:

   ```bash
   docker run --rm -e OPENAI_API_KEY="sk-your-api-key" -p 8501:8501 excelchatbot:latest
   ```

3. **Access the app:**
   ```
   http://localhost:8501
   ```

## 📖 Usage

### Summarize Mode

1. Select **"Summarize"** from the sidebar menu
2. Upload a CSV or Excel file
3. The app will:
   - Generate a text summary of your data
   - Suggest a visualization goal
   - Display an AI-generated chart based on that goal

### Question-Based Graph Mode

1. Select **"Question based Graph"** from the sidebar menu
2. Upload a CSV or Excel file
3. Enter your query (e.g., "Show me monthly trends", "Draw a barchart for each month")
4. Click **"Generate Graph"**
5. The app will:
   - Try to use OpenAI/LIDA to generate a custom visualization based on your query
   - If the OpenAI API fails or quota is exceeded, it automatically falls back to a local monthly bar chart

## 🔄 Fallback Behavior

If the OpenAI API is unavailable, quota is exceeded (error 429), or `OPENAI_API_KEY` is not set:

1. The app displays a clear warning message
2. It automatically attempts to generate a **local monthly bar chart** by:
   - Detecting a date/time column in your data (or parsing the first column as dates)
   - Grouping rows by month
   - Aggregating numeric columns (sum) or counting rows per month
   - Plotting using Seaborn/Matplotlib

**Example**: Upload `MalaysiaFloodDataset.csv` with a date column and the app will show a monthly count or sum without needing OpenAI.

## 📋 Project Structure

```
excelChatBot/
├── README.md              # This file
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in git)
├── .gitignore             # Git ignore rules
└── app.py                 # Main Streamlit application
```

## 📦 Dependencies

- **streamlit** — Web app framework
- **python-dotenv** — Load environment variables from `.env`
- **openai** — OpenAI API client
- **lida** — LLM-powered data visualization generator
- **pandas** — Data manipulation
- **matplotlib** — Plotting library
- **seaborn** — Statistical plotting library
- **Pillow** — Image processing
- **openpyxl** — Excel file support

See `requirements.txt` for exact versions.

## ⚙️ Configuration

### OpenAI API Key

- **Required for**: Full LLM-powered summarization and chart generation
- **How to get**: Visit [OpenAI Platform](https://platform.openai.com/api-keys)
- **Set via**: `.env` file or environment variable `OPENAI_API_KEY`
- **Not required**: The app has a built-in local fallback for monthly bar charts

### Streamlit Options

- `--server.port=8501` — Port to run on (default: 8501)
- `--server.enableCORS=false` — Disable CORS (default behavior in Docker)

## 🐛 Troubleshooting

### ImportError: No module named 'lida'

- Ensure your virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`
- If `lida` fails to install, it may require a specific Python version or additional system libraries

### ImportError: No module named 'seaborn' or 'matplotlib'

- These are in `requirements.txt` and should be installed automatically
- If missing: `pip install seaborn matplotlib openpyxl`

### OpenAI Error 429 (insufficient_quota)

- Your OpenAI API account has exceeded its quota
- Check your [OpenAI Billing](https://platform.openai.com/account/billing/overview)
- The app will automatically use the local monthly bar chart fallback
- No action needed — just use the local fallback

### Port 8501 already in use

- Change the port: `streamlit run app.py --server.port=8502`
- Or kill the existing process using the port

### Excel file won't load

- Ensure the file is valid `.xlsx` format
- If using older `.xls` files, convert to `.xlsx` first
- If you see errors, `openpyxl` must be installed: `pip install openpyxl`

### No date column found for local fallback

- The fallback looks for columns named "date", "time", "datetime", etc.
- If your date column has a different name, rename it or ask in an issue
- Alternatively, make sure the first column can be parsed as dates

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report issues or bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is part of the excelChatBot repository. See the repository for license details.

## 📧 Support

For issues or questions, please open an issue on the [GitHub repository](https://github.com/AreefSyam/excelChatBot).

---

**Happy charting! 📊**
