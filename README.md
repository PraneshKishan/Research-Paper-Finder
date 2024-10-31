# Research-Paper-Finder

This Research Paper Finder app helps users quickly find research papers on specific topics by scraping Google Scholar based on user-provided search tags. It retrieves titles, abstracts, and links to relevant papers, making it easier for researchers, students, and enthusiasts to discover academic resources.

## Features

- **Keyword-Based Search**: Enter search keywords or tags to find related research papers.
- **Quick Results**: Retrieves relevant titles, abstracts, and links to papers in real-time.
- **User-Friendly Interface**: Simple and intuitive Streamlit interface for easy use.

## Project Structure

- **`app.py`**: The main application file, built using Streamlit, where users can input search tags and view the results.
- **`scrape_papers` function**: A helper function that performs the web scraping on Google Scholar, processes the HTML to extract titles, abstracts, and links, and returns them as a list of dictionaries.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/research-paper-finder.git
   cd research-paper-finder
Install dependencies: This app requires Streamlit, requests, and BeautifulSoup4:
  'pip install streamlit requests beautifulsoup4'


#To run the code
  'streamlit run app.py'
  Open your browser and go to http://localhost:8501 to use the app.

#Usage
- Enter the search tags in the input box (e.g., "machine learning in healthcare").
- Press the Search button to fetch related research papers.
- The app will display a list of paper titles, abstracts, and links.
