def discover_original_price(sp, d):
    return round(sp / (100 - d) * 100, 2)
