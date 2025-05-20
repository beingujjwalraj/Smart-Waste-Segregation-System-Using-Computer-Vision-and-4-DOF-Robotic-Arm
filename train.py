from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO('/Users/ujjwalraj/runs/detect/yolov8n-ewaste10/weights/best.pt')

# Open the webcam (0 = default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open webcam.")
    exit()

print("📸 Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference on the frame
    results = model.predict(source=frame, show=False, conf=0.5)

    # Visualize results on the frame
    annotated_frame = results[0].plot()

    # Show the annotated frame
    cv2.imshow("E-waste Detection", annotated_frame)

    # Quit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()