
# Whatsapp Chat Analyzer

This is a Machine Learning project that takes the exported chat as an input and gives the graphical and theoretical analysis of the whole chat. It gives the details of both the whole group and individual users as well.


## Tech Stack

**Client:** Python

**Libraries:** Streamlit, Seaborn, WordCloud, Pandas, Emoji, URLExtract, Counter, Matplotlib

## Installation

Clone the repository https://github.com/taha-ahmad2002/ChatAnalyzer.git
```bash
# install the libraries using:
    pip install streamlit seaborn wordcloud pandas emoji urlextract matplotlib
```
## Features

- Total words, messages, shared links, media shared
- Monthly and Daily Timeline (Linear graph)
- Activity Map - Most Busy day, Most Busy month (Bar chart)
- Weekly Activity Map (Heatmap)
- Most Busy Users (Bar chart and tables)
- Word Cloud
- Most Common Words (Bar chart)
- Emoji Analysis (Number of emojis using table and pie chart)



## Screenshots

![App Screenshot](https://github.com/taha-ahmad2002/ChatAnalyzer/blob/master/screenshots/Screenshot%202026-03-07%20133110.png?raw=true)

![App Screenshot](https://github.com/taha-ahmad2002/ChatAnalyzer/blob/master/screenshots/Screenshot%202026-03-07%20133144.png?raw=true)

![App Screenshot](https://github.com/taha-ahmad2002/ChatAnalyzer/blob/master/screenshots/Screenshot%202026-03-07%20133156.png?raw=true)

![App Screenshot](https://github.com/taha-ahmad2002/ChatAnalyzer/blob/master/screenshots/Screenshot%202026-03-07%20133204.png?raw=true)
## Run Locally

Clone the project:

```bash
  git clone https://github.com/taha-ahmad2002/ChatAnalyzer.git
```
Create a python virtual enviroment:

```bash
  python -m venv myenv
```

Activate the virtual enviroment:

```bash
  myenv\Scripts\activate
```

Install dependencies:

```bash
  pip install streamlit seaborn wordcloud pandas emoji urlextract matplotlib
```

Start the server:

```bash
  streamlit run app.py
```

Select exported chat after pressing "Browse Files" and then press "Analyze"
## Feedback

If you have any feedback, please reach out to us at ahmad.taaha2002@gmail.com


## Deployment

The project is deployed on:

```bash
  https://chatanalyzergit-qlf48raowkk7tyb6tdmqqb.streamlit.app/
```
This project is deployed on streamlit but it's not a paid feature so to use the deployed project, we have to wake it up everytime.

