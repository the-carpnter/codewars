def most_frequent_item_count(collection):
    return max(map(collection.count, collection)) if collection else 0
