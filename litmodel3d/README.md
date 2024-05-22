---
tags: [gradio-custom-component, Model3D, model 3d, 3d, model, illumination, light, environment map, env map]
title: gradio_litmodel3d
short_description: An improved Model3D component with environment map support
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_litmodel3d`
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  

An improved Model3D component with environment map support

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

## `LitModel3D`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
str | Callable | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">path to (.obj, .glb, .stl, .gltf, .splat, or .ply) file to show in model3D viewer. If callable, the function will be called whenever the app loads to set the initial value of the component.</td>
</tr>

<tr>
<td align="left"><code>env_map</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">path to environment map file to show in model3D viewer. If callable, the function will be called whenever the app loads to set the initial value of the environment map.</td>
</tr>

<tr>
<td align="left"><code>tonemapping</code></td>
<td align="left" style="width: 25%;">

```python
Literal["standard", "aces"] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">tonemapping algorithm to use for rendering the scene. Should be one of "standard" or "aces". If not provided, defaults to "standard".</td>
</tr>

<tr>
<td align="left"><code>exposure</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>1.0</code></td>
<td align="left">exposure value to use for rendering the scene. Should be a float, increase this value to make the scene brighter, decrease to make it darker. Affects the exposure property of the camera.</td>
</tr>

<tr>
<td align="left"><code>contrast</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>1.0</code></td>
<td align="left">contrast value to use for rendering the scene. Should be a float, increase this value to make the scene more contrasted, decrease to make it less contrasted. Affects the contrast property of the camera.</td>
</tr>

<tr>
<td align="left"><code>clear_color</code></td>
<td align="left" style="width: 25%;">

```python
tuple[float, float, float, float] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">background color of scene, should be a tuple of 4 floats between 0 and 1 representing RGBA values.</td>
</tr>

<tr>
<td align="left"><code>camera_position</code></td>
<td align="left" style="width: 25%;">

```python
tuple[
    int | float | None,
    int | float | None,
    int | float | None,
]
```

</td>
<td align="left"><code>None, None, None</code></td>
<td align="left">initial camera position of scene, provided as a tuple of `(alpha, beta, radius)`. Each value is optional. If provided, `alpha` and `beta` should be in degrees reflecting the angular position along the longitudinal and latitudinal axes, respectively. Radius corresponds to the distance from the center of the object to the camera.</td>
</tr>

<tr>
<td align="left"><code>zoom_speed</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>1</code></td>
<td align="left">the speed of zooming in and out of the scene when the cursor wheel is rotated or when screen is pinched on a mobile device. Should be a positive float, increase this value to make zooming faster, decrease to make it slower. Affects the wheelPrecision property of the camera.</td>
</tr>

<tr>
<td align="left"><code>pan_speed</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>1</code></td>
<td align="left">the speed of panning the scene when the cursor is dragged or when the screen is dragged on a mobile device. Should be a positive float, increase this value to make panning faster, decrease to make it slower. Affects the panSensibility property of the camera.</td>
</tr>

<tr>
<td align="left"><code>height</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The height of the model3D component, specified in pixels if a number is passed, or in CSS units if a string is passed.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will display label.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will place the component in a container - providing some extra padding around the border.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will allow users to upload a file; if False, can only be used to display files. If not provided, this is inferred based on whether the component is used as an input or output.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will be hidden.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>

<tr>
<td align="left"><code>key</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the LitModel3D changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `upload` | This listener is triggered when the user uploads a file into the LitModel3D. |
| `edit` | This listener is triggered when the user edits the LitModel3D (e.g. image) using the built-in editor. |
| `clear` | This listener is triggered when the user clears the LitModel3D using the X button for the component. |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Is passed, passes the uploaded file as a {str} filepath to the function.
- **As input:** Should return, expects function to return a {str} or {pathlib.Path} filepath of type (.obj, .glb, .stl, or .gltf).

 ```python
 def predict(
     value: str | None
 ) -> str | Path | None:
     return value
 ```
 
