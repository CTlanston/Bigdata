def compute_pagerank(damping_factor, iterations, lines):
    # Parse the input lines into (node, [neighbors]) pairs
    links = lines.map(lambda urls: urls.split(":"))\
                 .map(lambda url_neighbors: (url_neighbors[0], url_neighbors[1].split(",")))\
                 .cache()

    # Initialize each node with a rank of 1.0
    ranks = links.map(lambda url_neighbors: (url_neighbors[0], 1.0))

    def computeContribs(urls, rank):
        num_urls = len(urls)
        for url in urls:
            yield (url, rank / num_urls)

    for iteration in range(iterations):
        # Calculates URL contributions to the rank of other URLs.
        contribs = links.join(ranks).flatMap(
            lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))
        
        # Re-calculates URL ranks based on neighbor contributions.
        ranks = contribs.reduceByKey(lambda x, y: x + y).mapValues(lambda rank: rank * damping_factor + (1 - damping_factor))

    return ranks.collect()

# Read data from S3
lines = sc.textFile("s3://bigdata-hw7-lanston/page-rank.txt")

# Experiment with different damping factors and iterations
results_damping = {damping_factor: compute_pagerank(damping_factor, 1, lines) for damping_factor in [0.15, 0.50, 0.85]}
results_iterations = {iteration: compute_pagerank(0.85, iteration, lines) for iteration in [1, 5, 10, 20]}


# Convert results to DataFrames for better display
from pyspark.sql import Row
def results_to_dataframe(results):
    rows = [Row(damping_factor=df, node=k, rank=v) for df, ranks in results.items() for k, v in ranks]
    return spark.createDataFrame(rows)


# DataFrame for different damping factors
df_damping = results_to_dataframe(results_damping)
df_damping.show()

# DataFrame for different iterations
df_iterations = results_to_dataframe(results_iterations)
df_iterations.show()
