from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from removebg import remove

app = FastAPI()

@app.post("/remove_bg")
async def remove_background(image: UploadFile = File(...)):
    # Guardar la imagen subida
    with open(image.filename, "wb") as buffer:
        buffer.write(image.file.read())

    # Eliminar el fondo de la imagen
    output_file = remove(image.filename)

    # Devolver la imagen resultante
    return FileResponse(output_file, media_type="image/png", filename="output.png")
