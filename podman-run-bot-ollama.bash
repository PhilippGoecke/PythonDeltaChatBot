podman build --no-cache --rm --volume $(pwd)/data:/home/deltachat/data/ -f Containerfile.Ollama -t deltachatbot:ollama .
podman run --interactive --tty --env OLLAMA_HOST=http://host.containers.internal:11434 --env OLLAMA_MODEL=gemma4:31b --volume $(pwd)/data:/home/deltachat/data/ deltachatbot:ollama
