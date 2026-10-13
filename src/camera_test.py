import argparse
import time

import cv2


def main():
    parser = argparse.ArgumentParser(description="Test camera si FPS")
    parser.add_argument("--camera", type=int, default=0, help="indexul camerei")
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        print("Nu pot deschide camera", args.camera)
        return

    prev = time.perf_counter()
    fps = 0.0
    while True:
        ok, frame = cap.read()
        if not ok:
            print("Nu pot citi imaginea de la camera")
            break

        now = time.perf_counter()
        dt = now - prev
        prev = now
        if dt > 0:
            fps = 0.9 * fps + 0.1 * (1.0 / dt)

        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Camera test (q = iesire)", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()