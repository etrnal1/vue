from fastapi import FastAPI, BackgroundTasks
import subprocess
from pydantic import BaseModel

app = FastAPI()

class CutVideoInput(BaseModel):
    input_file: str
    output_file: str
    start_time: str
    duration: str

@app.post("/cut_video")
async def cut_video(data: CutVideoInput, background_tasks: BackgroundTasks):
    background_tasks.add_task(run_ffmpeg, data.input_file, data.output_file, data.start_time, data.duration)
    return {"message": "Video processing started."}
@app.get("/")
def read_root():
    return {"Hello": "World"}
def run_ffmpeg(input_file: str, output_file: str, start_time: str, duration: str):
    try:
        output=subprocess.check_output(
            f'ffmpeg -i "{input_file}" -ss "{start_time}" -t "{duration}" -c copy -vsync 1 "{output_file}"', 
            shell=True,
            stderr=subprocess.STDOUT
        )
        # print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"ffmpeg error: {e.output}")

