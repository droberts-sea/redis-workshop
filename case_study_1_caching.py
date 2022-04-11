import argparse
import json
import redis
import time

def make_expensive_api_call(key):
  print(f"Making expensive API call for key {key}...")
  time.sleep(3)
  return {
    "key": key,
    "price": 12.34,
    "description": "maybe some product details or something",
  }

CACHE_DURATION = 60 * 15 # 15 minutes, in seconds
def api_call_with_cache(key):
  redis_client = redis.Redis(host='localhost', port=6379)

  result = None
  try:
    # Attempt to read from Redis
    result_bytes = redis_client.get(key)
    if result_bytes is None:
      raise
    result = json.loads(result_bytes)
  except:
    # Fall back to original API
    result = make_expensive_api_call(key)
    redis_client.set(key, json.dumps(result), ex=CACHE_DURATION)
  
  return result

def main():
  parser = argparse.ArgumentParser(description='Demo of caching with Redis')
  parser.add_argument('--key', required=True, help='key to look up')
  args = parser.parse_args()

  result = api_call_with_cache(args.key)
  print(f"Loaded data: '{result}'")

if __name__ == '__main__':
  main()