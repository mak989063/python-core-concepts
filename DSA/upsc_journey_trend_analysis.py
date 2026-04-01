import pandas as pd
import plotly.graph_objects as go

data = {
    "Year": [2023, 2024, 2025],
    "Paper1": [16, 57, 77.34],
    "Paper2": [40, 57, 62],
    "Preparation": ["0%", "20%", "50%"],
    "Remarks": [
        "No preparation",
        "Partial prep, lack of discipline",
        "Better prep, work pressure affected consistency"
    ]
}

df = pd.DataFrame(data)

fig = go.Figure()

# Paper 1 (GS)
fig.add_trace(go.Bar(
    x=df["Year"],
    y=df["Paper1"],
    name="Paper 1 (GS)",
    customdata=list(zip(df["Preparation"], df["Remarks"])),
    hovertemplate=
    "<b>Year:</b> %{x}<br>" +
    "<b>GS Marks:</b> %{y}<br>" +
    "<b>Preparation:</b> %{customdata[0]}<br>" +
    "<b>Insight:</b> %{customdata[1]}<extra></extra>"
))

# Paper 2 (CSAT)
fig.add_trace(go.Bar(
    x=df["Year"],
    y=df["Paper2"],
    name="Paper 2 (CSAT)",
    customdata=list(zip(df["Preparation"], df["Remarks"])),
    hovertemplate=
    "<b>Year:</b> %{x}<br>" +
    "<b>CSAT Marks:</b> %{y}<br>" +
    "<b>Preparation:</b> %{customdata[0]}<br>" +
    "<b>Insight:</b> %{customdata[1]}<extra></extra>"
))

# Layout
fig.update_layout(
    title="Mani's UPSC Prelims Journey Analysis",
    xaxis_title="Year",
    yaxis_title="Marks",
    barmode='group',
    hovermode="x unified"
)

fig.show()