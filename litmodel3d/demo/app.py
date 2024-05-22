
import gradio as gr
from gradio_litmodel3d import LitModel3D

# print gradio version
print(gr.__version__)

def update_hdr(hdr_upload):
    return gr.update(env_map=hdr_upload.name if hdr_upload else None)

with gr.Blocks() as demo:
    env_map = gr.File(label="HDR Environment Map", file_types=[".hdr"], file_count="single")
    modelupload = gr.File(label="3D Model", file_types=[".obj", ".gltf", ".glb"])
    model3d = LitModel3D(interactive=False)

    tonemapping = gr.Radio(
        value="standard",
        label="Tonemapping",
        choices=["standard", "aces"],
    )
    exposure = gr.Slider(
        value=1.0,
        label="Exposure",
        minimum=0.1,
        maximum=5.0, 
        step=0.1,
    )
    contrast = gr.Slider(
        value=1.0,
        label="Contrast",
        minimum=0.1,
        maximum=2.0, 
        step=0.1,
    )
    tonemapping.change(
        lambda tonemapping: gr.update(tonemapping=tonemapping),
        inputs=[tonemapping],
        outputs=[model3d],
    )
    exposure.change(
        lambda exposure: gr.update(exposure=exposure),
        inputs=[exposure],
        outputs=[model3d],
    )
    contrast.change(
        lambda contrast: gr.update(contrast=contrast),
        inputs=[contrast],
        outputs=[model3d],
    )

    modelupload.change(
        lambda model_upload: gr.update(value=model_upload),
        inputs=[modelupload],
        outputs=[model3d],
    )
    env_map.change(
        update_hdr,
        inputs=[env_map],
        outputs=[model3d],
    )


if __name__ == "__main__":
    demo.launch()
