# Docker

## Docker Commands

```bash
docker build --platform linux/amd64 -t maxharp3rsubmittable/getting-started .

docker run -dp 3000:3000 getting-started
docker stop 394f1787e52b

docker ps
docker image ls

docker tag repo/name:1 foo.azurecr.io/repo/name:1

docker push maxharp3rsubmittable/getting-started

# clean up
docker image prune
docker image prune -a
docker container prune

```

## Docker Compose Commands

```bash
docker compose up -d

docker compose logs -f
docker compose logs -f app
```

Using docker compose with multiple Dockerfiles:
<https://stackoverflow.com/a/48243640/293087>

## Docker Contexts

<https://serverfault.com/questions/1128587/change-the-docker-context-in-docker-desktop>

```sh
docker context ls

docker context use docker-test
```

## Building on Apple Hardware (for linux)

When running `docker build`, include `--platform linux/amd64`

via <https://stackoverflow.com/a/68004485/293087>
