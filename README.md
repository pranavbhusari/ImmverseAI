# 🚀 Multilingual QnA Generation System

An intelligent system that automatically generates meaningful and accurate Question-Answer (QnA) pairs from any input document, and outputs the results in three languages: **English, Hindi, and Marathi**.

## ✨ Features

- 📄 **Multi-format Support**: Process PDF, DOCX, and TXT files
- 🤖 **AI-Powered QnA**: Uses Groq API with Llama-3.3-70b model
- 🌐 **Multilingual Output**: English, Hindi, and Marathi translations
- 📊 **Excel Export**: Three formatted worksheets with color-coded headers
- 🎨 **Streamlit Web UI**: Easy-to-use interface for document processing
- 📚 **Smart Sampling**: 5 evenly-spaced chunks from entire document
- ⚡ **Fast & Accurate**: Individual translations for maximum accuracy
- 💰 **100% Free**: Groq (10k requests/day) + Google Translate APIs

## 📁 Project Structure

```
ImmverseAI/
├── app.py                 # Main Streamlit application
├── qna_generator.py       # QnA generation (Groq API - Llama)
├── translator.py          # Translation to Hindi/Marathi (Google)
├── document_parser.py     # PDF/DOCX/TXT parsing
├── excel_exporter.py      # Excel file creation
├── requirements.txt       # Python dependencies
├── .env                   # API keys (Groq)
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── QUICKSTART.md         # Quick start guide
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Groq API key (get free at https://console.groq.com/keys)
- pip

### 📌 Quick Setup

1. **Clone repository**
```bash
git clone https://github.com/YOUR-USERNAME/ImmverseAI.git
cd ImmverseAI
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Get Groq API key**
   - Visit https://console.groq.com/keys
   - Create free account
   - Generate API key

5. **Set up .env file**
```bash
# Create .env file
echo GROQ_API_KEY=your_api_key_here > .env
```

6. **Run application**
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## � Deployment

### Option 1: Docker (Local Testing)
```bash
# Build and run locally
docker-compose up --build
```
App runs at `http://localhost:8501`

### Option 2: Deploy to Render (Production)
See [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for complete instructions:
1. Push to GitHub
2. Connect GitHub to Render
3. Create Web Service with Docker
4. Add GROQ_API_KEY environment variable
5. Deploy! (takes ~5-10 minutes)

**Deployed URL**: `https://immverse-ai.onrender.com` (example)

## �📖 Usage

1. **Upload Document** → Select PDF, DOCX, or TXT file
2. **Configure** → Set number of questions (default: 3)
3. **Generate QnA** → AI generates Q&A pairs from document
4. **Translate** → Auto-translates to Hindi & Marathi
5. **Download** → Excel file with 3 language sheets

## ⚙️ Configuration

Edit in app.py:
- `questions_per_chunk` (default: 3) - Q&A pairs per section
- `chunk_size` (default: 8000) - Characters per chunk
- Languages for translation (English, Hindi, Marathi)

## 📊 Performance

| Task | Time |
|------|------|
| QnA Generation | 2-5s |
| Translation | 7-8s |
| Excel Export | 1s |
| **Total** | **~15s** |

## 💾 API Usage

### Groq API (QnA Generation)
- **Free Tier**: 10,000 requests/day
- **Model**: Llama-3.3-70b-versatile
- **Cost**: Free ✅

### Google Translate API
- **Free Tier**: Unlimited
- **Quality**: High accuracy
- **Cost**: Free ✅

## 🐛 Troubleshooting

**Error: GROQ_API_KEY not found**
> Create `.env` file with your API key

**Error: Document parsing fails**
> Ensure file is PDF/DOCX/TXT and not corrupted

**Translation showing English**
> Check internet connection and restart app

## 📝 Output Format

Excel file contains 3 sheets:
- **English** - Original Q&A pairs
- **Hindi** - Translated Q&A pairs
- **Marathi** - Translated Q&A pairs

Features:
- Color-coded headers
- Auto-sized columns
- Text wrapping
- Professional formatting

## 🔧 How It Works

### Document Processing
1. Upload document (PDF/DOCX/TXT)
2. Extract text
3. Split into 5 evenly-spaced chunks (full document coverage)

### QnA Generation
1. Process each chunk with Groq API
2. Generate contextual Q&A pairs
3. Combine results

### Translation
1. Translate each question individually
2. Translate each answer individually
3. Format into Excel sheets

## 🎯 Example

**Input**: Python tutorial PDF
**Output**: Excel with:
- 15 English Q&A pairs
- 15 Hindi Q&A pairs
- 15 Marathi Q&A pairs

## 📋 Requirements

```
streamlit>=1.28.1
python-docx>=0.8.11
pdfplumber>=0.9.0
openpyxl>=3.10.0
groq>=0.4.1
requests>=2.31.0
python-dotenv>=1.0.0
```

## 📧 Support

Issues? Open a GitHub issue!

## 📝 License

MIT License - feel free to use!

---

**Made with ❤️ for Multilingual QnA Generation**


### Step 1: Clone/Setup Project
```bash
cd c:\Users\Rutika\Desktop\ImmverseAI
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Google API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```
4. Edit `.env` and add your API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

## Usage

### Running the Application

1. **Activate virtual environment (if created)**:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

2. **Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

3. **The app will open in your browser** at `http://localhost:8501`

### Using the Application

**Step 1: Upload Document**
- Click on "Choose a file" and select your document (PDF, DOCX, or TXT)
- The system will extract and preview the text content

**Step 2: Configure Settings**
- **Number of QnA pairs per chunk**: 1-10 (default: 3)
- **Text chunk size**: 500-2000 characters (default: 1000)
- **Google API Key**: Enter your API key if not in environment

**Step 3: Generate QnA Pairs**
- Click "Generate QnA Pairs" button
- The system will process the document and generate questions and answers
- Preview the first 5 generated pairs

**Step 4: Translate & Export**
- Click "Translate to Hindi and Marathi" button
- The system will translate all QnA pairs to both languages
- Download the `Multilingual_QnA.xlsx` file

## Output Format

The generated Excel file (`Multilingual_QnA.xlsx`) contains three worksheets:

### English Sheet
| Questions | Answers |
|-----------|---------|
| Sample Question 1 | Sample Answer 1 |
| Sample Question 2 | Sample Answer 2 |

### Hindi Sheet
| Questions | Answers |
|-----------|---------|
| नमूना प्रश्न 1 | नमूना उत्तर 1 |
| नमूना प्रश्न 2 | नमूना उत्तर 2 |

### Marathi Sheet
| Questions | Answers |
|-----------|---------|
| नमूना प्रश्न 1 | नमूना उत्तर 1 |
| नमूना प्रश्न 2 | नमूना उत्तर 2 |

**Sheet Features:**
- 📌 Color-coded headers (Blue background, white text)
- 📏 Auto-sized columns (50 chars for questions, 60 chars for answers)
- 📝 Text wrapping for better readability
- 🔲 Cell borders for clear organization
- 📊 Professional formatting

## Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
OUTPUT_DIR=./output
```

## Module Documentation

### document_parser.py
Handles parsing of different document formats:
- `parse_pdf()`: Extract text from PDF files
- `parse_docx()`: Extract text from DOCX files
- `parse_txt()`: Extract text from TXT files
- `chunk_text()`: Split text into manageable chunks

### qna_generator.py
Generates QnA pairs using Google Generative AI:
- `generate_qna_from_text()`: Generate QnA from a single text
- `generate_qna_batch()`: Generate QnA from multiple text chunks
- Handles prompt engineering for optimal results

### translator.py
Translates content to different languages:
- `translate_text()`: Translate single text to target language
- `translate_qna_pairs()`: Translate entire QnA pairs
- Supports English, Hindi, and Marathi

### excel_exporter.py
Creates professionally formatted Excel files:
- `add_sheet()`: Add new worksheet with QnA pairs
- `create_multilingual_qna_file()`: Create complete multilingual file
- Automatic formatting and styling

## Troubleshooting

### Issue: "GOOGLE_API_KEY environment variable not set"
**Solution**: Enter your API key in the Streamlit interface, or set it in `.env` file and restart the app

### Issue: "Error parsing PDF"
**Solution**: Ensure the PDF is not corrupted and contains readable text (not scanned images)

### Issue: Translation is slow
**Solution**: This is normal for large documents. The system translates each QnA pair individually

### Issue: Limited API quota
**Solution**: Google Generative AI has usage limits. Check your API quota at [Google AI Studio](https://makersuite.google.com/)

## Requirements

See `requirements.txt` for complete list:
- **streamlit**: User interface framework
- **python-docx**: DOCX file parsing
- **pdfplumber**: PDF text extraction
- **openpyxl**: Excel file creation
- **google-generativeai**: Access to Gemini AI
- **googletrans**: Translation service
- **langchain**: LLM orchestration (optional)
- **python-dotenv**: Environment variable management

## API Usage

### Google Generative AI (Gemini)
- Free tier: Limited requests per minute
- Paid tier: Higher quotas and priority
- Cost: Check [Google AI pricing](https://ai.google.dev/pricing)

### Google Translate
- Uses free googletrans library
- No API key required
- Rate limiting applies

## Limitations

⚠️ **Known Limitations:**
- Maximum text extraction: Limited by API quotas
- Translation accuracy: Depends on Google Translate
- QnA quality: Depends on input document clarity
- Processing time: Larger documents take longer
- Language support: Currently limited to English, Hindi, Marathi

## Future Enhancements

🚀 **Potential Improvements:**
- Support for more file formats (XLSX, PPT, etc.)
- Additional language support
- Custom QnA filtering based on relevance
- Confidence scoring for generated QnA
- Batch processing of multiple documents
- Database storage for previous generations
- API endpoint for programmatic access

## License

This project is provided as-is for educational and commercial use.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the error messages carefully
3. Ensure all dependencies are installed correctly
4. Verify your Google API key is valid

## Development

### Running in Development Mode
```bash
streamlit run app.py --logger.level=debug
```

### Running Tests (if added)
```bash
pytest tests/
```

## Contributing

To contribute improvements:
1. Test your changes thoroughly
2. Update documentation
3. Ensure code follows PEP 8 style guide
4. Submit detailed pull requests

---

**Version**: 1.0.0  
**Last Updated**: March 2026  
**Status**: Production Ready
