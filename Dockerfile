# Python 3.12 বা আপনার প্রজেক্ট অনুযায়ী অফিসিয়াল ইমেজ
FROM python:3.12-slim

# পাইথনের আউটপুট আনবাউন্ড রাখা এবং পাইক্যাচে ফাইল তৈরি বন্ধ করা
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ওয়ার্কিং ডিরেক্টরি সেট করা
WORKDIR /app

# প্রয়োজনীয় সিস্টেম ডিপেন্ডেন্সি ইনস্টল করা (PostgreSQL বা অন্যান্য প্যাকেজ বিল্ডের জন্য)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt কপি করা এবং পাইপ প্যাকেজ ইনস্টল করা
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# প্রজেক্টের বাকি সব ফাইল কপি করা
COPY . .

# হোয়াইটনিউজ (WhiteNoise) স্ট্যাটিক ফাইলের জন্য কনফিগার করা থাকলে গিউনিকর্ন দিয়ে সার্ভার রান করা
CMD ["gunicorn", "student_management_system.wsgi:application", "--bind", "0.0.0.0:10000"]