> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy Real-time World Model

> Run a real-time world model demo powered by Matrix-Game.

This example streams a live world model with Matrix-Game. WebRTC is the
transport layer for low-latency, real-time video streaming.

<div style={{ display: 'flex', justifyContent: 'center', gap: '16px', marginTop: '24px', marginBottom: '24px' }}>
  <video autoPlay loop muted playsInline controls style={{ borderRadius: '8px', maxWidth: '60%' }}>
    <source src="https://storage.googleapis.com/falserverless/example_inputs/webRTCMatrix.mp4" type="video/mp4" />
  </video>
</div>

## 🚀 Try this Example

View the complete source code on [GitHub](https://github.com/fal-ai-community/fal-demos/tree/main/fal_demos/video/matrix_webrtc).

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
fal run fal_demos/video/matrix_webrtc/matrix.py::MatrixGame2
```

5. Run the frontend:

```bash theme={null}
cd fal_demos/video/matrix_webrtc/frontend
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
fal deploy fal_demos/video/matrix_webrtc/matrix.py::MatrixGame2
```

The real-time endpoint will be `your-username/your-app/webrtc`.

## Game modes and seed image

The backend defaults to the `universal` mode in `MatrixGame2.setup()`. Other
supported modes include `universal` and `gta_drive`. To switch modes, update
`self._default_mode` and `self._mode_seed_dirs` in `matrix.py`.

The seed image path is derived in `MatrixGame2.setup()` from the selected mode.
If you want a different seed, update `self._default_seed_path` in `matrix.py`.
