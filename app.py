import pandas as pd
import matplotlib.pyplot as plt
import gradio as gr
import os

DATASET_PATH = "learning_content_dataset_100k.csv"


def analyze_dataset(file):
  
    if file is not None:
        csv_path = file.name
        status = "User uploaded dataset is used"
    else:
        if os.path.exists(DATASET_PATH):
            csv_path = DATASET_PATH
            status = " Uploaded dataset not found, using existing dataset"
        else:
            return " No dataset found. Please upload a CSV file.", None, None

    df = pd.read_csv(csv_path)
    df["date"] = pd.to_datetime(df["date"])

  
    total_views = df["views"].sum()
    total_likes = df["likes"].sum()
    total_comments = df["comments"].sum()
    avg_duration = round(df["duration_minutes"].mean(), 2)

    top_content = df.groupby("content_type")["views"].sum().idxmax()
    top_course = df.groupby("course")["views"].sum().idxmax()

    insights = f"""
{status}

Total Views: {total_views}
Total Likes: {total_likes}
Total Comments: {total_comments}
Average Duration (minutes): {avg_duration}

Most Viewed Content Type: {top_content}
Most Popular Course: {top_course}
"""

    plt.figure()
    df.groupby("content_type")["views"].sum().plot(kind="bar")
    plt.title("Views by Content Type")
    plt.xlabel("Content Type")
    plt.ylabel("Views")
    plt.tight_layout()
    plt.savefig("content_views.png")
    plt.close()

  
    plt.figure()
    df["date"].value_counts().sort_index().plot()
    plt.title("Upload Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Uploads")
    plt.tight_layout()
    plt.savefig("upload_trend.png")
    plt.close()

    return insights, "content_views.png", "upload_trend.png"


app = gr.Interface(
    fn=analyze_dataset,
    inputs=gr.File(label="Upload CSV file (optional)"),
    outputs=[
        gr.Textbox(label="📊 Study Insights"),
        gr.Image(label="Views by Content Type"),
        gr.Image(label="Upload Trend")
    ],
    title="📈 Learning Content Analysis Dashboard",
    description="Upload your dataset or analyze the existing dataset using OS-based file handling"
)

app.launch()
