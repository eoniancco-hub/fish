# 發電機維修廣告影片

這是 HyperFrames 直式廣告 composition，尺寸 `1080x1920`，長度 15 秒。

預覽：

```bash
cd ad-video
npx hyperframes preview
```

檢查：

```bash
cd ad-video
npx hyperframes lint
npx hyperframes validate
npx hyperframes inspect
```

輸出 MP4：

```bash
cd ad-video
npx hyperframes render
```

目前這台環境沒有 `node` / `npx` / `ffmpeg`，所以我先建立 composition 原始檔。安裝 Node 22+ 與 FFmpeg 後即可渲染。
