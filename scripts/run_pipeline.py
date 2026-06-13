"""
Master execution script for Bluestock Mutual Fund Analytics Project
"""

import os

print("Running ETL Pipeline...")
os.system("python scripts\\etl_pipeline.py")

print("Loading Data to SQLite...")
os.system("python scripts\\load_to_sqlite.py")

print("Computing Metrics...")
os.system("python scripts\\compute_metrics.py")

print("Running Recommender...")
os.system("python scripts\\recommender.py")

print("Pipeline Completed Successfully!")