import sys
sys.path.append(".")

import xarray as xr
import plotly.graph_objects as go
from node import nodes
from element import members

ds = xr.open_dataset("data/screening_task (1).nc")

girders = {
    "G1": [13,22,31,40,49,58,67,76,81],
    "G2": [14,23,32,41,50,59,68,77,82],
    "G3": [15,24,33,42,51,60,69,78,83],
    "G4": [16,25,34,43,52,61,70,79,84],
    "G5": [17,26,35,44,53,62,71,80,85],
}

fig = go.Figure()

# 1️⃣ Bridge geometry
for n1, n2 in members.values():
    x1, _, z1 = nodes[n1]
    x2, _, z2 = nodes[n2]
    fig.add_trace(go.Scatter3d(
        x=[x1, x2], y=[0, 0], z=[z1, z2],
        mode='lines',
        line=dict(color='black', width=2),
        showlegend=False
    ))

scale = 0.1

# 2️⃣ BMD (Red)
first = True
for g in girders.values():
    for e in g:
        n1, n2 = members[e]
        x1, _, z1 = nodes[n1]
        x2, _, z2 = nodes[n2]
        Mz_i = ds.forces.sel(Element=e, Component="Mz_i").values * scale
        Mz_j = ds.forces.sel(Element=e, Component="Mz_j").values * scale

        fig.add_trace(go.Scatter3d(
            x=[x1, x2], y=[Mz_i, Mz_j], z=[z1, z2],
            mode='lines',
            line=dict(color='red', width=6),
            name='BMD' if first else None,
            showlegend=first
        ))
        first = False

# 3️⃣ SFD (Blue)
first = True
for g in girders.values():
    for e in g:
        n1, n2 = members[e]
        x1, _, z1 = nodes[n1]
        x2, _, z2 = nodes[n2]
        Vy_i = ds.forces.sel(Element=e, Component="Vy_i").values * scale
        Vy_j = ds.forces.sel(Element=e, Component="Vy_j").values * scale

        fig.add_trace(go.Scatter3d(
            x=[x1, x2], y=[Vy_i, Vy_j], z=[z1, z2],
            mode='lines',
            line=dict(color='blue', width=6),
            name='SFD' if first else None,
            showlegend=first
        ))
        first = False

fig.update_layout(
    title="3D Shear Force & Bending Moment Diagrams",
    scene=dict(
        xaxis_title="X (Bridge Length)",
        yaxis_title="Force/Moment",
        zaxis_title="Z (Girder Width)"
    )
)

fig.show()
