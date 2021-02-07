# ==================================================================
# official Docker Python image, slim version
# ------------------------------------------------------------------
FROM python:3.9-slim-buster
RUN APT_INSTALL="apt-get install -y --no-install-recommends" && \
    GIT_CLONE="git clone --depth 10" && \
    PIP_INSTALL="python3 -m pip --no-cache-dir install --upgrade -r" && \
    apt-get update && \
    $APT_INSTALL git && \
# ==================================================================
# cloning git repository
# ------------------------------------------------------------------
    $GIT_CLONE && \
    https://github.com/inverniz/Docker_exercise
# ==================================================================
# installing python requirements
# ------------------------------------------------------------------
    $PIP_INSTALL \
    requirements.txt
# ==================================================================
# starting server
# ------------------------------------------------------------------
ENTRYPOINT [ "python3", "server.py" ]
EXPOSE 5000