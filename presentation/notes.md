# Redis Workshop

Thursday April 14, 2022

## Outline

What is Redis
- Name
  - Redis like "red"
  - "Remote Dictionary Service"
- What problem does it solve
- How can you tell you're looking at a Redis problem
- What problems doesn't it solve
  - Don't use it as your primary data store
  - Don't EVER put PII / PCI data in redis
- Comparison with Dynamo
  - Redis
    - In-memory first
    - Pros
      - Better perf (sub-millisecond)
      - Great primitives around caching (LRU / LFU eviction, TTL, etc)
    - Cons
      - Persistence is point-in-time snapshot + append-only log, so recovery from crash or restart can be slow / painful
      - Whole dataset has to fit in RAM -> $$$$$
      - Requires management to scale (though cloud providers e.g. AWS elasticache will do this for you)
      - Less support for encryption, compliance stuff
        - [Elasticache claims to be PCI compliant](https://aws.amazon.com/about-aws/whats-new/2018/07/amazon-elasticache-for-redis-is-now-pcidss-compliant/)
  - DynamoDB
    - On-disk first
    - Pros
      - Persistence by default, no downtime
      - Compliance features (versioning / WORM / encryption)
      - Fully managed
      - Scales infinitely (size and throughput)
    - Cons
      - Worse perf (<10 ms)
      - Can struggle with write-heavy workflows
      - No caching primitives
      - Locked into AWS



Using Redis
- Docker
- In the cloud (AWS elasticache)

Case Studies

Papering over a flakey dependency
- Scenario:
  - E-commerce website
  - Relatively large scale, distributed application
  - Get product prices / descriptions from a distributor's API
    - API is usually fast but unreliable.
      - Downtime / latency spikes.
      - Or, maybe it's expensive, or we're getting throttled, or we only use 1% of the data they send back.
    - Need data for every page load
    - Prices / descriptions are relatively stable
    - Access patterns follow a power law, 80/20 distro
- Options:
  - Save product data to your database
    - Need to implement caching primitives (expiration, etc) yourself
    - Taking up valuable space in your DB!
    - Slow
  - Implement an in-memory cache as part of the app
    - Lots of work, lots of bugs
    - Node spin-up is problematic, has to populate cache
  - Redis
    - Check cache before making API call
    - Automatic TTL / LRU eviction
    - Shared by all nodes, so no spin-up problem
      - Probably want point-in-time backups so Redis itself can recover quickly

HTTP Replay Cache

Most purchased products page

Takeaways
- All high-throughput distributed systems problems.
- Redis is never authoritative, just a fast caching layer. If you lose the Redis data it's not a huge problem.


References
- https://ibrahimcesar.cloud/blog/redis-exploring-redis-as-serverless-databases-to-solve-idempotence-in-api-upstash/
- https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/
- https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- https://aws.amazon.com/elasticache/pricing/?nc=sn&loc=5
- https://severalnines.com/database-blog/redis-vs-dynamodb-comparison
- https://medium.com/gumgum-tech/migrating-from-elasticache-for-memcached-to-dax-dynamodb-accelerator-ebc4677ee68e
- https://www.digitalocean.com/community/cheatsheets/how-to-manage-redis-databases-and-keys