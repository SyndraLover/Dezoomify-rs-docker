# Dezoomify-rs-docker
**This Repository is only meant for Artists and Humans who appreciate Art by Artists.** 
- Dezoomify-rs 2.18.1 inside debian container with a python wrapper.
- always downloads 8k if available
- can set to download largest if ALWAYS_LARGEST=True in evironment
- use with [gluetun](https://github.com/qdm12/gluetun) if you download in bulk. 

## Usage
- Docker as your user, omit user if necessary
```sh 
    docker run --user $(id -u):$(id -g) -v dezoomify_imports:/app/import -v /path/to/gallery:/app/export -p 9420:9420 -d ghcr.io/syndralover/dezoomify-rs:latest
```
- Docker Compose
```sh
git clone https://github.com/SyndraLover/Dezoomify-rs-docker.git
cd Dezoomify-rs-docker
docker-compose up -d
```

## for single links
- Via Curl
```sh
curl -X POST "http://dezoomify-rs.host:9420" -H "Content-Type: application/json" -d '{"link" : "https://artsandculture.google.com/asset/{name}/{jumble}"}'
```
- Via python request from this repository
```sh
python request.py http://server.ip:9420 https://artsandculture.google.com/asset/{name}/{jumble}
```

## Bulkmode
```sh
curl http://server.ip:9420
```

What is a *curl*??? Open your browser and enter `http://server.ip:9420`, press enter a few times to make sure <3

if you are using portainer you can upload files with links in them to dezoomify_imports volume from the UI.
You can mount the path directly. !!!WARNING!!! all files inside the import directory will be deleted to avoid duplicates. Pass a directory directly at your own risk.

Currently there is no simple way of obtaining the right links. if you find a way or know of a way please add them to the scraping_the_scrapists directory as a simple file and name them. <3

## Known issues
Deleting files is dumb.

## Legality
Famously what is legal must be moral and what is illegal must be immoral. THIS IS NOT LEGAL ADVICE!

## References
- https://github.com/lovasoa/dezoomify-rs
- https://github.com/qdm12/gluetun

## License
Inherits GPL-3.0 of [Dezoomify-rs](https://github.com/lovasoa/dezoomify-rs)