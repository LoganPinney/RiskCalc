TRADING CALCULATOR – LIGHTWEIGHT GUI APP
========================================

Description:
------------
This is a lightweight desktop GUI application for real-time trading risk calculations, inspired by the aesthetics and simplicity of Windows 95. It uses Python with PySimpleGUI and Matplotlib to offer fast performance, responsive sliders, and an easy-to-use interface.

Core Features:
--------------
- Input stock price and available capital
- Sliders for:
  * Stop-loss percentage
  * Risk per trade percentage
  * Target profit/loss (P&L) ratio
- Real-time updates for:
  * Stop-loss price
  * Target price
  * Share size
  * Risk-to-reward ratios
- Dynamic bar chart showing risk/reward zones

Setup Instructions:
-------------------
1. Install dependencies:

   pip install PySimpleGUI matplotlib

2. Run the application:

   python app.py

3. (Optional) Package for Windows:

   pip install pyinstaller  
   pyinstaller --onefile app.py

Author:
-------
Logan Pinney – 2025

Purpose:
--------
This is part of a greater toolkit to support fast decision-making in day trading, prototyped for private use and future bot integration.

