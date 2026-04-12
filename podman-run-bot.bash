podman build --no-cache --rm --volume $(pwd)/data:/home/deltachat/bot -f Containerfile -t deltachatbot:test .
podman run --interactive --tty --volume $(pwd)/data:/home/deltachat/bot deltachatbot:test
