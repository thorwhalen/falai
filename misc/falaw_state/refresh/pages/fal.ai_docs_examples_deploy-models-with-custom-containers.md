> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Models with Custom Containers

> fal now supports running apps within custom Docker containers, providing greater flexibility and control over your environment.

### Example: Using Custom Containers with fal Apps

Here's a complete example demonstrating how to use custom containers with `fal`.

```python theme={null}
import fal

from fal.container import ContainerImage

dockerfile_str = """
FROM python:3.11

RUN apt-get update && apt-get install -y ffmpeg
RUN pip install pyjokes ffmpeg-python
"""

custom_image = ContainerImage.from_dockerfile_str(
    dockerfile_str,
    registries={
        "https://my.registry.io/": {
            "username": <username>,
            "password": <password>,
        },
    },
)

class Test(fal.App):
    image = custom_image
    machine_type = "GPU"

    requirements = ["torch"]

    def setup(self):
        import subprocess
        subprocess.run(["nvidia-smi"])

    @fal.endpoint("/")
    def index(self):
        return "Hello, World!"
```

#### Detailed Explanation

1. **Importing fal and ContainerImage**:

```python theme={null}
import fal
from fal.container import ContainerImage
```

2. **Creating a Dockerfile String**:
   A multi-line string (`dockerfile_str`) is defined, specifying the base image as `python:3.11`, and installing `ffmpeg` and `pyjokes` packages.

```python theme={null}
dockerfile_str = """
FROM python:3.11

RUN apt-get update && apt-get install -y ffmpeg
RUN pip install pyjokes ffmpeg-python
"""
```

<Note>
  **Version mismatch**

  Ensure that the Python version in the Dockerfile matches the Python version in
  your local environment that you use to run the app.

  This is required to avoid any compatibility issues. We use `pickle` to serialize
  the app under the hood, and the Python versions must match to avoid any
  serialization issues.

  That being said, we are constantly working on improving this experience.
</Note>

Alternatively, you can use a Dockerfile path to specify the Dockerfile location:

```python theme={null}
import pathlib
PWD = Path(__file__).resolve().parent

class Test(fal.App):
    image = ContainerImage.from_dockerfile(f"{PWD}/Dockerfile")
```

#### Running the App

To run the app, save the code to a file (e.g., `test_container.py`) and execute it using the `fal run` command:

```bash theme={null}
fal run test_container.py
```

This example demonstrates how to leverage Docker containers in fal, enabling customized execution environments for your apps. For more details and advanced usage, refer to the [fal Container Documentation](/serverless/development/use-custom-container-image).
