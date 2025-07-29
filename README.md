Lansing, Michigan Is Losing Its Winters — A 60-Year Climate Data Analysis
This project analyzes over 60 years of daily weather data to quantify how warming trends are reshaping Michigan’s winters, especially through lost sub-freezing days.

Key Findings
- Lansing winters are warming **~0.86°F per decade** on average
- **Sub-freezing days** have declined by ~24 days since 1960
- **Winter lows are warming twice as fast** as summer highs
- Early spring and late fall are changing slower than midwinter

- <img width="989" height="586" alt="image" src="https://github.com/user-attachments/assets/06482980-5acc-45b2-b729-75bb6b880c10" />

<img width="987" height="586" alt="image" src="https://github.com/user-attachments/assets/735ee115-038f-4f4c-9c10-31cc60a20672" />

Code Highlights
- Custom `Temperature_Data` class for organizing and cleaning 60+ years of messy climate records
- Auto-fixes bad entries (e.g., 0°F lows in July) using estimation logic
- Modular design with month/day extraction, validation checks, and reproducible analysis

Planned improvements:
- Time series forecasting
