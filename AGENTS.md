# AGENTS.md

## Agent Overview

This application is designed to be compatible with future integrations involving assistant agents or trading bots that require direct communication with trading strategy inputs.  Python app using PySimpleGUI and Matplotlib that acts as a lightweight trading risk calculator. The app should be styled like a minimalist Win95 GUI. No agents are currently active, but the following design principles are enforced:

### Agent Roles (Planned)

- **ChartAgent**
  - Observes all slider/input updates.
  - Renders the Matplotlib chart and updates visual elements.
  - Will eventually expose a JSON interface for remote rendering if needed.

- **CalcAgent**
  - Monitors UI state.
  - Performs all calculations on profit/loss, stop-loss, and share size.
  - Ensures calculations respect user-defined tolerances.

- **UISyncAgent**
  - Handles all PySimpleGUI updates and synchronization between slider inputs and calculated outputs.
  - Prevents conflicting updates or infinite refresh loops.

### Future Considerations

- Agent wrappers will expose JSON payloads to allow bots to pre-fill trade plans.
- Modular hooks can be extended for WebSocket-based clients or headless versions.
- Safe mode with limited sliders will be available for novice agent control.

---

This document will evolve as the application matures and integration with other components (e.g., CenterPoint API, Ross-style strategy scoring) comes online.

Author: Logan Pinney  
Last Updated: July 2025
