import os
import subprocess
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI

class Item(BaseModel):
    link: str

def _env():
    global ALWAYS_LARGEST, MAX_HEIGHT, MAX_WIDTH
    MAX_WIDTH=os.getenv("MAX_WIDTH",7680)
    MAX_HEIGHT=os.getenv("MAX_HEIGHT",4320)
    ALWAYS_LARGEST=os.getenv("ALWAYS_LARGEST",False)
def rename(link):
    if os.path.isfile("/app/export/dezoomified.jpg"):
        new_name=link.rpartition("/")[0].rpartition("/")[2]
        os.rename("/app/export/dezoomified.jpg","/app/export/"+str(new_name)+".jpg")
app = FastAPI()

@app.post("/")
def link(inp : Item):
    _env()
    if ALWAYS_LARGEST:
        subprocess.run(["/app/dezoomify-rs",inp.link,"-l"],cwd="/app/export")
        rename(inp.link)
    else:
        subprocess.run(["/app/dezoomify-rs",inp.link,"-h",str(MAX_HEIGHT),"-w",str(MAX_WIDTH)],cwd="/app/export")
        rename(inp.link)
@app.get("/")
def nom_nom():
    _env()
    print("( ^_^)3 nom nom")
    print("I will nom nom all the Files in the import directory")
    files=[x for x in subprocess.run("find /app/import/*", shell=True, capture_output=True, text=True).stdout.split('\n') if x!=""]
    if files!=[]:
        for _ in files:
            with open(_) as f:
                l = [x for x in [line.rstrip() for line in f] if x!=""]
                for oops in l:
                    try:
                        if ALWAYS_LARGEST:
                            subprocess.run(["/app/dezoomify-rs",oops,"-l"],cwd="/app/export")
                            rename(oops)
                        else:
                            subprocess.run(["/app/dezoomify-rs",oops,"-h",str(MAX_HEIGHT),"-w",str(MAX_WIDTH)],cwd="/app/export")
                            rename(oops)
                    except: 
                        print("*CRUNCH*")
            subprocess.run(["rm "+_])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9420)

