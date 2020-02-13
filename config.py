import os

GCP_PROJECT = os.getenv("GCP_PROJECT")

class Config:
    PROJECT_ID=GCP_PROJECT
