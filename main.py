import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape research papers
def scrape_papers(search_query):
    search_query = search_query.replace(' ', '+')
    url = f"https://scholar.google.com/scholar?q={search_query}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    papers = []
    for result in soup.select('.gs_ri'):
        title = result.select_one('.gs_rt').text
        link = result.select_one('.gs_rt a')['href'] if result.select_one('.gs_rt a') else "No link available"
        abstract = result.select_one('.gs_rs').text if result.select_one('.gs_rs') else "No abstract available"
        papers.append({'title': title, 'abstract': abstract, 'link': link})

    return papers

# Streamlit app
st.title("Research Paper Finder")
st.write("Enter search tags to find research papers")

# User input
search_tags = st.text_input("Search Tags", placeholder="e.g., machine learning in healthcare")

if st.button("Search"):
    if search_tags:
        with st.spinner('Searching...'):
            results = scrape_papers(search_tags)
            if results:
                st.write(f"Found {len(results)} papers:")
                for i, paper in enumerate(results):
                    st.write(f"**{i+1}. {paper['title']}**")
                    st.write(f"[Link]({paper['link']})")
                    st.write(f"**Abstract:** {paper['abstract']}\n")
            else:
                st.write("No papers found. Please try different search tags.")
    else:
        st.write("Please enter search tags to search for research papers.")

