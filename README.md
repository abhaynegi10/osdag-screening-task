# 🏗️ Osdag Screening Task – Structural Post-Processing

This project demonstrates structural result visualization using **Xarray** and **Plotly**.  
The objective was to generate Shear Force and Bending Moment diagrams from finite element analysis output.

---

## 📁 Project Structure

data/  
└── screening_task (1).nc   # Structural analysis dataset  

node.py                      # Node coordinates  
element.py                   # Element connectivity  

task1_sfd_bmd.py             # 2D SFD & BMD (Central Girder)  
task2_3d_sfd_bmd.py          # 3D SFD & BMD (All Girders)  

BMD.png                      # Bending Moment Diagram  
SFD.png                      # Shear Force Diagram  

---

## 📊 Task-1: SFD & BMD (Central Longitudinal Girder)

- Xarray was used to read the NetCDF dataset.  
- Internal forces (`Mz_i`, `Mz_j`, `Vy_i`, `Vy_j`) were extracted.  
- Central girder elements were selected.  
- Continuous Shear Force Diagram (SFD) and Bending Moment Diagram (BMD) were generated using Plotly.

**Output:**  
SFD.png  
BMD.png  

---

## 🌉 Task-2: 3D Shear Force & Bending Moment Diagrams

- Node coordinates and element connectivity were used to reconstruct the bridge geometry.  
- Force values were mapped to each element.  
- Shear and moment diagrams were extruded vertically to produce a 3D visualization similar to professional structural post-processing tools.

**Output:**  
3D force visualization of all girders  

---

## 🛠️ Technologies Used

- Python 3.11  
- Xarray  
- Plotly  
- NumPy  

---

## ▶️ How to Run

pip install xarray plotly numpy  
python task1_sfd_bmd.py  
python task2_3d_sfd_bmd.py  

---

## ✅ Objective Achieved

✔ Extraction of structural internal forces  
✔ Generation of 2D SFD & BMD  
✔ Reconstruction of 3D structural geometry  
✔ Professional post-processing visualization  

---

This project replicates real-world structural engineering post-processing workflows.
