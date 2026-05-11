> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy 3D Progressive Rendering

> Build a real-time text-to-3D and image-to-3D application with live voxel streaming using SAM-3D Objects.

This example demonstrates how to build a 3D reconstruction pipeline that streams
voxel data in real-time during diffusion. Watch your 3D models take shape
progressively as geometry and appearance diffusion stages run.

<div style={{ display: 'flex', gap: '16px', marginTop: '24px', marginBottom: '24px' }}>
  <video autoPlay loop muted playsInline controls style={{ flex: 1, borderRadius: '8px', maxWidth: '50%' }}>
    <source src="https://storage.googleapis.com/falserverless/example_inputs/3d.mp4" type="video/mp4" />
  </video>

  <video autoPlay loop muted playsInline controls style={{ flex: 1, borderRadius: '8px', maxWidth: '50%' }}>
    <source src="https://storage.googleapis.com/falserverless/example_inputs/minecraft3Dstream.mp4" type="video/mp4" />
  </video>
</div>

## 🚀 Try this Example

View the complete source code on [GitHub](https://github.com/rehan-remade/Manifold).

**Live Demo:** [manifold-jet.vercel.app](https://manifold-jet.vercel.app/)

**Steps to run:**

1. Install fal:

```bash theme={null}
pip install fal
```

2. Authenticate:

```bash theme={null}
fal auth login
```

3. Clone the repository with submodules:

```bash theme={null}
git clone --recurse-submodules https://github.com/rehan-remade/Manifold.git
cd Manifold
```

4. Set up the frontend:

```bash theme={null}
cd frontend
npm install
```

5. Configure environment variables in `frontend/.env.local`:

```env theme={null}
FAL_KEY=your_fal_api_key_here
FAL_ENDPOINT_ID=rehan/sam-3d-stream
GROQ_API_KEY=your_groq_api_key_here  # Optional, for prompt enhancement
```

6. Run the development server:

```bash theme={null}
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to see the demo.

<Tip>
  You can use the hosted endpoint `rehan/sam-3d-stream` directly, or deploy your own custom endpoint to modify the reconstruction pipeline.
</Tip>

## How it Works

1. **Prompt Enhancement** — Groq LLM (`llama-3.3-70b`) rewrites your text into an optimized image prompt + segmentation label
2. **Image Generation** — `fal-ai/z-image/turbo` generates a 3D-ready image in \~1s
3. **3D Reconstruction** — SAM-3D runs geometry and appearance diffusion on H100, streaming voxel data via SSE callbacks at each denoising step
4. **Live Visualization** — React Three Fiber renders voxels/mesh/GLB in real-time as data streams in

For image-to-3D, a vision model analyzes the uploaded image to generate the segmentation prompt.

## Deploy Your Own Endpoint

To customize the SAM-3D backend, deploy your own:

```bash theme={null}
cd serverless
fal deploy app.py::SAM3DStreamApp
```

Then update `FAL_ENDPOINT_ID` in `.env.local` with your new endpoint ID.

## Key Features

* **Progressive Rendering**: See voxels appear during both geometry and appearance diffusion stages
* **Binary Streaming Protocol**: Efficient base64-encoded voxel data (xyz + rgb per voxel)
* **Multiple Output Formats**: Voxels, vertex-colored mesh preview, and final GLB model
* **Custom Container**: Complex CUDA dependencies handled via Dockerfile
* **H100 GPU**: High-performance inference for fast reconstruction

## Backend Architecture

The serverless endpoint uses Server-Sent Events (SSE) for streaming progressive updates:

```python theme={null}
import fal
from fal.container import ContainerImage
from fastapi.responses import StreamingResponse

class SAM3DStreamApp(
    fal.App,
    keep_alive=600,
    kind="container",
    image=ContainerImage.from_dockerfile_str(dockerfile_str, builder="depot"),
):
    machine_type = "GPU-H100"

    def setup(self):
        # Download model weights and initialize pipeline
        from huggingface_hub import snapshot_download
        
        snapshot_download(
            "jetjodh/sam-3d-objects",
            local_dir=str(CACHE_DIR),
        )
        self.pipeline = self._create_pipeline(config_path)

    @fal.endpoint("/stream")
    def stream_3d_reconstruction(self, input: SAM3DStreamInput, request: Request):
        """Stream 3D reconstruction with real-time voxel visualization."""
        
        def geometry_callback(stage, step, total_steps, coords, **kwargs):
            # Encode and queue voxel data for streaming
            voxel_data = encode_voxels_binary(coords)
            progress_queue.put({
                "stage": "geometry",
                "step": step,
                "voxel_data": voxel_data,
            })

        def appearance_callback(stage, step, total_steps, coords, colors, **kwargs):
            # Stream colored voxels during appearance diffusion
            voxel_data = encode_voxels_binary(coords, colors)
            progress_queue.put({
                "stage": "appearance",
                "step": step,
                "voxel_data": voxel_data,
            })

        # Run pipeline with streaming callbacks
        outputs = self.pipeline.run(
            merged_image,
            geometry_callback=geometry_callback,
            appearance_callback=appearance_callback,
        )

        return StreamingResponse(
            event_stream(),
            media_type="text/event-stream",
        )
```

## SSE Event Types

The streaming endpoint emits these event types:

| Event          | Description                                                      |
| -------------- | ---------------------------------------------------------------- |
| `loading`      | Initial setup and image loading                                  |
| `geometry`     | Voxel coordinates during geometry diffusion (Stage 1)            |
| `appearance`   | Voxel coordinates + colors during appearance diffusion (Stage 2) |
| `mesh_preview` | Vertex-colored mesh (instant preview before texture baking)      |
| `glb_ready`    | Final textured GLB model data                                    |
| `complete`     | Final URLs for Gaussian splat and GLB files                      |

## Binary Voxel Encoding

Voxels are packed as uint8 arrays for efficient streaming:

```python theme={null}
def encode_voxels_binary(coords_np, colors_list):
    """Pack voxels as uint8: [x,y,z,r,g,b] per voxel."""
    # Normalize coordinates to 0-255 range
    coords_normalized = ((coords_np - coords_min) / coords_range * 255).astype(np.uint8)
    
    # Pack coordinates and colors
    packed = np.empty((len(coords_np), 6), dtype=np.uint8)
    packed[:, :3] = coords_normalized  # xyz
    packed[:, 3:] = colors_arr[:, :3]  # rgb
    
    return base64.b64encode(packed.tobytes()).decode("ascii")
```

## Frontend Integration

The React frontend uses a custom hook to consume the SSE stream:

```typescript theme={null}
export function useSAM3DStream() {
  const [voxels, setVoxels] = useState<Voxel[]>([]);
  const [meshData, setMeshData] = useState<MeshData | null>(null);
  const [renderMode, setRenderMode] = useState<RenderMode>("voxels");

  const startStream = useCallback(async (imageUrl: string, prompt: string) => {
    const response = await fetch("/api/stream-3d", {
      method: "POST",
      body: JSON.stringify({ imageUrl, prompt }),
    });

    const reader = response.body.getReader();
    
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      // Parse SSE events
      const event = JSON.parse(line.slice(6));
      
      if (event.stage === "geometry" || event.stage === "appearance") {
        const decoded = decodeVoxels(event);
        setVoxels(decoded);
        setRenderMode("voxels");
      } else if (event.stage === "mesh_preview") {
        const mesh = decodeMesh(event);
        setMeshData(mesh);
        setRenderMode("mesh");
      }
    }
  }, []);

  return { voxels, meshData, renderMode, startStream };
}
```

## Voxel Rendering with Three.js

Use React Three Fiber to render the streaming voxels:

```tsx theme={null}
function VoxelViewer({ voxels }: { voxels: Voxel[] }) {
  return (
    <Canvas>
      <instancedMesh args={[undefined, undefined, voxels.length]}>
        <boxGeometry args={[0.1, 0.1, 0.1]} />
        <meshStandardMaterial vertexColors />
        {voxels.map((voxel, i) => (
          <group key={i} position={[voxel.x, voxel.y, voxel.z]}>
            <mesh>
              <boxGeometry args={[0.1, 0.1, 0.1]} />
              <meshStandardMaterial color={voxel.color} />
            </mesh>
          </group>
        ))}
      </instancedMesh>
    </Canvas>
  );
}
```

## Custom Container Image

The backend requires complex CUDA dependencies. Use a Dockerfile for full control:

```python theme={null}
dockerfile_str = r"""
FROM nvidia/cuda:12.8.0-cudnn-devel-ubuntu22.04

# Install Python and system dependencies
RUN apt-get update && apt-get install -y python3.11 python3.11-dev \
    libgl1 libosmesa6 libosmesa6-dev

# PyTorch with CUDA support
RUN pip install torch==2.8.0 torchvision --index-url https://download.pytorch.org/whl/cu128

# SAM-3D Objects with streaming callback support
RUN git clone https://github.com/rehan-remade/sam-3d-objects.git && \
    cd sam-3d-objects && pip install -e .

# Additional 3D libraries
RUN pip install kaolin pytorch3d gsplat
"""

class SAM3DStreamApp(
    fal.App,
    kind="container",
    image=ContainerImage.from_dockerfile_str(dockerfile_str, builder="depot"),
):
    machine_type = "GPU-H100"
```

## Input Parameters

| Parameter               | Type          | Default  | Description                         |
| ----------------------- | ------------- | -------- | ----------------------------------- |
| `image_url`             | string        | required | URL of the image to reconstruct     |
| `mask_urls`             | list\[string] | `[]`     | Optional mask URLs for segmentation |
| `prompt`                | string        | `"car"`  | Text prompt for auto-segmentation   |
| `seed`                  | int           | random   | Random seed for reproducibility     |
| `stream_geometry_every` | int           | `1`      | Emit geometry updates every N steps |
| `stream_colors_every`   | int           | `1`      | Emit color updates every N steps    |

## Project Structure

```
manifold/
├── frontend/                 # Next.js web application
│   ├── app/
│   │   ├── page.tsx          # Main orchestrator
│   │   ├── api/              # Server-side API routes
│   │   ├── components/       # React Three Fiber components
│   │   ├── hooks/            # useSAM3DStream SSE hook
│   │   └── lib/              # Types, decoders, constants
│   └── public/
│
├── serverless/               # fal.ai serverless endpoint
│   ├── app.py                # SAM-3D streaming endpoint
│   └── pyproject.toml        # fal app config
│
└── sam-3d/                   # Git submodule (forked SAM-3D Objects)
```

## Performance Considerations

### Streaming Frequency

Control the streaming frequency to balance smoothness vs. performance:

```python theme={null}
class SAM3DStreamInput(BaseModel):
    stream_geometry_every: int = Field(
        default=1,
        ge=1,
        le=10,
        description="Emit geometry updates every N steps (1=smoothest, 10=fastest)",
    )
    stream_colors_every: int = Field(
        default=1,
        ge=1,
        le=10,
        description="Emit color updates every N steps",
    )
```

### Binary Encoding

The binary encoding reduces payload size significantly compared to JSON:

* 6 bytes per voxel (xyz + rgb as uint8)
* \~10,000 voxels = \~60KB per frame
* Base64 encoding adds \~33% overhead

## Key Takeaways

* **SSE streaming** enables real-time visualization of long-running 3D reconstruction
* **Binary encoding** makes voxel streaming efficient over HTTP
* **Custom containers** handle complex GPU dependencies (CUDA, PyTorch3D, kaolin)
* **Progressive rendering** gives users immediate visual feedback during generation
* **H100 GPUs** provide the compute power needed for fast 3D diffusion

This pattern demonstrates how to build interactive 3D AI applications that provide real-time feedback, combining the power of diffusion models with efficient streaming protocols and modern web rendering.
