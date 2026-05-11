> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Real-time Video-to-Video Model

> Run a real-time video-to-video pipeline that returns YOLO detections on your stream.

This example turns a live webcam feed into annotated video using YOLO. WebRTC is
the transport layer for low-latency, real-time streaming.

## 🚀 Try this Example

View the complete source code on [GitHub](https://github.com/fal-ai-community/fal-demos/tree/main/fal_demos/video/yolo_webcam_webrtc).

**Steps to run:**

1. Install fal:

```bash theme={null}
pip install fal
```

2. Authenticate:

```bash theme={null}
fal auth login
```

3. Clone the demos repo and install dependencies:

```bash theme={null}
git clone https://github.com/fal-ai-community/fal-demos.git
cd fal-demos
pip install -e .
```

4. Run the backend (local dev):

```bash theme={null}
fal run fal_demos/video/yolo_webcam_webrtc/yolo.py::WebcamWebRtc
```

5. Run the frontend:

```bash theme={null}
cd fal_demos/video/yolo_webcam_webrtc/frontend
npm install
FAL_KEY=myfalkey npm run dev
```

Open the Vite dev server in your browser and set the **Endpoint** field to the
full real-time endpoint (for example: `myuser/myapp/webrtc`).

<Tip>
  This deployment flow is the same as other serverless examples, like [Deploy Text-to-Image Model](/examples/image-generation/deploy-text-to-image-model), but the request path is a real-time endpoint.
</Tip>

## Deploy to fal

To host the backend, deploy the app and use the resulting endpoint in the UI:

```bash theme={null}
fal deploy fal_demos/video/yolo_webcam_webrtc/yolo.py::WebcamWebRtc
```

The real-time endpoint will be `your-username/your-app/webrtc`.

## How it works

* The browser streams your webcam to the app in real-time (WebRTC transport).
* The backend runs YOLO on each frame and draws detection boxes.
* The annotated stream is sent back to the browser over the same connection.
