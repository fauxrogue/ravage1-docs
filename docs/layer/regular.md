# Layer Settings - Regular Layer

Regular layers use unique nodes for each channel. You can have an image texture on the Albedo Channel, while using a value slider to set the bump detail. Important to note however, the main layer mapping will control the mapping properties for all the channel nodes if they also are Image Textures.

For the channels, you can use an Image Texture node, RGB node and Value node.

-   RGB nodes will draw a color picker.
-   Value nodes will show a slider.
-   Texture nodes will show the texture's properties.

In the example below, the Albedo, Roughness and Bump channels are controlled by an Image Texture node, the Metallic channel has a value node turned to 1.00 which will make this layer fully metalic but with break up from the other channels.

![](../img/panel_layer_regular.png)
