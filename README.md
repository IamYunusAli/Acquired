## Installation

### Creating a Virtual Environment

#### Using Virtualenv

Using `venv`, Python's built-in virtual environment module:

1. Open your terminal or command prompt.

2. Navigate to your project directory.

3. Run the following command to create a new virtual environment:

   ```bash
   python -m venv your_env_name
   ```

   Replace `your_env_name` with the desired name for your environment.

4. Activate the environment:

   - On Windows:

   ```bash
   .\your_env_name\scripts\activate
   ```

   - On macOS/Linux:

   ```bash
   source your_env_name/bin/activate
   ```

Now, your virtual environment is created and activated. You can clone and run it on vevn

### Project Planning - EDA & Stats

### Task done

Descriptive Statistics
Text Analysis(Sentiment analysis & Topic Modeling):
Time Series Analysis
Publisher Analysis

### Folder Structure:

<pre>
├── .vscode
│ └── settings.json
├── .github
   └── workflows
     ├── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── notebooks
   ├──data/
         ......     
   ├── Company_analysis.ipynb
   ├── __init__.py
   └── README.md
└── scripts
   ├── __init__.py
   ├── README.md
└── src
  ├── __init__.py
└── README.md
</pre>

**Author:** Yunus A. Hassen
