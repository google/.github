import os

# قراءة المفتاح من ملف .env
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("PILOT_API_KEY")

if not api_key:
    print("⚠️ لا يوجد مفتاح تشغيل. الرجاء إضافة مفتاح في ملف .env")
else:
    print(f"✅ المفتاح موجود: {api_key}")
    # هنا تقدر تكمل تشغيل برنامج الطيار الذكي