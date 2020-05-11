# locust-newrelic-sidecar

![](https://github.com/albertowar/locust-newrelic-sidecar/workflows/Master%20Build/badge.svg)
![](https://github.com/albertowar/locust-newrelic-sidecar/workflows/PR%20Build/badge.svg)

Sidecar to push Locust statistics to NewRelic as events.

## Requirements
The minimum requirement to build and run this locally are:
- Docker and `docker-compose`.
- Python 3 (and pip).
- **Optional**: pycodestyle (if you want to run the linter)

## Usage
TBD

## Development
Once you have cloned the repository, the `Makefile` provides you with a few shortcuts to facilitate the development flow:
- `lint`: runs the linter on the `srs` folder.
- `image`: builds the image.
- `run`: runs the image alongside of a Locust standalone instance.
- `cleanup`: stops and removes the containers.

## Folder structure
TBD

## Contribute
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
Both approaches (library vs separate container) would work but they come with advantages/disadvantages.

Using a library integrated as part of the `locustfile` (test script) would enable the NewRelic agent to push APM (CPU, Memory, etc) as well as the events which could facilitate troubleshooting of Locust performance issues if they arise.

However, this approach has some disadvantages:
* Dependency conflicts between Locust and the library.
* Monitoring library impacting the performance of Locust by taking too much memory/CPU/network resources.
* The added cost of adding APM.

In reality, you are probably going to need APM when you are integrating Locust for the first time with your infrastructure. Once you have gone through the initial tweaking phase, you will undestand well what's required for Locust to run efficiently in your environment and you will rarely look again in APM.

Using a separate container would allow us to:
* Avoid dependency issues. Since it runs on a separate container, we could even use a different programming language!
* Avoid taking stealing away compute/network resources.

This option on the other hand will prevent us from analysing any performance issues Locust might be struggling with.

With all that being said, I decided to go for the latter because I already have enough understanding of the framework. In the future, if people are interested, we could bundle the core functionality into a separate package and publish it into PyPI.
