---
layout: post
title: Tiny project - adding useful map layers to finn.no
---

Recently I've been spending a lot of time looking at real estate listings. In Norway, the one stop website for this is finn.no. Over time I've realized there's a couple of things I want to check with every listing that I'm interested in, that I can't do on the website itself. These include:
- check if the house is in a potential flood area
- check the noise levels around the house, from road or train 
- check the ground type in the area, and especially make sure there is no [quick clay](https://en.wikipedia.org/wiki/Quick_clay)

You can find this information using publicly available maps at the Ministry of Environment, the Norwegian Geotechnical Institute and other places. They are also available in a WMS format that can be loaded dynamically using a map viewer like the one available on the [ArcGIS website](https://www.arcgis.com/apps/mapviewer/index.html). With this in mind, I thought it would be great to instantly see the map with the important layers centered on the address of the real estate listing, right in the ad. 

To do this I made a simple Chrome extension that attaches an iframe of the map to a particular element on the ad page. What's great about the Map Viewer in ArcGIS is that it can be configured by its url to a large extent - the map layers included, the address search, even the visibility of the side panel - can all be specified as url parameters. With that, all I have to do is construct a url in the extension and display the iframe. You can find the extension on my [GitHub](https://github.com/branislavjenco/finn-map-layers) if you want to use it yourself.





