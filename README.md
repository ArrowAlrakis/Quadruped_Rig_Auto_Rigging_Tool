# Quadruped_Rig_Auto_Rigging_Tool
Python Auto Rig Tool for Quadruped Creatures
Created by Arrow Lyu. Designed originally for Rimerock, my original dragon character.

# Overview
This is a Python-based Auto Rigging Tool built for quadruped creatures in Autodesk Maya.
Originally developed to rig a fantasy dragon (with fins, crests, whiskers, and tail spikes), the script supports both standard and custom anatomical features.

It generates a clean joint structure, controllers, and constraints — making it easier for artists to move directly into skin weighting and animation.


# Key Features
Auto joint generation (spine, legs, neck, tail)
Custom joint count per region (adjustable in code)
Special support for: Fins, Spikes, Whiskers, Crests
Proxy-based rig logic
Skin weight transfer from proxy to final mesh
Scripted 100% in Python (Maya commands and pymel)
Works in Maya (tested in versions 2019–2025)

# Demo
▶ Quadruped_AutoRig_demo_v01

(Note: Some helper modules used in the script are private, learned from my professor, Dennis Turner, and not shared publicly due to the instructor's request. However, core functionality and design are fully visible in the demo.)

# How to Use
1. Open Maya and load your quadruped model
2. Run the Python script in Maya script editor
3. Move proxy locators to fit your model shape
4. Choose which body parts to include in your rig (in script)
5. Run final build — your rig is ready for weight painting
6. (Optional) Run the skin weight transfer section to move weights from proxy to render mesh

# Notes
This project was originally developed as a personal rigging tool for my original character.
The code is hard-coded but well-structured and commented. Advanced users can easily customize it for other creatures.
External dependencies (e.g., helper modules from Dennis Turner) are not required for the tool to function in its base form.

# About the Author
This tool was developed by Arrow Lyu, a game art designer with experience in rigging and scripting, aiming to bridge art and technical workflows. It reflects an interest in character TD work and tech art pipelines for games and animation.
