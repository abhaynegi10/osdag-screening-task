import xarray as xr
import plotly.graph_objects as go

# Load dataset
ds = xr.open_dataset("data/screening_task (1).nc")

central_elements = [15, 24, 33, 42, 51, 60, 69, 78, 83]

Mz = []
Vy = []
x = []

pos = 0

for e in central_elements:
    Mz_i = ds.forces.sel(Element=e, Component="Mz_i").values
    Mz_j = ds.forces.sel(Element=e, Component="Mz_j").values
    Vy_i = ds.forces.sel(Element=e, Component="Vy_i").values
    Vy_j = ds.forces.sel(Element=e, Component="Vy_j").values

    x.append(pos); Mz.append(Mz_i); Vy.append(Vy_i)
    pos += 1
    x.append(pos); Mz.append(Mz_j); Vy.append(Vy_j)

# -------- BMD --------
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x, y=Mz, mode="lines+markers"))
fig1.update_layout(
    title="Bending Moment Diagram (Central Girder)",
    xaxis_title="Bridge Length",
    yaxis_title="Mz"
)
fig1.show()

# -------- SFD --------
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x, y=Vy, mode="lines+markers"))
fig2.update_layout(
    title="Shear Force Diagram (Central Girder)",
    xaxis_title="Bridge Length",
    yaxis_title="Vy"
)
fig2.show()
