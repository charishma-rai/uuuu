# Crime Scene Prompt Engine & Templates

This directory contains data-driven prompt templates used by the AI notebook to construct rich visual prompts for image generation models (e.g., Stable Diffusion, Midjourney, FLUX, Imagen).

## Directory Structure
- `themes.json`: Master atmospheric themes (Gothic Mansion, 1940s Noir, Orient Express, etc.).
- `locations.json`: Specific rooms and architectural settings.
- `lighting.json`: Lighting modifiers (Candlelight, Gaslamp glow, Neon, Moonlight).
- `weather.json`: Atmospheric weather conditions (Torrential Rain, Dense Fog, Blizzard).

## How Notebooks Construct Crime Scene Prompts
The game engine combines elements dynamically:
`[Theme.description] + [Location.keywords] + [Lighting.prompt_modifier] + [Weather.prompt_modifier] + [Evidence items]`

No images are hardcoded in this directory. All crime scene illustrations are generated at runtime.
