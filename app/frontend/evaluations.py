import streamlit as st



def render_dashboard_evaluation() -> None:
    st.subheader("🖥️ Dashboard")
    st.caption("Metrics will be available when the benchmark pipeline is implemented.")

    load_time, completion, failures = st.columns(3)
    load_time.metric("Load time", "N/A")
    completion.metric("Task completion", "N/A")
    failures.metric("Rendering failures", "N/A")




def render_model_evaluation() -> None:
    st.subheader("🤖 Models")
    st.caption("Metrics are unavailable until models and reference data are ready.")

    accuracy, f1, balanced = st.columns(3)
    accuracy.metric("Accuracy", "N/A")
    f1.metric("Macro F1", "N/A")
    balanced.metric("Balanced Accuracy", "N/A")



def render_explainers() -> None:
    st.subheader("🔎 Model Explainability")
    st.info(
        "Explanations require trained models and evaluation samples with "
        "reference labels."
    )

    global_tab, local_tab = st.tabs(
        ["🌐 Global View", "📍 Local Examples"]
    )
   

def main() -> None:
   
    dashboard_tab, models_tab, explainers_tab = st.tabs(
        ["🖥️ Dashboard", "🤖 Models", "🔎 Explainability"]
    )
    with dashboard_tab:
        render_dashboard_evaluation()
    with models_tab:
        render_model_evaluation()
    with explainers_tab:
        render_explainers()


if __name__ == "__main__":
    main()
