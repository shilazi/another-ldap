# Production-Ready Image

If used in production, use proxy with `https` and set `COOKIE_SECURE` to `True`.

## Change Log

- Replace image with `METADATA_IMAGE`
- Replace cookie name with `COOKIE_NAME`
- Switch cookie secure with `COOKIE_SECURE`
- Support `protocol` and `callback` query params of `/logout` route
- Support `SCRIPT_NAME` for serving under a subpath
- Bookworm based container image with `gunicorn` 

## Run With Docker

```bash
cd deploy/docker

docker compose up
```

# Run With Kubernetes

Note: when kubernetes version `>=` 1.22, `ingress.yaml` need set `spec.ingressClassName`.

```bash
cd deploy/kubernetes

kubectl apply -f .
kubectl apply -f whoami/
```