> ## Documentation Index
> Fetch the complete documentation index at: https://fal.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Examples

> Step-by-step tutorials and code examples for building with fal

export const ExampleCard = ({title, description, image, href, dateAdded}) => {
  let isNew = false;
  if (dateAdded) {
    const added = new Date(dateAdded);
    const now = new Date();
    const diffTime = Math.abs(now - added);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    isNew = diffDays <= 30;
  }
  return <a href={href} className="group block no-underline" style={{
    border: 'none',
    outline: 'none'
  }}>
      <div className="relative rounded-2xl overflow-hidden transition-all duration-500 ease-out group-hover:scale-[1.03]" style={{
    height: '340px',
    backgroundImage: `url(${image})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    border: 'none',
    boxShadow: '0 4px 20px rgba(0,0,0,0.15)'
  }}>
        <div className="absolute inset-0" style={{
    background: 'linear-gradient(to bottom, rgba(0,0,0,0.35) 0%, rgba(0,0,0,0.25) 50%, rgba(0,0,0,0.5) 100%)'
  }} />
        
        {isNew && <div className="absolute top-4 right-4 z-10 px-3 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider" style={{
    background: 'linear-gradient(135deg, #8553ff 0%, #6366f1 100%)',
    color: 'white',
    fontFamily: 'Public Sans',
    fontSize: '10px',
    letterSpacing: '1px',
    boxShadow: '0 2px 10px rgba(133, 83, 255, 0.4)'
  }}>
            New
          </div>}
        
        <div className="absolute inset-0 transition-all duration-500 group-hover:opacity-90" style={{
    background: 'linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 35%, transparent 60%)'
  }} />
        
        <div className="absolute bottom-0 left-0 right-0 p-5 transition-all duration-300">
          <h4 className="text-white mb-2 transition-transform duration-300 group-hover:translate-y-[-2px]" style={{
    fontFamily: 'Focal',
    fontSize: '24px',
    fontWeight: 500,
    lineHeight: 1,
    letterSpacing: '-0.48px'
  }}>
            {title}
          </h4>
          <p className="text-white transition-all duration-300 group-hover:translate-y-[-2px]" style={{
    fontFamily: 'Public Sans',
    fontSize: '14px',
    fontWeight: 500,
    lineHeight: 1.5,
    letterSpacing: '-0.28px'
  }}>
            {description}
          </p>
        </div>
      </div>
    </a>;
};

export const MODEL_API_EXAMPLES = [{
  title: "Generate Images from Text",
  description: "Create stunning images using text prompts with FLUX and other models.",
  image: "https://v3b.fal.media/files/b/rabbit/EuI3qlj6YuU0RdL8frhFz_b3f41c0a0a204cedb65fdd422b42f4d5.jpg",
  href: "/examples/image-generation/generate-images-from-text",
  dateAdded: null
}, {
  title: "Generate Videos from Images",
  description: "Transform static images into dynamic videos with AI-powered animation.",
  image: "https://v3b.fal.media/files/b/kangaroo/ytEAu0n1-fdVCtHgm7I9a_89ee87948a774d219c29351b1e4fd4da.jpg",
  href: "/examples/video-generation/generate-videos-from-image",
  dateAdded: null
}, {
  title: "Convert Speech to Text",
  description: "Transcribe audio files with high accuracy using Whisper.",
  image: "https://v3b.fal.media/files/b/zebra/RG5Bvv69wgJv-gbWAliYW_45ae8d4adc8b4b5e926b3c2c28a127d4.jpg",
  href: "/examples/audio-speech/convert-speech-to-text",
  dateAdded: null
}, {
  title: "Use Large Language Models",
  description: "Build powerful AI applications with Llama, Mistral, and other LLMs.",
  image: "https://v3b.fal.media/files/b/zebra/pjq9D101BZainhOpBpdIa_04328ca3afde43e0809d8f471fb52062.jpg",
  href: "/examples/integrations/use-llms",
  dateAdded: null
}, {
  title: "Fast FLUX",
  description: "Ultra-fast image generation with optimized FLUX.",
  image: "/images/image-5.png",
  href: "/examples/image-generation/fast-flux",
  dateAdded: null
}, {
  title: "Fast SDXL",
  description: "High-speed Stable Diffusion XL inference.",
  image: "/images/image-9.png",
  href: "/examples/image-generation/fast-sdxl",
  dateAdded: null
}, {
  title: "Build Custom Workflow UI",
  description: "Create intuitive user interfaces for complex AI workflows.",
  image: "https://v3b.fal.media/files/b/kangaroo/4nMIYfcKpQOoN5Xkxx8Xj_aada02b4749f41839f2f96fc6789ccea.jpg",
  href: "/examples/integrations/custom-workflow-ui",
  dateAdded: null
}, {
  title: "Integrate with n8n",
  description: "Automate workflows by integrating fal AI models with n8n.",
  image: "https://v3b.fal.media/files/b/penguin/nB7rGViPfVhhjB4G2jPJp_73c97f13d0364bc9b912d316c1bb6d07.jpg",
  href: "/examples/integrations/n8n",
  dateAdded: null
}, {
  title: "Next.js Integration",
  description: "Build full-stack AI apps with Next.js and fal.",
  image: "/images/image-8.png",
  href: "/examples/integrations/nextjs",
  dateAdded: null
}, {
  title: "Vercel Integration",
  description: "Deploy AI-powered apps on Vercel with fal.",
  image: "/images/image-7.png",
  href: "/examples/integrations/vercel",
  dateAdded: null
}];

export const SERVERLESS_EXAMPLES = [{
  title: "Deploy Text-to-Image Model",
  description: "Build and deploy your own text-to-image API using Sana or FLUX.",
  image: "https://v3b.fal.media/files/b/zebra/LKfy5G6ZTgDi5kqSK7G6v_16dc6c79476d4d858d8f22b2d77d374f.jpg",
  href: "/examples/image-generation/deploy-text-to-image-model",
  dateAdded: null
}, {
  title: "Deploy Text-to-Video Model",
  description: "Create a production-ready video generation API with WAN.",
  image: "https://v3b.fal.media/files/b/elephant/fVvQzNYZ9vtG3SwxJPhWs_85d586a94ba34c278427459e3f598f05.jpg",
  href: "/examples/video-generation/deploy-text-to-video-model",
  dateAdded: null
}, {
  title: "Deploy WAN LoRA Training",
  description: "Fine-tune WAN video generation with LoRA training.",
  image: "/images/image-6.png",
  href: "/examples/image-generation/deploy-wan-lora-training",
  dateAdded: null
}, {
  title: "Deploy a ComfyUI Server",
  description: "Run ComfyUI with SDXL Turbo as a serverless API.",
  image: "https://v3b.fal.media/files/b/0a876c07/ahOa0bd2Z1_HQFfOl_Uy9_04d7d98840f74acd91ae4628ddd42d9d.jpg",
  href: "/examples/image-generation/deploy-comfyui-server",
  dateAdded: null
}, {
  title: "Deploy Multi-GPU Inference",
  description: "Scale image generation across multiple GPUs with streaming.",
  image: "https://v3b.fal.media/files/b/koala/sxlKoYjz5-pUSPg2KvP4U_5a478c7423a048f89c4c5e90c287b96f.jpg",
  href: "/examples/video-generation/deploy-multi-gpu-inference",
  dateAdded: null
}, {
  title: "Deploy Text-to-Speech Model",
  description: "Build natural-sounding voice synthesis APIs with Kokoro.",
  image: "https://v3b.fal.media/files/b/rabbit/-YOK-ncB-zw8iZu0lGhKx_537ff78d861c44acb7f584623480f464.jpg",
  href: "/examples/audio-speech/deploy-text-to-speech-model",
  dateAdded: null
}, {
  title: "Deploy Text-to-Music Model",
  description: "Generate original music from text descriptions using DiffRhythm.",
  image: "https://v3b.fal.media/files/b/tiger/kBuwc7RF4jOPMisP24Rg0_1684aba74ec14c81a9544e33102c3ec8.jpg",
  href: "/examples/audio-speech/deploy-text-to-music-model",
  dateAdded: null
}, {
  title: "Publish Custom Metrics with Prometheus Pushgateway",
  description: "Publish custom metrics on fal and expose them for scraping.",
  image: "/images/image-1.png",
  href: "/examples/serverless/deploy-prometheus-pushgateway",
  dateAdded: "2026-04-16"
}, {
  title: "Deploy 3D Progressive Rendering",
  description: "Stream real-time text-to-3D reconstruction with live voxel visualization.",
  image: "https://v3b.fal.media/files/b/0a8935fe/Ezbvf27opeW6gEoDS4nlw_da7064399f9c4342b5e118f6875ec389.jpg",
  href: "/examples/video-generation/deploy-3d-progressive-rendering",
  dateAdded: null
}, {
  title: "Deploy Real-time Video-to-Video",
  description: "Run real-time video-to-video with YOLO object detection.",
  image: "https://v3b.fal.media/files/b/0a8d2007/gV_LMXNrguqRaDB9sLqir_b5d36b36de5a40bdb5cb2cd3f8af29d7.jpg",
  href: "/examples/video-generation/deploy-realtime-video-to-video-model",
  dateAdded: null
}, {
  title: "Deploy Real-time World Model",
  description: "Run a real-time world model demo powered by Matrix-Game.",
  image: "https://v3b.fal.media/files/b/tiger/IwzOGSbzp6e8N00QuLtFF_129417bb24f248298e95c3fa2b1b82fb.jpg",
  href: "/examples/video-generation/deploy-realtime-world-model",
  dateAdded: null
}, {
  title: "Deploy with Custom Containers",
  description: "Use custom Docker containers for complex dependencies.",
  image: "https://v3b.fal.media/files/b/zebra/L5WtylOCEW3cb28FVzVH0_49db14e3031b41b9838a267cf8214ef8.jpg",
  href: "/examples/deploy-models-with-custom-containers",
  dateAdded: null
}, {
  title: "Migrate from Replicate",
  description: "Move your models from Replicate to fal.",
  image: "https://v3b.fal.media/files/b/kangaroo/WcNt4yo_7RJaCZa0Og6gE_37660458463d4008959517c59a40aafd.jpg",
  href: "/examples/integrations/migrate-from-replicate",
  dateAdded: null
}, {
  title: "Migrate External Docker Server",
  description: "Migrate your existing Docker-based inference server to fal.",
  image: "https://v3b.fal.media/files/b/panda/LqyVE8NElm_vf-t27Yfkz_6c1dd3323df343e4a3ec968d8f67024c.jpg",
  href: "/examples/integrations/migrate-external-docker-server",
  dateAdded: null
}, {
  title: "Migrate from Modal",
  description: "Move your Modal applications to fal.",
  image: "https://v3b.fal.media/files/b/0a900b9e/ptbZcVWIQ_fXGGHfv8Zez_0ea5ca41bdf143a29e21e30a53120672.jpg",
  href: "/examples/integrations/migrate-from-modal",
  dateAdded: null
}, {
  title: "Migrate from RunPod",
  description: "Move your RunPod Serverless workers to fal.",
  image: "https://v3b.fal.media/files/b/0a8cfd08/Ji4e0i6Afbeql3Wr5UTz6_ab60b14661424612bf19059e97e996a5.jpg",
  href: "/examples/integrations/migrate-from-runpod",
  dateAdded: null
}];

## Using Models

Call fal's ready-to-use models from your application.

<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-6 mb-12">
  {MODEL_API_EXAMPLES.map((example, index) => (
      <ExampleCard key={index} {...example} />
    ))}
</div>

<div id="deploying-models" />

## Deploying Models

Deploy your own custom models on fal's serverless infrastructure.

<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
  {SERVERLESS_EXAMPLES.map((example, index) => (
      <ExampleCard key={index} {...example} />
    ))}
</div>
