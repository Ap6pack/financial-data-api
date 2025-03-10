from cachetools import TTLCache

# Cache setup: Store up to 100 items, with a time-to-live (TTL) of 5 minutes (300 seconds)
cache = TTLCache(maxsize=100, ttl=300)

def get_cached_data(key):
    """Retrieve data from cache if available."""
    return cache.get(key)

def set_cached_data(key, value):
    """Store data in cache."""
    cache[key] = value