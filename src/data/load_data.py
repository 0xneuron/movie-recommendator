from src.data import *

import pandas as pd

def load_movies():
    return pd.read_csv(MOVIES_FILE)

def load_ratings():
    return pd.read_csv(RATINGS_FILE)    

def load_tags():
    return pd.read_csv(TAGS_FILE)

def load_links():
    return pd.read_csv(LINKS_FILE)

def load_genome_scores():
    return pd.read_csv(GENOME_SCORES_FILE)

def load_genome_tags():
    return pd.read_csv(GENOME_TAGS_FILE)

def load_all_data():
    movies = load_movies()
    ratings = load_ratings()
    tags = load_tags()
    links = load_links()
    genome_scores = load_genome_scores()
    genome_tags = load_genome_tags()

    return {
        "movies": movies,
        "ratings": ratings,
        "tags": tags,
        "links": links,
        "genome_scores": genome_scores,
        "genome_tags": genome_tags
    }