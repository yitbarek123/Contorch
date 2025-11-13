import docker
import os

# Initialize Docker client (Docker must be installed inside the orchestrator container)
client = docker.from_env()

