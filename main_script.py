import yaml
from bertopic import BERTopic
from bertopic.representation import MaximalMarginalRelevance
from bertopic.vectorizers import ClassTfidfTransformer
from umap import UMAP
from hdbscan import HDBSCAN
from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer
from utils.preprocess import load_data, get_tokenizer_and_stopwords

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

def run_bertopic(country, inbody):
    params = config[country]

    # Step 1 - Extract embeddings
    embedding_model = SentenceTransformer(params["embedding_model"])

    # Step 2 - Reduce dimensionality
    umap_model = UMAP(**params["umap_params"])

    # Step 3 - Cluster reduced embeddings
    hdbscan_model = HDBSCAN(**params["hdbscan_params"])

    # Step 4 - Tokenize topics
    tokenizer, stop_words = get_tokenizer_and_stopwords(params["vectorizer_params"])
    vectorizer_model = CountVectorizer(tokenizer=tokenizer, stop_words=stop_words, ngram_range=tuple(params["vectorizer_params"]["ngram_range"]))

    # Step 5 - Create topic representation
    ctfidf_model = ClassTfidfTransformer()
    representation_model = MaximalMarginalRelevance(diversity=params["topic_representation_param"]["diversity"])

    # Initialize BERTopic with country-specific parameters
    topic_model = BERTopic(
        embedding_model=embedding_model,
        umap_model=umap_model,
        hdbscan_model=hdbscan_model,
        vectorizer_model=vectorizer_model,
        ctfidf_model=ctfidf_model,
        representation_model=representation_model,
        **params["topic_params"]  # Apply additional topic parameters directly
    )

    topics, probs = topic_model.fit_transform(inbody)
    print(f"Topics for {country}: {topics}")

# Example call
inbody = load_data("India")  # Replace "India" as needed
run_bertopic("India", inbody)

