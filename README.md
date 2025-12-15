Data Understanding

The Spotify Global Chart 2024 dataset consists of weekly rankings of the Top 200 most-streamed songs worldwide on Spotify throughout 2024. The dataset contains 10,600 observations and 10 attributes, representing track-level performance metrics and metadata.

The dataset includes both numerical variables, such as chart rank, streaming counts, and chart longevity (rank, streams, weeks_on_chart), as well as categorical variables, including artist names, track titles, and source identifiers.

All columns contain complete data with no missing values, indicating a high level of data quality. However, preliminary inspection reveals potential redundancies (e.g., overlapping source columns) and logical considerations (such as new chart entries reflected in previous_rank values), which will be addressed in the data cleaning phase.

The data cleaning process involved standardizing column names, removing redundant source-related attributes, and handling chart entry logic. Additional features were engineered to identify new chart entries and track rank movement across weeks. The cleaned dataset was saved for subsequent exploratory data analysis.