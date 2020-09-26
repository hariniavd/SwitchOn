# SwitchOn

This is an Windows Application build on Python. 

In this Application we have a desktop application that will be used to catch defects in products as
they pass by on an assembly line. Defects will be identified by matching images of the products
taken by a camera with images of known good parts.

Main Screen:
- There are two tabs in the UI, one is Analytics Tabs and other is Image Gallery Tab. 
- The Opening Screen has Analytics Tab by Default, which asks for User Selection of an SKU Product Name. 

Analytics Tab:
- Initially it is loaded with a drop-down, where we can select an required SKU.
- When an SKU is selected, we fetch the selected SKU's data for 4 hours and represent the data in a Bar Graph representation.
- On different selection of SKU's, the Bar Graph is changes as per the data it receives.

Image Gallery Tab:
- When Image Gallery Tab is open, images are displayed in a Grid layout.
- There are options to filter All, Good and Bad items respectively.
- On click of an image, a dialog box appears which has the selected image
