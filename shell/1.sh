awk -F '\\|\\+\\|' '{print $2}' 1.txt
/Users/mac/Movies/2023-08-04\ 23-39-51.mp4
/Users/mac/Movies/z112.mp4
00:00:00 
1:33:36


"input_file": "/Users/mac/Movies/2023-08-04 23-39-51.mp4",
  "output_file": "/Users/mac/Movies/z112.mp4",
  "start_time": "00:00:00",
  "duration": "01:00:00"



  你的 JSON 对象中似乎缺少了一个逗号 (,)，应该在 `"output_file": "/Users/mac/Movies/z112.mp4"` 后面添加一个逗号。另外，文件路径中的空格可以保留，不需要使用反斜杠进行转义。

修正后的 JSON 对象应该如下所示：

```json
{
  "input_file": "/Users/mac/Movies/2023-08-04 23-39-51.mp4",
  "output_file": "/Users/mac/Movies/z112.mp4",
  "start_time": "00:00:00",
  "duration": "01:00:00"
}
```

然后，你可以使用此 JSON 对象作为 POST 请求的请求体发送到 `/cut_video` 路由。

如果你使用的是 FastAPI 自动生成的交互式 API 文档，你只需要在相应的字段中填入这些值，然后点击 "Try it out" 按钮。

如果你使用的是一个 HTTP 客户端，例如 curl，你的命令可能看起来像这样：

```bash
curl -X POST "http://localhost:8000/cut_video" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"input_file\":\"/Users/mac/Movies/2023-08-04 23-39-51.mp4\",\"output_file\":\"/Users/mac/Movies/z112.mp4\",\"start_time\":\"00:00:00\",\"duration\":\"01:00:00\"}"
```

请注意，你需要将 `localhost:8000` 替换为你的 FastAPI 应用的实际 URL 和端口，如果你已经更改了默认设置。