# locust-newrelic-sidecar

![](https://github.com/albertowar/locust-newrelic-sidecar/workflows/Build/badge.svg)
![](https://github.com/albertowar/locust-newrelic-sidecar/workflows/Release/badge.svg)

Sidecar to push Locust statistics to NewRelic as events.

## Requirements
The minimum requirement to build and run this locally are:
- Docker and `docker-compose`.
- Python 3 (and pip).
- **Optional**: pycodestyle (if you want to run the linter)

## Development
Once you have cloned the repository, the `Makefile` provides you with a few shortcuts to facilitate the development flow:
- `lint`: runs the linter on the `srs` folder.
- `image`: builds the image.
- `run`: runs the image alongside of a Locust standalone instance.
- `cleanup`: stops and removes the containers.

## Folder structure
TBD

## FAQ
### Why did I create this tool?
[Locust](http://locust.io/) is a pretty solid open source load testing tool which enables the user to run distributed load tests using simple Python scripts to describe the scenarios.

Although its web interface has a few charts to display the test results in real-time, it has a couple of drawbacks:
- The charts are not persisted over time. Therefore, if the browser loses connection to Locust or you accidentally refresh the page, the results of the test until that point will be lost.
- The web interface focuses on displaying information for the generic use case (latency, error rate, rps), but it doesn't support more complex data visualizations (statistics per endpoint, error rate per status code, etc).

There are many alternatives that could help to solve this problem out there, however I decided to use NewRelic it is one of the most polular monitoring solutions in the industry.

With that being said, I am open to contributions that add integrations with other monitoring solutions or other improvements.

### Why not creating a library instead?
