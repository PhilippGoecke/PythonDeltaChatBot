podman build --no-cache --rm --volume $(pwd)/data:/home/deltachat/data/ -f Containerfile -t deltachatbot:test .
podman run --interactive --tty --volume $(pwd)/data:/home/deltachat/data/ deltachatbot:test
