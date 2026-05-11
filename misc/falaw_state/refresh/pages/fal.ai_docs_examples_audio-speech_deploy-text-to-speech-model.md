> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy a Text-to-Speech Model

> This example demonstrates how to build a comprehensive text-to-speech service using Kokoro, showcasing CPU-efficient deployment, multi-language support, multiple endpoints with shared logic, and advanced audio processing techniques.

## 🚀 Try this Example

View the complete source code on [GitHub](https://github.com/fal-ai-community/fal-demos/blob/main/fal_demos/tts/kokoro.py).

**Steps to run:**

1. Install fal:

```bash theme={null}
pip install fal
```

2. Authenticate (if not already done):

```bash theme={null}
fal auth login
```

3. Copy the code below into `kokoro.py`

<CodeGroup>
  ```python kokoro.py wrap theme={null}
  from typing import Literal

  import fal
  from fal.exceptions import FieldException
  from fal.toolkit import File
  from fastapi import Response
  from pydantic import BaseModel, Field


  class AmEnglishRequest(BaseModel):
      prompt: str = Field(
          default="",
          examples=[
              "The future belongs to those who believe in the beauty of their dreams. So, dream big, work hard, and make it happen!"
          ],
          ui={"important": True},
      )
      text: str = Field(
          default="",
          examples=[
              "The future belongs to those who believe in the beauty of their dreams. So, dream big, work hard, and make it happen!"
          ],
      )
      # Use Literal for voice to restrict to specific enum values
      voice: Literal[
          "af_heart",
          "af_alloy",
          "af_aoede",
          "af_bella",
          "af_jessica",
          "af_kore",
          "af_nicole",
          "af_nova",
          "af_river",
          "af_sarah",
          "af_sky",
          "am_adam",
          "am_echo",
          "am_eric",
          "am_fenrir",
          "am_liam",
          "am_michael",
          "am_onyx",
          "am_puck",
          "am_santa",
      ] = Field(
          examples=["af_heart"],
          default="af_heart",
          description="Voice ID for the desired voice.",
      )
      speed: float = Field(
          default=1.0,
          ge=0.1,
          le=5.0,
          description="Speed of the generated audio. Default is 1.0.",
      )


  class BrEnglishRequest(BaseModel):
      prompt: str = Field(
          examples=[
              "Ladies and gentlemen, welcome aboard. Please ensure your seatbelt is fastened and your tray table is stowed as we prepare for takeoff."
          ]
      )
      voice: Literal[
          "bf_alice",
          "bf_emma",
          "bf_isabella",
          "bf_lily",
          "bm_daniel",
          "bm_fable",
          "bm_george",
          "bm_lewis",
      ] = Field(
          examples=["bf_alice"],
          description="Voice ID for the desired voice.",
      )
      speed: float = Field(
          default=1.0,
          ge=0.1,
          le=5.0,
          description="Speed of the generated audio. Default is 1.0.",
      )


  class JapaneseRequest(BaseModel):
      prompt: str = Field(examples=["夢を追いかけることを恐れないでください。努力すれば、必ず道は開けます！"])
      voice: Literal[
          "jf_alpha",
          "jf_gongitsune",
          "jf_nezumi",
          "jf_tebukuro",
          "jm_kumo",
      ] = Field(
          examples=["jf_alpha"],
          description="Voice ID for the desired voice.",
      )
      speed: float = Field(
          default=1.0,
          ge=0.1,
          le=5.0,
          description="Speed of the generated audio. Default is 1.0.",
      )


  class AmEngOutput(BaseModel):
      audio: File = Field(
          description="The generated music",
          examples=[
              File._from_url(
                  "https://fal.media/files/elephant/dXVMqWsBDG9yan3kaOT0Z_tmp0vvkha3s.wav"
              )
          ],
      )


  class BrEngOutput(BaseModel):
      audio: File = Field(
          description="The generated music",
          examples=[
              File._from_url(
                  "https://fal.media/files/kangaroo/4wpA60Kum6UjOVBKJoNyL_tmpxfrkn95k.wav"
              )
          ],
      )


  class JapaneseOutput(BaseModel):
      audio: File = Field(
          description="The generated music",
          examples=[
              File._from_url(
                  "https://fal.media/files/lion/piLhqKO8LJxrWaNg2dVUv_tmpp6eff6zl.wav"
              )
          ],
      )


  class Kokoro(fal.App):
      min_concurrency = 0
      max_concurrency = 1
      keep_alive = 3000
      app_name = "kokoro"
      requirements = [
          "kokoro==0.8.4",
          "soundfile==0.13.1",
          "misaki[en]==0.8.4",
          "misaki[ja]==0.8.4",
          "misaki[zh]==0.8.4",
          "numpy==1.26.4",
          "https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl",
      ]
      machine_type = "L"  # Use a CPU machine type since Kokoro is only 82M parameters and runs efficiently on CPU

      async def setup(self):
          from kokoro import KPipeline

          self.pipelines = {}
          self.pipelines["American English"] = KPipeline(lang_code="a")
          self.pipelines["British English"] = KPipeline(lang_code="b")
          self.pipelines["Japanese"] = KPipeline(lang_code="j")

      async def _generate(
          self,
          request: AmEnglishRequest,
          response: Response,
          language: str = "American English",
      ):
          prompt = request.prompt or request.text
          if len(prompt) >= 20000:
              # Use fieldexception to nicely render the error in the UI
              raise FieldException(
                  field="prompt",
                  message="Prompt must be less than 20000 characters.",
              )

          import tempfile

          import numpy as np
          import soundfile as sf

          pipeline = self.pipelines[language]
          generator = pipeline(
              prompt,
              voice=request.voice,
              speed=request.speed,
              split_pattern=r"\n+",
          )
          for i, (gs, ps, audio) in enumerate(generator):
              if i == 0:
                  final_audio = audio.detach().cpu().numpy()
              else:
                  audio = audio.detach().cpu().numpy()
                  final_audio = np.concatenate((final_audio, audio), axis=0)

          # Set the billing units to be a minimum of 1 and scale with 1000 characters
          response.headers["x-fal-billable-units"] = str(max(1, len(prompt) // 1000))

          # Use a temporary file to save the audio and then send it via the cdn through the File object
          with tempfile.NamedTemporaryFile(suffix=".wav") as f:
              sf.write(f.name, final_audio, 24000)
              return AmEngOutput(
                  audio=File.from_path(f.name, content_type="audio/wav", repository="cdn")
              )

      @fal.endpoint("/")
      async def generate(
          self, request: AmEnglishRequest, response: Response
      ) -> AmEngOutput:
          return await self._generate(request, response, language="American English")

      @fal.endpoint("/american-english")
      async def generate_am_english(
          self, request: AmEnglishRequest, response: Response
      ) -> AmEngOutput:
          return await self._generate(request, response, language="American English")

      @fal.endpoint("/british-english")
      async def generate_br_english(
          self, request: BrEnglishRequest, response: Response
      ) -> BrEngOutput:
          return await self._generate(request, response, language="British English")

      @fal.endpoint("/japanese")
      async def generate_japanese(
          self, request: JapaneseRequest, response: Response
      ) -> JapaneseOutput:
          return await self._generate(request, response, language="Japanese")


  ...  # Define the rest of the languages as endpoints similarly
  ```

  ```toml pyproject.toml wrap theme={null}
  [project]
  name = "kokoro-demo"
  version = "0.1.0"
  description = "Kokoro text-to-speech demo"
  requires-python = ">=3.11"
  dependencies = [
      "pydantic>=2.0",
      "fal @ git+https://github.com/fal-ai/fal.git#subdirectory=projects/fal"
  ]

  [tool.fal.apps]
  kokoro = { auth = "shared", ref = "kokoro.py::Kokoro", no_scale=true }
  ```
</CodeGroup>

4. Run the app:

```bash theme={null}
fal run kokoro.py
```

<Info>
  **Or clone this repository**:

  ```bash theme={null}
  git clone https://github.com/fal-ai-community/fal-demos.git
  cd fal-demos
  pip install -e .
  # Use the app name (defined in pyproject.toml)
  fal run kokoro
  # Or use the full file path:
  # fal run fal_demos/tts/kokoro.py::Kokoro
  ```
</Info>

<Tip>
  **Before you run**, make sure you have:

  * Authenticated with fal: `fal auth login`
  * Activated your virtual environment (recommended): `python -m venv venv && source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows)
</Tip>

## Key Features

* **Multi-Language Support**: American English, British English, Japanese with native voices
* **CPU-Efficient Deployment**: Lightweight 82M parameter model runs efficiently on CPU
* **Multiple Endpoints**: Language-specific endpoints with shared generation logic
* **Voice Variety**: Multiple voice options for each supported language
* **Audio Streaming**: Generator-based audio processing for memory efficiency
* **Character-Based Billing**: Usage-based pricing tied to text length
* **Advanced Validation**: Custom error handling with user-friendly messages
* **Audio File Management**: Temporary file handling and CDN integration

## When to Use CPU Deployment

CPU deployment is ideal when:

* Models are lightweight (\< 100M parameters)
* Inference is fast enough on CPU
* Cost optimization is important
* GPU resources are not required
* Multiple concurrent requests can share CPU resources efficiently

## Project Setup

```python theme={null}
from typing import Literal

import fal
from fal.exceptions import FieldException
from fal.toolkit import File
from fastapi import Response
from pydantic import BaseModel, Field
```

## Language-Specific Input Models

Define input models for each supported language with appropriate voice options:

```python theme={null}
class AmEnglishRequest(BaseModel):
    prompt: str = Field(
        default="",
        examples=[
            "The future belongs to those who believe in the beauty of their dreams. So, dream big, work hard, and make it happen!"
        ],
        ui={"important": True},
    )
    text: str = Field(
        default="",
        examples=[
            "The future belongs to those who believe in the beauty of their dreams. So, dream big, work hard, and make it happen!"
        ],
    )
    voice: Literal[
        "af_heart",    # American Female voices
        "af_alloy",
        "af_aoede",
        "af_bella",
        "af_jessica",
        "af_kore",
        "af_nicole",
        "af_nova",
        "af_river",
        "af_sarah",
        "af_sky",
        "am_adam",     # American Male voices
        "am_echo",
        "am_eric",
        "am_fenrir",
        "am_liam",
        "am_michael",
        "am_onyx",
        "am_puck",
        "am_santa",
    ] = Field(
        examples=["af_heart"],
        default="af_heart",
        description="Voice ID for the desired voice.",
    )
    speed: float = Field(
        default=1.0,
        ge=0.1,
        le=5.0,
        description="Speed of the generated audio. Default is 1.0.",
    )

class BrEnglishRequest(BaseModel):
    prompt: str = Field(
        examples=[
            "Ladies and gentlemen, welcome aboard. Please ensure your seatbelt is fastened and your tray table is stowed as we prepare for takeoff."
        ]
    )
    voice: Literal[
        "bf_alice",    # British Female voices
        "bf_emma",
        "bf_isabella",
        "bf_lily",
        "bm_daniel",   # British Male voices
        "bm_fable",
        "bm_george",
        "bm_lewis",
    ] = Field(
        examples=["bf_alice"],
        description="Voice ID for the desired voice.",
    )
    speed: float = Field(
        default=1.0,
        ge=0.1,
        le=5.0,
        description="Speed of the generated audio. Default is 1.0.",
    )

class JapaneseRequest(BaseModel):
    prompt: str = Field(
        examples=["夢を追いかけることを恐れないでください。努力すれば、必ず道は開けます！"]
    )
    voice: Literal[
        "jf_alpha",    # Japanese Female voices
        "jf_gongitsune",
        "jf_nezumi",
        "jf_tebukuro",
        "jm_kumo",     # Japanese Male voices
    ] = Field(
        examples=["jf_alpha"],
        description="Voice ID for the desired voice.",
    )
    speed: float = Field(
        default=1.0,
        ge=0.1,
        le=5.0,
        description="Speed of the generated audio. Default is 1.0.",
    )
```

## Language-Specific Output Models

```python theme={null}
class AmEngOutput(BaseModel):
    audio: File = Field(
        description="The generated audio",
        examples=[
            File._from_url(
                "https://fal.media/files/elephant/dXVMqWsBDG9yan3kaOT0Z_tmp0vvkha3s.wav"
            )
        ],
    )

class BrEngOutput(BaseModel):
    audio: File = Field(
        description="The generated audio",
        examples=[
            File._from_url(
                "https://fal.media/files/kangaroo/4wpA60Kum6UjOVBKJoNyL_tmpxfrkn95k.wav"
            )
        ],
    )

class JapaneseOutput(BaseModel):
    audio: File = Field(
        description="The generated audio",
        examples=[
            File._from_url(
                "https://fal.media/files/lion/piLhqKO8LJxrWaNg2dVUv_tmpp6eff6zl.wav"
            )
        ],
    )
```

## Application Configuration for CPU Deployment

```python theme={null}
class Kokoro(fal.App):
    min_concurrency = 0
    max_concurrency = 1
    keep_alive = 3000  # Longer keep-alive for TTS services
    app_name = "kokoro"
    requirements = [
        "kokoro==0.8.4",
        "soundfile==0.13.1",
        "misaki[en]==0.8.4",  # English language support
        "misaki[ja]==0.8.4",  # Japanese language support
        "misaki[zh]==0.8.4",  # Chinese language support
        "numpy==1.26.4",
        # Spacy model for English NLP
        "https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl",
    ]
    machine_type = "L"  # CPU machine - efficient for lightweight models

    async def setup(self):
        from kokoro import KPipeline

        # Initialize pipelines for each supported language
        self.pipelines = {}
        self.pipelines["American English"] = KPipeline(lang_code="a")
        self.pipelines["British English"] = KPipeline(lang_code="b")
        self.pipelines["Japanese"] = KPipeline(lang_code="j")
```

## Shared Generation Logic

Create a reusable generation method that handles all languages:

```python theme={null}
async def _generate(
    self,
    request: AmEnglishRequest,
    response: Response,
    language: str = "American English",
):
    # Handle both 'prompt' and 'text' fields for backwards compatibility
    prompt = request.prompt or request.text

    # Custom validation with user-friendly error messages
    if len(prompt) >= 20000:
        raise FieldException(
            field="prompt",
            message="Prompt must be less than 20000 characters.",
        )

    import tempfile
    import numpy as np
    import soundfile as sf

    # Get the appropriate pipeline for the language
    pipeline = self.pipelines[language]

    # Generate audio using streaming approach
    generator = pipeline(
        prompt,
        voice=request.voice,
        speed=request.speed,
        split_pattern=r"\n+",  # Split on line breaks for better pacing
    )

    # Process audio chunks and concatenate
    for i, (gs, ps, audio) in enumerate(generator):
        if i == 0:
            final_audio = audio.detach().cpu().numpy()
        else:
            audio = audio.detach().cpu().numpy()
            final_audio = np.concatenate((final_audio, audio), axis=0)

    # Character-based billing calculation
    response.headers["x-fal-billable-units"] = str(max(1, len(prompt) // 1000))

    # Save audio to temporary file and upload to CDN
    with tempfile.NamedTemporaryFile(suffix=".wav") as f:
        sf.write(f.name, final_audio, 24000)  # 24kHz sample rate
        return AmEngOutput(
            audio=File.from_path(
                f.name,
                content_type="audio/wav",
                repository="cdn"  # Upload to CDN for fast access
            )
        )
```

## Multiple Endpoint Definitions

Define language-specific endpoints using the shared generation logic:

```python theme={null}
@fal.endpoint("/")
async def generate(
    self, request: AmEnglishRequest, response: Response
) -> AmEngOutput:
    return await self._generate(request, response, language="American English")

@fal.endpoint("/american-english")
async def generate_am_english(
    self, request: AmEnglishRequest, response: Response
) -> AmEngOutput:
    return await self._generate(request, response, language="American English")

@fal.endpoint("/british-english")
async def generate_br_english(
    self, request: BrEnglishRequest, response: Response
) -> BrEngOutput:
    return await self._generate(request, response, language="British English")

@fal.endpoint("/japanese")
async def generate_japanese(
    self, request: JapaneseRequest, response: Response
) -> JapaneseOutput:
    return await self._generate(request, response, language="Japanese")
```

## Key Concepts and Best Practices

### CPU-Efficient Deployment

**Why CPU for TTS:**

* Kokoro is only 82M parameters - runs efficiently on CPU
* Lower cost compared to GPU instances
* Sufficient performance for real-time TTS
* Better resource utilization for multiple concurrent requests

### Audio Streaming and Memory Management

**Generator-based processing:**

```python theme={null}
# Stream audio generation to handle long texts efficiently
generator = pipeline(prompt, voice=request.voice, speed=request.speed)

# Process chunks incrementally
for i, (gs, ps, audio) in enumerate(generator):
    if i == 0:
        final_audio = audio.detach().cpu().numpy()
    else:
        final_audio = np.concatenate((final_audio, audio), axis=0)
```

### Character-Based Billing

```python theme={null}
# Scale billing with text length (per 1000 characters)
response.headers["x-fal-billable-units"] = str(max(1, len(prompt) // 1000))
```

### Audio File Handling

```python theme={null}
# Use temporary files for audio processing
with tempfile.NamedTemporaryFile(suffix=".wav") as f:
    sf.write(f.name, final_audio, 24000)  # Save with proper sample rate
    return Output(
        audio=File.from_path(
            f.name,
            content_type="audio/wav",
            repository="cdn"  # Auto-upload to CDN
        )
    )
```

### Multi-Language Architecture

**Pipeline initialization:**

```python theme={null}
self.pipelines = {
    "American English": KPipeline(lang_code="a"),
    "British English": KPipeline(lang_code="b"),
    "Japanese": KPipeline(lang_code="j"),
}
```

**Language-specific voice options:**

```python theme={null}
# American English voices
voice: Literal[
    "af_heart", "af_alloy", "af_aoede",  # Female
    "am_adam", "am_echo", "am_eric",     # Male
]

# British English voices
voice: Literal[
    "bf_alice", "bf_emma", "bf_lily",    # Female
    "bm_daniel", "bm_george", "bm_lewis" # Male
]
```

## Advanced Features

### Custom Validation

```python theme={null}
if len(prompt) >= 20000:
    raise FieldException(
        field="prompt",
        message="Prompt must be less than 20000 characters.",
    )
```

### Backwards Compatibility

```python theme={null}
# Support both 'prompt' and 'text' field names
prompt = request.prompt or request.text
```

### Flexible Text Processing

```python theme={null}
generator = pipeline(
    prompt,
    voice=request.voice,
    speed=request.speed,
    split_pattern=r"\n+",  # Split on paragraphs for natural pacing
)
```

## Deployment and Usage

### Running the Service

```bash theme={null}
# Development
fal run fal_demos/tts/kokoro.py::Kokoro

# Production deployment
fal deploy kokoro
```

### Making Requests

**American English:**

```python theme={null}
import fal_client

result = await fal_client.submit_async(
    "your-username/kokoro/american-english",
    arguments={
        "prompt": "Hello, this is a test of American English text-to-speech!",
        "voice": "af_heart",
        "speed": 1.2
    }
)
```

**British English:**

```python theme={null}
result = await fal_client.submit_async(
    "your-username/kokoro/british-english",
    arguments={
        "prompt": "Cheerio! This is British English text-to-speech.",
        "voice": "bf_alice",
        "speed": 1.0
    }
)
```

**Japanese:**

```python theme={null}
result = await fal_client.submit_async(
    "your-username/kokoro/japanese",
    arguments={
        "prompt": "こんにちは、これは日本語の音声合成です。",
        "voice": "jf_alpha",
        "speed": 0.9
    }
)
```

## Use Cases

* **Content Creation**: Generate voiceovers for videos and podcasts
* **Accessibility**: Convert text content to audio for visually impaired users
* **E-Learning**: Create educational content with natural-sounding narration
* **Customer Service**: Generate dynamic audio responses for chatbots
* **Multilingual Applications**: Support global audiences with native-sounding voices
* **Book Reading**: Convert written content to audiobooks

## Performance Optimizations

### Memory Efficiency

```python theme={null}
# Stream processing prevents memory buildup for long texts
for i, (gs, ps, audio) in enumerate(generator):
    # Process incrementally rather than loading all at once
```

### Cost Optimization

```python theme={null}
machine_type = "L"  # CPU is sufficient and cost-effective
keep_alive=3000     # Longer keep-alive reduces cold starts
```

## Key Takeaways

* **CPU deployment** is ideal for lightweight models like Kokoro (82M parameters)
* **Multi-language support** requires separate pipelines and voice models
* **Character-based billing** aligns costs with resource usage
* **Audio streaming** handles long texts efficiently without memory issues
* **Temporary file handling** with CDN upload provides fast, reliable audio delivery
* **Multiple endpoints** with shared logic offer flexibility while maintaining DRY principles
* **Custom validation** provides better user experience with clear error messages

This pattern is perfect for building production-ready TTS services that need to support multiple languages and voices while maintaining cost efficiency and high performance through CPU-optimized deployment.
