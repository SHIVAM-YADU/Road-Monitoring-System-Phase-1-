import cv2
import time
import os
from datetime import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("app.log"),   # saves logs to file
        logging.StreamHandler()           # shows logs in terminal
    ]
)

def cleanup_folder(folder_path):
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]

    # Keep only image files
    files = [f for f in files if f.endswith(".jpg")]

    if len(files) <= 1:
        return  # nothing to delete

    # Sort by modified time (latest last)
    files.sort(key=os.path.getmtime)

    latest_file = files[-1]

    for file in files:
        if file != latest_file:
            try:
                os.remove(file)
            except Exception as e:
                logging.error(f"Error deleting {file}: {e}")

    logging.info(f"Cleanup done in {folder_path}, kept: {latest_file}")
# ----------------------------
# CONFIG
CLEANUP_INTERVAL = 120  # 2 minutes (testing)
last_cleanup_time = time.time()
# ----------------------------

BASE_FOLDER = "."

CAPTURED_FOLDER = os.path.join(BASE_FOLDER, "captured_images")
POTHOLE_FOLDER = os.path.join(BASE_FOLDER, "potholes")
NORMAL_FOLDER = os.path.join(BASE_FOLDER, "normal")

os.makedirs(CAPTURED_FOLDER, exist_ok=True)
os.makedirs(POTHOLE_FOLDER, exist_ok=True)
os.makedirs(NORMAL_FOLDER, exist_ok=True)

CAPTURE_INTERVAL = 40   # 40 seconds (testing)

# 👉 Manual location
LOCATION_NAME = "Mumbai_Street_01"
LATITUDE = "19.0760N"
LONGITUDE = "72.8777E"

# ----------------------------
# CAMERA SETUP
# ----------------------------

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    logging.error("Could not open camera")
    exit()

logging.info("Camera running... capturing every 40 seconds")
logging.info("Press 'q' to quit")

last_capture_time = time.time()

# ----------------------------
# MAIN LOOP
# ----------------------------

while True:
    ret, frame = cap.read()

    if not ret:
        logging.warning("Camera error. Retrying...")
        time.sleep(2)
        cap = cv2.VideoCapture(0)
        continue

    cv2.imshow("Live Camera", frame)

    current_time = time.time()

    # ----------------------------
    # 📸 CAPTURE LOGIC
    # ----------------------------
    if current_time - last_capture_time >= CAPTURE_INTERVAL:

        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H-%M-%S")

        filename = f"{LOCATION_NAME}_{date_str}_{time_str}.jpg"

        # Add overlay text
        overlay1 = f"Date: {date_str} Time: {time_str}"
        overlay2 = f"Location: {LOCATION_NAME}"
        overlay3 = f"Lat: {LATITUDE}, Lon: {LONGITUDE}"

        font = cv2.FONT_HERSHEY_SIMPLEX
        frame_with_text = frame.copy()

        cv2.putText(frame_with_text, overlay1, (10, 30), font, 0.6, (0, 255, 0), 2)
        cv2.putText(frame_with_text, overlay2, (10, 60), font, 0.6, (0, 255, 0), 2)
        cv2.putText(frame_with_text, overlay3, (10, 90), font, 0.6, (0, 255, 0), 2)

        # Save raw
        raw_path = os.path.join(CAPTURED_FOLDER, filename)
        raw_saved = cv2.imwrite(raw_path, frame_with_text)

        # Temporary detection
        result = False

        # Save classified
        if result:
            final_path = os.path.join(POTHOLE_FOLDER, filename)
        else:
            final_path = os.path.join(NORMAL_FOLDER, filename)

        final_saved = cv2.imwrite(final_path, frame_with_text)

        # Logging
        if raw_saved and final_saved:
            logging.info(f"Captured at {time_str}")
            logging.info(f"Raw saved: {raw_path}")
            logging.info(f"Classified saved: {final_path}")
        else:
            logging.error("Error saving image")

        last_capture_time = current_time

    # ----------------------------
    # 🧹 CLEANUP LOGIC
    # ----------------------------
    if current_time - last_cleanup_time >= CLEANUP_INTERVAL:

        cleanup_folder(CAPTURED_FOLDER)
        cleanup_folder(POTHOLE_FOLDER)
        cleanup_folder(NORMAL_FOLDER)

        last_cleanup_time = current_time

    # Exit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ----------------------------
# CLEANUP
# ----------------------------

cap.release()
cv2.destroyAllWindows()