## Quick Start Guide

### ⚡ 5-Minute Setup (Windows)

1. **Open Command Prompt** in the project folder

2. **Run the setup script**:
   ```bash
   setup.bat
   ```

3. **Edit configuration**:
   - Open `.env` file in any text editor
   - Add your Google API Key from [Google AI Studio](https://makersuite.google.com/app/apikey)

4. **Start the application**:
   ```bash
   venv\Scripts\activate
   streamlit run app.py
   ```

5. **Browser opens automatically** at `http://localhost:8501`

---

### ⚡ 5-Minute Setup (Mac/Linux)

1. **Open Terminal** in the project folder

2. **Run the setup script**:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Activate environment**:
   ```bash
   source venv/bin/activate
   ```

4. **Edit configuration**:
   - Open `.env` file in your preferred editor
   - Add your Google API Key from [Google AI Studio](https://makersuite.google.com/app/apikey)

5. **Start the application**:
   ```bash
   streamlit run app.py
   ```

6. **Browser opens automatically** at `http://localhost:8501`

---

### 📚 Manual Setup (If Scripts Fail)

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate it**:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file**:
   ```bash
   copy .env.example .env      # Windows
   cp .env.example .env         # Mac/Linux
   ```

5. **Edit .env** and add your API key

6. **Run the app**:
   ```bash
   streamlit run app.py
   ```

---

### 🔑 Getting Your Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click **"Create API Key"**
3. Copy the generated key
4. Paste it in your `.env` file as `GOOGLE_API_KEY=your_key_here`

⚠️ **Important**: Keep your API key secure and never commit it to version control!

---

### 🎯 Using the Application

1. **Upload** your document (PDF, DOCX, or TXT)
2. **Configure** the number of QnA pairs (3-10 recommended)
3. **Click Generate** to create QnA pairs
4. **Translate & Export** to get the Excel file
5. **Download** `Multilingual_QnA.xlsx`

---

### 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| API Key Error | Add GOOGLE_API_KEY to .env file |
| PDF won't parse | Ensure PDF contains readable text (not scanned image) |
| Slow generation | Normal for large documents - depends on document size |
| Module not found | Run `pip install -r requirements.txt` again |
| Port 8501 already in use | Kill the process or use `streamlit run app.py --server.port 8502` |

---

### 📞 Example Usage

**Input**: Business proposal document (5 pages)  
**QnA Pairs Generated**: 15+ pairs per language  
**Output**: Excel file with 3 sheets (EN, HI, MR)  
**Time**: 2-3 minutes  

---

### 📁 Files Overview

```
project/
├── app.py                 ← Run this to start
├── setup.bat             ← Windows setup
├── setup.sh              ← Mac/Linux setup
├── QUICKSTART.md         ← This file
├── requirements.txt      ← Dependencies
├── .env.example          ← Config template
├── config.py             ← Settings
└── [modules]             ← Core logic
```

---

**Ready?** Run setup now and let's generate some QnA pairs! 🚀
