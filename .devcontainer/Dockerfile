FROM mcr.microsoft.com/devcontainers/python:3.14-bookworm

USER vscode
WORKDIR /workspace

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/home/vscode/.local/bin:${PATH}" \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1

CMD ["sleep", "infinity"]
