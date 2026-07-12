# Problem: A blog platform needs to associate tags with articles. Each article can have multiple tags, but tags should be unique for a given article. We also want to easily find all unique tags used across all articles.

# Analysis:

# We need to store a collection of tags for each article.
# Tags must be unique per article.
# We might need to perform operations like finding common tags between articles or getting a list of all unique tags used site-wide.
# Best Data Structure: Set (for individual articles) and potentially a Set (for site-wide unique tags)

# For individual articles: A set is perfect for storing the tags associated with a single article because it automatically handles uniqueness.

# For site-wide unique tags: A set can be used to aggregate all tags and find the unique one


# Tags for Article 1
article1_tags = {"python", "backend", "webdev", "programming", "python"} # Duplicate 'python' is ignored


# Tags for Article 2
article2_tags = {"javascript", "frontend", "webdev", "react"}

# Tags for Article 3
article3_tags = {"python", "data science", "machine learning"}

print(f"Article 1 Tags: {article1_tags}")
print(f"Article 2 Tags: {article2_tags}")
print(f"Article 3 Tags: {article3_tags}")

# Finding common tags between Article 1 and Article 2 (Intersection)
common_tags_1_2 = article1_tags.intersection(article2_tags)
print(f"Common tags between Article 1 and 2: {common_tags_1_2}") # {'webdev'}

# Finding all unique tags used across all articles (Union)
all_tags_set = set()
all_tags_set.update(article1_tags)
all_tags_set.update(article2_tags)
all_tags_set.update(article3_tags)

print(f"All unique tags used: {all_tags_set}")

# You could also use the union operator iteratively or with multiple sets:
# all_tags_set_alt = article1_tags | article2_tags | article3_tags
# print(f"All unique tags (alternative): {all_tags_set_alt}")
