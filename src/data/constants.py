from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
# parent[2] goes up two levels to the root of the project
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
SENTIMENT_DIR = DATA_DIR / "sentiment"

GENOME_SCORES_FILE=RAW_DIR / "genome-scores.csv"
GENOME_TAGS_FILE=RAW_DIR / "genome-tags.csv"
LINKS_FILE=RAW_DIR / "links.csv"
MOVIES_FILE=RAW_DIR / "movies.csv"
RATINGS_FILE=RAW_DIR / "ratings.csv"
TAGS_FILE=RAW_DIR / "tags.csv"