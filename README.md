# dmarc-visualizer

This is fork of - https://github.com/debricked/dmarc-visualizer

Forked and modified to work for my own personal projects

Analyse and visualize DMARC results using open-source tools.

* [parsedmarc](https://github.com/domainaware/parsedmarc) for parsing DMARC reports,
* [Elasticsearch](https://www.elastic.co/) to store aggregated data.
* [Grafana](https://grafana.com/) to visualize the aggregated reports.

## Screenshot

![Screenshot of Grafana dashboard](/big_screenshot.png?raw=true)

## Step-by-step

```
git clone https://github.com/debricked/dmarc-visualizer
cd dmarc-visualizer
docker-compose -f ./docker-compose.yml --verbose up
```