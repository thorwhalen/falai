> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy WAN LoRA Training

> Fine-tune WAN (text-to-video) with LoRA using your own short clips and images.

## 🚀 Try this Example

View the complete source code on [GitHub](https://github.com/fal-ai-community/fal-demos/blob/main/fal_demos/video/wan_trainer.py).

**Steps to run:**

1. Install fal:

```bash theme={null}
pip install fal
```

2. Authenticate (if not already done):

```bash theme={null}
fal auth login
```

3. Clone the demos repo and install dependencies:

```bash theme={null}
git clone https://github.com/fal-ai-community/fal-demos.git
cd fal-demos
pip install -e .
```

4. Run the trainer:

```bash theme={null}
fal run fal_demos/video/wan_trainer.py::WanLoRATrainerDemo
```

<Tip>
  This demo uses a GPU-heavy training stack and can run for a while depending on your step count.
</Tip>

## Deploy to fal

To host the trainer as an API:

```bash theme={null}
fal deploy fal_demos/video/wan_trainer.py::WanLoRATrainerDemo
```

## How it works

* Downloads WAN weights from Hugging Face and a pinned training repo.
* Prepares a dataset from your ZIP file (images and/or short videos).
* Runs LoRA training with DeepSpeed and returns the adapter weights.

## Input format

Your `training_data_url` should point to a ZIP containing:

* Images or videos (`.png`, `.jpg`, `.jpeg`, `.gif`, `.mp4`)
* Optional caption files (`my_clip.txt` next to `my_clip.mp4`)

If you set `auto_scale_input=true`, videos are fit to **81 frames at 16 fps** for WAN training.

## Example request

```python theme={null}
import fal_client

result = fal_client.submit(
    "your-username/wan-lora-trainer-demo",
    arguments={
        "training_data_url": "https://your-bucket/train.zip",
        "rank": 16,
        "number_of_steps": 400,
        "learning_rate": 2e-4,
        "trigger_phrase": "your-style",
        "auto_scale_input": True,
        "video_clip_mode": "single_beginning",
    },
).get()

print(result["lora_file"]["url"])
```
