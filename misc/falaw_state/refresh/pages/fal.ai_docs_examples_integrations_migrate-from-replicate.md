> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate from Replicate

> This guide will help you transition from using [Replicate](https://replicate.com/)'s tools, specifically their [Cog](https://github.com/replicate/cog) tool, to fal's platform. Cog is a tool used to package machine learning models in Docker containers, which simplifies the deployment process.

## Step 1: Generate the Dockerfile with Cog

First, ensure you have Cog installed. If not, follow the instructions on the [Cog GitHub page](https://github.com/replicate/cog).

Navigate to your project directory and run:

```bash theme={null}
cog debug > Dockerfile
```

This command will generate a `Dockerfile` in the root of your project.

## Step 2: Adapt the Dockerfile for fal

With your `Dockerfile` generated, you might need to make a few modifications to ensure compatibility with fal.

First, we need to extract Python dependencies and install them in the Docker image. We can do this by copying the dependencies from the Cog file to the Docker image. Here's an example of how you can do this:

<Warning>
  **Requirements**

  The following command assumes you have `yq` installed. If not, you can install it using `pip install yq`.
  Or follow the instructions on the [yq GitHub page](https://github.com/mikefarah/yq).

  You might also need to install `jq` if you don't have it installed. e.g. You can install it using `sudo apt-get install jq` if you are using a Debian-based system. Alternatively, check out the [jq GitHub page](https://github.com/jqlang/jq).
</Warning>

```bash theme={null}
yq -e '.build.python_packages | map(select(. != null and . != "")) | map("'"'"'" + . + "'"'"'") | join(" ")' cog.yaml
```

This will give you a list of Python packages that you can install in your Docker image. Using `RUN pip install ...` in your Dockerfile.

<Info>
  **e.g.**

  'torch' 'torchvision' 'torchaudio' 'torchsde' 'einops' 'transformers>=4.25.1' ...
</Info>

Alternatively, you can write the contents of the `python_packages` to a `requirements.txt` file and install them in the Dockerfile. See the example in [the containerized application page](/serverless/development/use-custom-container-image).

Here's a basic example of what your `Dockerfile` might look like:

<Info>
  The example Cog project is [https://github.com/fofr/cog-comfyui](https://github.com/fofr/cog-comfyui).
</Info>

```bash theme={null}
FROM python:3.10.6 as deps
COPY .cog/tmp/build4143857248/cog-0.0.1.dev-py3-none-any.whl /tmp/cog-0.0.1.dev-py3-none-any.whl  # [!code --]
RUN --mount=type=cache,target=/root/.cache/pip pip install -t /dep /tmp/cog-0.0.1.dev-py3-none-any.whl # [!code --]
COPY .cog/tmp/build4143857248/requirements.txt /tmp/requirements.txt # [!code --]
RUN --mount=type=cache,target=/root/.cache/pip pip install -t /dep -r /tmp/requirements.txt # [!code --]
RUN --mount=type=cache,target=/root/.cache/pip pip install -t /dep 'torch' 'torchvision' 'torchaudio' 'torchsde' 'einops' 'transformers>=4.25.1' 'safetensors>=0.3.0' 'aiohttp' 'accelerate' 'pyyaml' 'Pillow' 'scipy' 'tqdm' 'psutil' 'spandrel' 'kornia>=0.7.1' 'websocket-client==1.6.3' 'diffusers>=0.25.0' 'albumentations==1.4.3' 'cmake' 'imageio' 'joblib' 'matplotlib' 'pilgram' 'scikit-learn' 'rembg' 'numba' 'pandas' 'numexpr' 'insightface' 'onnx' 'segment-anything' 'piexif' 'ultralytics!=8.0.177' 'timm' 'importlib_metadata' 'opencv-python-headless>=4.0.1.24' 'filelock' 'numpy' 'einops' 'pyyaml' 'scikit-image' 'python-dateutil' 'mediapipe' 'svglib' 'fvcore' 'yapf' 'omegaconf' 'ftfy' 'addict' 'yacs' 'trimesh[easy]' 'librosa' 'color-matcher' 'facexlib' # [!code ++]
FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/x86_64-linux-gnu:/usr/local/nvidia/lib64:/usr/local/nvidia/bin
ENV NVIDIA_DRIVER_CAPABILITIES=all
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked set -eux; \
apt-get update -qq && \
apt-get install -qqy --no-install-recommends curl; \
rm -rf /var/lib/apt/lists/*; \
TINI_VERSION=v0.19.0; \
TINI_ARCH="$(dpkg --print-architecture)"; \
curl -sSL -o /sbin/tini "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-${TINI_ARCH}"; \
chmod +x /sbin/tini
ENTRYPOINT ["/sbin/tini", "--"]
ENV PATH="/root/.pyenv/shims:/root/.pyenv/bin:$PATH"
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked apt-get update -qq && apt-get install -qqy --no-install-recommends \
	make \
	build-essential \
	libssl-dev \
	zlib1g-dev \
	libbz2-dev \
	libreadline-dev \
	libsqlite3-dev \
	wget \
	curl \
	llvm \
	libncurses5-dev \
	libncursesw5-dev \
	xz-utils \
	tk-dev \
	libffi-dev \
	liblzma-dev \
	git \
	ca-certificates \
	&& rm -rf /var/lib/apt/lists/*
RUN curl -s -S -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash && \
	git clone https://github.com/momo-lab/pyenv-install-latest.git "$(pyenv root)"/plugins/pyenv-install-latest && \
	pyenv install-latest "3.10.6" && \
	pyenv global $(pyenv install-latest --print "3.10.6") && \
	pip install "wheel<1"
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked apt-get update -qq && apt-get install -qqy ffmpeg && rm -rf /var/lib/apt/lists/*
RUN --mount=type=bind,from=deps,source=/dep,target=/dep \
    cp -rf /dep/* $(pyenv prefix)/lib/python*/site-packages; \
    cp -rf /dep/bin/* $(pyenv prefix)/bin; \
    pyenv rehash
RUN curl -o /usr/local/bin/pget -L "https://github.com/replicate/pget/releases/download/v0.8.1/pget_linux_x86_64" && chmod +x /usr/local/bin/pget
RUN pip install onnxruntime-gpu --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-cuda-12/pypi/simple/
# fal platform will inject the necessary mechanisms to run your application. // [!code ++]
WORKDIR /src # [!code --]
EXPOSE 5000 # [!code --]
CMD ["python", "-m", "cog.server.http"] # [!code --]
COPY . /src # [!code --]
```

And that's it! 🎉

Ensure all dependencies and paths match your project's requirements.

## Step 3: Deploy on fal

fal supports deploying Docker-based applications easily. Follow these steps to deploy your Docker container on fal:

1. **Create an account on fal**: If you haven't already, sign up at [fal](https://fal.ai).

2. **Create a new project**: In your favorite directory, create a new project and move the `Dockerfile` into it. Create a new Python file with the following content:

```python theme={null}
import fal

from fal.container import ContainerImage
from pathlib import Path

PWD = Path(__file__).resolve().parent


class MyApp(fal.App):
	image = ContainerImage.from_dockerfile(f"{PWD}/Dockerfile")

	def setup(self):
		...

	@fal.endpoint("/")
	def predict(self, input: Input) -> Output:
		# Rest is your imagination.
```

<Note>
  **Converting your app/server**

  On a serious note, you need to do a little bit of conversion to run your
  application. But don't get intimidated, it's just a few lines of code. The
  structure is of cog server and fal apps are similar, so you can easily adapt
  your application to run on fal.
</Note>

You can see details documentation on how to use fal SDK [here](/serverless).

More information on how to deploy a containerized application can be found [here](/serverless/development/use-custom-container-image).

## Step 4: Test Your Deployment

Once deployed, ensure that everything is working as expected by accessing your application through the URL provided by fal. Monitor logs and performance to make sure the migration was successful.

## Troubleshooting

If you encounter any issues during the migration, check the following:

* **Dependencies**: Ensure all required dependencies are listed in your `requirements.txt` or equivalent file.
* **Environment Variables and Build Arguments**: Double-check that all necessary environment variables and build arguments are set correctly in your Dockerfile.
* **Logs**: Use the logging features in fal to diagnose any build or runtime issues.

For further assistance, refer to the [fal Documentation](#) or reach out to the fal support team.

## Conclusion

Migrating from Replicate to fal can be smooth with proper preparation and testing. This guide provides a straightforward path, but each project may have unique requirements. Adapt these steps as needed to fit your specific use case.

For additional help, join our community on [Discord](https://discord.com/invite/fal-ai) or contact our support team.
