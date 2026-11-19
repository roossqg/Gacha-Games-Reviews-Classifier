from pathlib import Path

import pandas as pd
import streamlit as st

from app.sentiment_and_topic.graphs_sentiments import (
    bar,
    boxplot,
    classify_sentiment_by_scores,
    counts,
    histogram,
)


DATASET_PATH = (
    Path(__file__).resolve().parents[1]
    / "sentiment_and_topic"
    / "datasets_by_llm"
    / "vader_sentiment_dataset.csv"
)


def render_sentiments(data: pd.DataFrame) -> None:
    sentiment_counts = data["sentiment"].value_counts()
    total_reviews = len(data)

    st.subheader("📌 Overview")
    positive, neutral, negative, total = st.columns(4)
    positive.metric(
        "😊 Positive reviews",
        f"{sentiment_counts.get('POSITIVE', 0):,}",
        f"{sentiment_counts.get('POSITIVE', 0) / total_reviews:.1%}" if total_reviews else "0%",
    )
    neutral.metric(
        "😐 Neutral reviews",
        f"{sentiment_counts.get('NEUTRAL', 0):,}",
        f"{sentiment_counts.get('NEUTRAL', 0) / total_reviews:.1%}" if total_reviews else "0%",
    )
    negative.metric(
        "😞 Negative reviews",
        f"{sentiment_counts.get('NEGATIVE', 0):,}",
        f"{sentiment_counts.get('NEGATIVE', 0) / total_reviews:.1%}" if total_reviews else "0%",
    )
    total.metric("📝 Total reviews", f"{total_reviews:,}")

    st.divider()
    st.subheader("🎮 Sentiment by game")
    st.caption("Compare the number of positive, neutral, and negative reviews for each game.")
    st.plotly_chart(counts(data), use_container_width=True)

    st.divider()
    st.subheader("📊 Sentiment score distributions")
    st.caption("See how each sentiment score is distributed across its corresponding reviews.")
    score_histograms = histogram(data)
    histogram_columns = st.columns(3)
    for column, title, figure in zip(
        histogram_columns,
        ("😊 Positive", "😞 Negative", "😐 Neutral"),
        score_histograms.values(),
    ):
        with column:
            st.markdown(f"#### {title}")
            st.plotly_chart(figure, use_container_width=True)

    st.divider()
    st.subheader("📦 Score comparison by sentiment")
    st.caption("Box plots make it easy to compare score variation across sentiment classes.")
    score_boxplots = boxplot(data)
    boxplot_columns = st.columns(3)
    for column, title, figure in zip(
        boxplot_columns,
        ("😊 Positive score", "😞 Negative score", "😐 Neutral score"),
        score_boxplots.values(),
    ):
        with column:
            st.markdown(f"#### {title}")
            st.plotly_chart(figure, use_container_width=True)

    st.divider()
    st.subheader("🔤 Frequent words and phrases by sentiment")
    st.caption("Explore the most common terms and phrases in each group of reviews.")
    bar(data)


def main() -> None:
    st.title("🧭 Sentiment Analysis & Topics")
    st.write(
        "Explore players' reactions in reviews and, soon, the main topics discussed "
        "about each game."
    )

    sentiment_tab, topics_tab = st.tabs(["💭 Sentiments", "🏷️ Topics"])

    with sentiment_tab:
        pre_data = pd.read_csv(DATASET_PATH)
        data = classify_sentiment_by_scores(pre_data)
        render_sentiments(data)

    with topics_tab:
        st.subheader("🏷️ Topic analysis")
        st.info("Topic analysis will be available soon.")


if __name__ == "__main__":
    main()
