# FortuneTeller

## Command Reference

### Build the image

```bash
docker build -t fortuneteller .
```

### Build the container

```bash
docker run -p 5000:5000 --rm --name fortuneteller-container fortuneteller
```