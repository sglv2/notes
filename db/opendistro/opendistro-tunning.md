# Local tests
Start local instance
```
docker run --rm -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" amazon/opendistro-for-elasticsearch:latest
```

Export cluster settings, including defaults
```
# GET _cluster/settings?include_defaults
curl -sk -u admin:admin https://localhost:9200/_cluster/settings?include_defaults | jq . > original-settings.json
```

# Disk based shard allocation
[Disk based shard allocation documentation] (https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-cluster.html#disk-based-shard-allocation)

## cluster.routing.allocation.disk.threshold_enabled
threshold_enabled must be true to enable the disk allocation decider.
```
cat original-settings.json | jq -r '.defaults.cluster.routing.allocation.disk.threshold_enabled'
```
## cluster.routing.allocation.disk.watermark
```
cat original-settings.json | jq -r '.defaults.cluster.routing.allocation.disk.watermark'
```
### low
`cluster.routing.allocation.disk.watermark.low`
Elasticsearch will not allocate shards to nodes where disk usage exceeds this threshold (default %)
This setting has no effect on the primary shards of newly-created indices but will prevent their replicas from being allocated.

### high
`cluster.routing.allocation.disk.watermark.high`
Elasticsearch will try to relocate shards from nodes where disk usage exceeds this threshold (default 90%).

### flood_stage
`cluster.routing.allocation.disk.watermark.flood_stage`
Enforces a `read_only_allow_delete` on every index on a node where at least one disk is exceeding this threshold (default 95%)

## Get disk usage
```
# GET _cat/allocation?format=json
curl -sk -u admin:admin -X GET 'https://localhost:9200/_cat/allocation?format=json&bytes=mb' | jq .
```

## Updating disk based shard allocation configuration
```
# PUT _cluster/settings
curl -X PUT https://localhost:9200/_cluster/settings \
  -sk -u admin:admin \
  -H 'Content-Type: application/json' \
  -d'
  {
    "persistent": {
      "cluster.routing.allocation.disk.watermark.low": "80%",
      "cluster.routing.allocation.disk.watermark.high": "85%"
    }
  }'
```