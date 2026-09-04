import torch
from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image, export_to_video
import argparse
import os

def generate_video(image_path, output_folder="outputs/videos"):
    # التأكد من وجود مجلد المخرجات
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # تحديد الجهاز المستخدم
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"🚀 يتم التشغيل باستخدام: {device}")

    # تحميل النموذج (Stable Video Diffusion XT)
    model_id = "stabilityai/stable-video-diffusion-img2vid-xt"
    
    print("⏳ جاري تحميل نموذج الفيديو (قد يستغرق وقتاً لأن حجمه كبير)...")
    pipe = StableVideoDiffusionPipeline.from_pretrained(
        model_id, 
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        variant="fp16" if device == "cuda" else None
    )
    
    if device == "cuda":
        pipe.enable_model_cpu_offload() # لتقليل استهلاك الذاكرة (VRAM)
    else:
        pipe = pipe.to(device)

    # تحميل وتجهيز الصورة
    image = load_image(image_path)
    image = image.resize((1024, 576)) # الأبعاد المثالية لهذا النموذج

    print(f"🎬 جاري تحويل الصورة {image_path} إلى فيديو...")
    
    # توليد الإطارات (Frames)
    # decode_chunk_size=8 يساعد في تقليل استهلاك الذاكرة
    frames = pipe(image, decode_chunk_size=8, generator=torch.manual_seed(42)).frames[0]

    # حفظ الفيديو
    file_name = f"video_{os.path.basename(image_path).split('.')[0]}.mp4"
    save_path = os.path.join(output_folder, file_name)
    export_to_video(frames, save_path, fps=7)
    
    print(f"✅ تم بنجاح! الفيديو جاهز هنا: {save_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Image-to-Video Generator")
    parser.add_argument("--image", type=str, required=True, help="مسار الصورة التي تريد تحويلها")
    
    args = parser.parse_args()
    generate_video(args.image)
