# LinkedIn Post Generator for Data Scientists (Using Groq API)

## Overview
This project is designed to help data scientists generate LinkedIn posts quickly and efficiently using the **Groq API**. The tool utilizes **Streamlit** for an interactive user interface and leverages **few-shot learning** techniques to guide the language model in producing high-quality LinkedIn posts.

## Features
- Interactive web interface powered by **Streamlit**.
- Uses **Groq API** for natural language generation.
- Implements **few-shot learning** for improved text generation.
- Supports **preprocessing and reformatting** of JSON data.
- Customizable post structure to fit LinkedIn's best practices.

## Installation
Ensure you have Python installed (preferably Python 3.8+). Then, clone this repository and install the required dependencies:

```sh
# Clone the repository
git clone https://github.com/SHIVOGOJOHN/LinkedIn-Post-Generator-For-Data-Scientists-With-Groq-API.git
cd LinkedIn-Post-Generator-For-Data-Scientists-With-Groq-API

# Install dependencies
pip install -r requirements.txt
```

## Usage
Run the application using Streamlit:

```sh
streamlit run app.py
```

Once launched, you can enter your topic or key points, and the tool will generate a well-structured LinkedIn post.

## File Structure
```
.
├── .streamlit/            # Streamlit configuration files
├── app.py                 # Main application script
├── few_shot.py            # Implements few-shot learning examples
├── llm.py                 # Handles Groq API interactions
├── post_generator.py      # Core logic for post generation
├── preprocess.py          # Preprocessing functions for input data
├── ReformatJson.py        # JSON reformatting utilities
├── jsononline-net.json    # Example input JSON
├── preprocessed.json      # Preprocessed JSON data
├── reformatted_json.json  # Reformatted JSON data
├── requirements.txt       # Dependencies list
└── README.md              # Project documentation
```

## Dependencies
All required Python packages are listed in `requirements.txt`. Key dependencies include:

```plaintext
streamlit
requests
```



