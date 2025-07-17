# AGENTS.md

## Overview

This project is structured with modular agents in mind. Each agent manages a specific responsibility such as calculation, UI synchronization, or chart rendering. While the initial app is single-process and UI-based, the agent framework is future-proofed for eventual automation, bot integration, or remote control.

---

## Agent Roles

### 1. `CalcAgent`
- Calculates stop-loss, target price, share size, risk per trade, and reward.
- Reacts to slider/input state changes.
- Outputs human-readable and JSON-format results.

### 2. `ChartAgent`
- Uses Matplotlib to render a bar chart showing entry, stop-loss, and target.
- Updates the chart dynamically based on CalcAgent’s output.
- (Future) Will support JSON-based remote chart rendering.

### 3. `UISyncAgent`
- Manages all PySimpleGUI updates.
- Ensures all user-facing values stay in sync across inputs, sliders, and charts.
- Prevents feedback loops or broken state from rapid changes.

---

## Commit Message Guidelines

Use the following format for commits:


### Types
- `feat`: New feature (e.g. `feat: calc - added risk-to-reward calculator`)
- `fix`: Bug fix (e.g. `fix: chart - resolved rendering error on slider change`)
- `refactor`: Code cleanup with no functionality change
- `docs`: Documentation updates
- `chore`: Build, dependency, or meta changes
- `test`: Adds or updates tests

---

## Pull Request (PR) Guidelines

1. **Branch Naming**: Use `agent/<agent-name>/<brief-purpose>`
   - Example: `agent/chart/fix-redraw-glitch`

2. **PR Title Format**: Match commit format (e.g. `feat: ui - added slider constraints`)

3. **Checklist Before Opening PR**:
   - [ ] Code runs without errors (`python app.py`)
   - [ ] New features include inline comments
   - [ ] All UI inputs maintain sync
   - [ ] Chart renders properly (or failure is logged cleanly)

4. **PR Review Expectations**:
   - Keep changes < 400 LOC when possible
   - Use markdown in PRs to explain before/after behavior
   - Mention the relevant agent you're working with

---

## Future Agent Lifecycle Considerations

Each agent will eventually:
- Expose an interface (e.g. CLI, JSON-RPC, or WebSocket)
- Have optional AI or rule-based decision trees
- Be testable in isolation

Design decisions made now should keep this lifecycle in mind.

---

Author: Logan Pinney  
Last Updated: July 2025