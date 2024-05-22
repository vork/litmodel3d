
import gradio as gr
from app import demo as app
import os

_docs = {'LitModel3D': {'description': 'Creates a component allows users to upload or view 3D Model files (.obj, .glb, .stl, .gltf, .splat, or .ply).\n', 'members': {'__init__': {'value': {'type': 'str | Callable | None', 'default': 'None', 'description': 'path to (.obj, .glb, .stl, .gltf, .splat, or .ply) file to show in model3D viewer. If callable, the function will be called whenever the app loads to set the initial value of the component.'}, 'env_map': {'type': 'str | None', 'default': 'None', 'description': 'path to environment map file to show in model3D viewer. If callable, the function will be called whenever the app loads to set the initial value of the environment map.'}, 'tonemapping': {'type': 'Literal["standard", "aces"] | None', 'default': 'None', 'description': 'tonemapping algorithm to use for rendering the scene. Should be one of "standard" or "aces". If not provided, defaults to "standard".'}, 'exposure': {'type': 'float', 'default': '1.0', 'description': 'exposure value to use for rendering the scene. Should be a float, increase this value to make the scene brighter, decrease to make it darker. Affects the exposure property of the camera.'}, 'contrast': {'type': 'float', 'default': '1.0', 'description': 'contrast value to use for rendering the scene. Should be a float, increase this value to make the scene more contrasted, decrease to make it less contrasted. Affects the contrast property of the camera.'}, 'clear_color': {'type': 'tuple[float, float, float, float] | None', 'default': 'None', 'description': 'background color of scene, should be a tuple of 4 floats between 0 and 1 representing RGBA values.'}, 'camera_position': {'type': 'tuple[\n    int | float | None,\n    int | float | None,\n    int | float | None,\n]', 'default': 'None, None, None', 'description': 'initial camera position of scene, provided as a tuple of `(alpha, beta, radius)`. Each value is optional. If provided, `alpha` and `beta` should be in degrees reflecting the angular position along the longitudinal and latitudinal axes, respectively. Radius corresponds to the distance from the center of the object to the camera.'}, 'zoom_speed': {'type': 'float', 'default': '1', 'description': 'the speed of zooming in and out of the scene when the cursor wheel is rotated or when screen is pinched on a mobile device. Should be a positive float, increase this value to make zooming faster, decrease to make it slower. Affects the wheelPrecision property of the camera.'}, 'pan_speed': {'type': 'float', 'default': '1', 'description': 'the speed of panning the scene when the cursor is dragged or when the screen is dragged on a mobile device. Should be a positive float, increase this value to make panning faster, decrease to make it slower. Affects the panSensibility property of the camera.'}, 'height': {'type': 'int | str | None', 'default': 'None', 'description': 'The height of the model3D component, specified in pixels if a number is passed, or in CSS units if a string is passed.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.'}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'every': {'type': 'float | None', 'default': 'None', 'description': "If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute."}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will allow users to upload a file; if False, can only be used to display files. If not provided, this is inferred based on whether the component is used as an input or output.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'key': {'type': 'int | str | None', 'default': 'None', 'description': 'if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.'}}, 'postprocess': {'value': {'type': 'str | Path | None', 'description': 'Expects function to return a {str} or {pathlib.Path} filepath of type (.obj, .glb, .stl, or .gltf)'}}, 'preprocess': {'return': {'type': 'str | None', 'description': 'Passes the uploaded file as a {str} filepath to the function.'}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the LitModel3D changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'upload': {'type': None, 'default': None, 'description': 'This listener is triggered when the user uploads a file into the LitModel3D.'}, 'edit': {'type': None, 'default': None, 'description': 'This listener is triggered when the user edits the LitModel3D (e.g. image) using the built-in editor.'}, 'clear': {'type': None, 'default': None, 'description': 'This listener is triggered when the user clears the LitModel3D using the X button for the component.'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'LitModel3D': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_litmodel3d`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  
</div>

An improved Model3D component with environment map support
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_litmodel3d
```

## Usage

```python

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

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `LitModel3D`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["LitModel3D"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["LitModel3D"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, passes the uploaded file as a {str} filepath to the function.
- **As output:** Should return, expects function to return a {str} or {pathlib.Path} filepath of type (.obj, .glb, .stl, or .gltf).

 ```python
def predict(
    value: str | None
) -> str | Path | None:
    return value
```
""", elem_classes=["md-custom", "LitModel3D-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          LitModel3D: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
