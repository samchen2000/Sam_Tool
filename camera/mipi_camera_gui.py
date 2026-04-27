#!/usr/bin/env python3
"""
簡易 MIPI CSI Camera GUI - Raspberry Pi 5

功能：
- 顯示即時影像
- 右側控制面板：亮度、對比、飽和、色相、R/G/B 倍率
- 每個參數提供滑桿與 +/- 按鈕

依賴：opencv-python, pillow, numpy
"""
import sys
import time
try:
    import cv2
except Exception:
    print("請安裝 opencv-python：pip install opencv-python")
    raise
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class CameraGUI:
    def __init__(self, root, cam_index=0, width=640, height=480):
        self.root = root
        self.root.title("MIPI Camera GUI")
        self.width = width
        self.height = height

        # 相機初始化（嘗試使用 V4L2）
        try:
            self.cap = cv2.VideoCapture(cam_index, cv2.CAP_V4L2)
        except Exception:
            self.cap = cv2.VideoCapture(cam_index)
        if not self.cap.isOpened():
            # fallback to default
            self.cap = cv2.VideoCapture(cam_index)
        # 設定解析度
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        # 參數（預設）
        self.params = {
            'brightness': tk.DoubleVar(value=0.0),     # -100 .. +100 (offset)
            'contrast': tk.DoubleVar(value=1.0),       # 0.0 .. 3.0 (alpha)
            'saturation': tk.DoubleVar(value=1.0),     # 0.0 .. 3.0
            'hue': tk.DoubleVar(value=0.0),            # -180 .. 180
            'r_mul': tk.DoubleVar(value=1.0),          # 0.0 .. 2.0
            'g_mul': tk.DoubleVar(value=1.0),
            'b_mul': tk.DoubleVar(value=1.0),
        }

        self._build_ui()

        self.running = True
        self.update_interval = 30  # ms
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
        self._update_frame()

    def _build_ui(self):
        main = ttk.Frame(self.root)
        main.pack(fill=tk.BOTH, expand=True)

        # 左邊顯示區
        left = ttk.Frame(main)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.image_label = ttk.Label(left)
        self.image_label.pack(fill=tk.BOTH, expand=True)

        # 右邊控制區
        right = ttk.Frame(main, width=300)
        right.pack(side=tk.RIGHT, fill=tk.Y)

        # helper to add control rows
        def add_control(name, var, from_, to_, resolution):
            row = ttk.Frame(right)
            row.pack(fill=tk.X, padx=6, pady=4)
            lbl = ttk.Label(row, text=name, width=10)
            lbl.pack(side=tk.LEFT)
            minus = ttk.Button(row, text='-', width=3, command=lambda v=var: v.set(max(from_, v.get()-resolution)))
            minus.pack(side=tk.LEFT, padx=(4,2))
            scale = ttk.Scale(row, variable=var, orient=tk.HORIZONTAL, from_=from_, to=to_, length=150)
            scale.pack(side=tk.LEFT, padx=2)
            plus = ttk.Button(row, text='+', width=3, command=lambda v=var: v.set(min(to_, v.get()+resolution)))
            plus.pack(side=tk.LEFT, padx=(2,4))
            val = ttk.Label(row, textvariable=var, width=6)
            val.pack(side=tk.LEFT)

        add_control('Brightness', self.params['brightness'], -100.0, 100.0, 1.0)
        add_control('Contrast', self.params['contrast'], 0.0, 3.0, 0.05)
        add_control('Saturation', self.params['saturation'], 0.0, 3.0, 0.05)
        add_control('Hue', self.params['hue'], -180.0, 180.0, 1.0)
        add_control('R_mul', self.params['r_mul'], 0.0, 2.0, 0.05)
        add_control('G_mul', self.params['g_mul'], 0.0, 2.0, 0.05)
        add_control('B_mul', self.params['b_mul'], 0.0, 2.0, 0.05)

        btn_row = ttk.Frame(right)
        btn_row.pack(fill=tk.X, padx=6, pady=8)
        tk.Button(btn_row, text='Reset', command=self._reset_params).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_row, text='Snapshot', command=self._save_snapshot).pack(side=tk.LEFT, padx=4)

    def _reset_params(self):
        self.params['brightness'].set(0.0)
        self.params['contrast'].set(1.0)
        self.params['saturation'].set(1.0)
        self.params['hue'].set(0.0)
        self.params['r_mul'].set(1.0)
        self.params['g_mul'].set(1.0)
        self.params['b_mul'].set(1.0)

    def _save_snapshot(self):
        ret, frame = self.cap.read()
        if not ret:
            print('Snapshot failed')
            return
        out = self._apply_adjustments(frame)
        ts = int(time.time())
        fname = f'snapshot_{ts}.png'
        cv2.imwrite(fname, out)
        print('Saved', fname)

    def _apply_adjustments(self, frame):
        # frame: BGR
        img = frame.astype(np.float32)

        # apply RGB multipliers (OpenCV uses BGR order)
        b_mul = float(self.params['b_mul'].get())
        g_mul = float(self.params['g_mul'].get())
        r_mul = float(self.params['r_mul'].get())
        img[..., 0] *= b_mul
        img[..., 1] *= g_mul
        img[..., 2] *= r_mul

        # contrast and brightness
        contrast = float(self.params['contrast'].get())
        brightness = float(self.params['brightness'].get())
        img = img * contrast + brightness

        # convert to uint8 for HSV ops
        img = np.clip(img, 0, 255).astype(np.uint8)

        # convert to HSV to modify hue & saturation
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
        # OpenCV H range: 0-179, S:0-255, V:0-255
        hue_shift = float(self.params['hue'].get())
        sat_mul = float(self.params['saturation'].get())
        hsv[..., 0] = (hsv[..., 0] + (hue_shift * 179.0 / 360.0)) % 180.0
        hsv[..., 1] = np.clip(hsv[..., 1] * sat_mul, 0, 255)

        img2 = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
        return img2

    def _update_frame(self):
        if not self.running:
            return
        ret, frame = self.cap.read()
        if not ret:
            # show black frame on failure
            frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        else:
            # resize to display size to keep UI responsive
            frame = cv2.resize(frame, (self.width, self.height))

        out = self._apply_adjustments(frame)

        # convert BGR -> RGB -> PIL Image
        rgb = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        # keep reference
        self.image_label.imgtk = imgtk
        self.image_label.configure(image=imgtk)

        self.root.after(self.update_interval, self._update_frame)

    def _on_close(self):
        self.running = False
        try:
            if self.cap and self.cap.isOpened():
                self.cap.release()
        except Exception:
            pass
        self.root.quit()


def main():
    root = tk.Tk()
    app = CameraGUI(root, cam_index=0, width=640, height=480)
    root.mainloop()


if __name__ == '__main__':
    main()
