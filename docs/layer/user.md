# Layer Settings - Blank/User Layer

Blank layers are layers that are controlled by nodes created by the user.

This allows you to reuse nodes and possibly be more efficient, the functionality is added so as not to limit you to use the addon's interface alone but to have control over your layers.

![](../img/gifs/layer_blank.gif)

---

## Node Editor Operator

When you create a blank layer, all the preview layer operators will disappear and you will be left with the "Open Node Editor" operator. This will open a node editor and make the relevant node the active node. All you will have to do is tab into the specified blank node group and set up your layer.

Note that tampering with the nodes in the main node tree will possibly break the material's compatibility with the addon.

![](../img/panel_layer_blank_operators.png)

## Channels

Channels for the blank layers are similar to other layers, however, they cannot be expanded as their properties are controlled in the node editor.

![](../img/panel_layer_blank_channels.png)

## Inputs

Any created node inputs will be shown as below. For any property that you would like to change on the fly, feel free to create a group input that will allow for this when the layer is active.

![](../img/panel_layer_blank_inputs.png)
