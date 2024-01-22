"""
df_csv_excel - Python library for dataframe processing.
"""
import pandas as pd
import os, re, warnings


__version__ = "0.1.1"

def parse_dates(df, date_column_name, format=None):
    def apply_date_parser(date_parser, format=None):
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                df['date_column'] = date_parser(df[date_column_name], errors='coerce', format=format)
            return df['date_column'].values
        except Exception as e:
            print(e)
            return None

    if format is None:
        try:
            # Attempt parsing with default settings
            return apply_date_parser(pd.to_datetime)
        except Exception as e:
            # If default parsing fails, try to extract and use the format from the error
            match = re.search(r'Parsing dates in (.+?) format', str(e))
            if match:
                date_format = match.group(1)
                return apply_date_parser(pd.to_datetime, format=date_format)
            else:
                print(e)
                return None
    else:
        # Parse with the specified format
        return apply_date_parser(pd.to_datetime, format=format)
