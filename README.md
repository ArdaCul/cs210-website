# Musical Journey Analysis

Diving into my musical journey with data! 🎵 Investigating seasonal patterns in my Spotify plays to discover how my music taste evolves with the seasons. Are there melodies that harmonize with the weather? Let the data tell the tale! 🍂❄️🌷🌞 #DataScience #MusicAnalysis

## Motivation

The motivation behind this project was a personal curiosity to understand my music taste and how it evolves with the seasons. I aimed to gain insights into the patterns and variations in my listening habits.

## Data Source

The data for this analysis comes from Spotify, providing a detailed streaming history. I collected this data to explore the dynamics of my music preferences over time.

## Overview

This project explores the seasonal patterns in my Spotify listening history. The analysis includes insights into daily song counts, most-listened genres per season, and top 10 artists for each season. The project also features an interactive website that visually presents the findings with interactive charts and a unique music playback experience.

## Deployment

Please find the website deployed at the following url: [cs210-website.vercel.app](https://cs210-website.vercel.app/)

## Project Structure

The project is divided into several components:

1. **Data Collection and Analysis:**
   - Streaming history data from Spotify was collected and analyzed using Python.
   - Seasonal patterns, daily counts, and top genres and artists were extracted from the data.
   - The analysis involved the following stages and techniques:
     - **Data Collection:**
       - I started by requesting my streaming history from Spotify, which was downloaded in JSON format.
       - An online tool was used to extract genre information for each song.
     - **Data Preprocessing:**
       - The collected data was cleaned and processed using Pandas in Python.
       - Date and time information was converted, and new columns such as season, day, and duration were created.
     - **Exploratory Data Analysis (EDA):**
       - Various EDA techniques were applied to understand the distribution of song counts, artist preferences, and genres.
       - Seasonal patterns and daily listening habits were explored.
     - **Visualization:**
       - Matplotlib and Seaborn were utilized to create visualizations, including line charts, bar charts, and interactive elements.

2. **Interactive Website:**
   - The project includes an interactive NextJS 14 website showcasing the analysis results.
   - Notable features include:
     - **Daily Song Counts Line Chart:** Interactive chart displaying the daily song counts with mouse-over information.
     - **Most-Listened Genres Bar Chart:** Interactive bar chart showcasing the most-listened genres per season.
     - **Top 10 Listened Artists with Music Playback:** Interactive boxes displaying the top 10 listened artists for each season. Users can play and pause songs directly from the website.

## Getting Started

To run the analysis and explore the interactive website locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ArdaCul/cs210-website.git
   cd cs210-website
   npm install
   npm run dev
