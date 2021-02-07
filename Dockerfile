# ==================================================================
# fetching the official Docker Python image (slim version)
# ------------------------------------------------------------------
FROM python:3.9-slim-buster
# ==================================================================
# defining useful local variable
# ------------------------------------------------------------------
RUN APT_INSTALL="apt-get install -y --no-install-recommends" \
    && GIT_CLONE="git clone --depth 10" \
    && PIP_INSTALL="python3 -m pip --no-cache-dir install --upgrade -r" \
# ==================================================================
# installing git
# ------------------------------------------------------------------
    && apt-get update \
    && $APT_INSTALL git \
    && rm -rf /var/lib/apt/lists/* \
# ==================================================================
# cloning git repository and setting it as working directory
# ------------------------------------------------------------------
    && $GIT_CLONE \
    https://github.com/inverniz/Docker_exercise \
# ==================================================================
# installing python requirements
# ------------------------------------------------------------------
    && $PIP_INSTALL \
    Docker_exercise/requirements.txt
# ==================================================================
# starting server
# ------------------------------------------------------------------
WORKDIR /Docker_exercise/
ENTRYPOINT [ "python3", "server.py" ]
# ==================================================================
# exposing port 5000
# ------------------------------------------------------------------
EXPOSE 5000