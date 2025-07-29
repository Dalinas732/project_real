# Lansing, Michigan Is Losing Its Winters — A 60-Year Climate Data Analysis

This project analyzes over 60 years of daily weather data to quantify how warming trends are reshaping Michigan’s winters, especially through lost sub-freezing days.

---

## 📈 Key Findings

- **Lansing winters are warming ~0.86°F per decade** on average  
- **Sub-freezing days have declined by ~24 days** since 1960  
- **Winter lows are warming nearly twice as fast** as summer highs  
- Early spring and late fall are changing slower than midwinter  

---

## 📊 Visuals

### December Temperature Trends (1960–2024)
![December Temperature Trends](plots/december_trend.png)

### July Temperature Trends (1960–2024)
![July Temperature Trends](plots/july_trend.png)

---

## 🧠 Code Highlights

- Custom `Temperature_Data` class for organizing and cleaning 60+ years of messy climate records  
- Auto-fixes corrupted entries (e.g., 0°F lows in July) using imputation logic  
- Modular design with month/day extraction, data validation, and reproducible analysis  
- Uses `pandas`, `numpy`, and `matplotlib` for analysis and visualization

---

## 📄 Full Report

A detailed PDF summary of methodology, results, and context is available here:  
[**Project_Summary.pdf**](Project_Summary.pdf)

---

## 📁 Repository Structure

- `src/class_history/` — Code for data cleaning and temperature class  
- `tests/` — Sanity checks for data validity across months/years  
- `Temp_Trends/`, `Number of Freezing Days/` — Notebooks for trend analysis  
- `data/` — Raw and cleaned spreadsheet data (1960–2024)  
- `temp_script.py` — Script for generating plots using the cleaned dataset  

---

## 🔮 Planned Improvements

- Add ARIMA or Prophet-based **time series forecasting**  
- Visualize confidence intervals for future winter projections  
- Build a **Streamlit dashboard** for interactive exploration

---

## 🛠 Requirements

- Python (>=3.8)  
- Jupyter Notebook  
- Git  
- `pandas`, `numpy`, `matplotlib`  

To run analysis:  
Ensure `temp_script.py` and `cleandata.xlsx` are in the working directory of your Jupyter notebook.

---

