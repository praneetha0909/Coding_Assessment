# Coding_Assessment

This project implements a python function to classify packages as "STANDARD", "SPECIAL", "REJECTED" based on their volume and mass.
## Objective

The program simulates an automation system in a robotics factory where packages are dispatched to different stacks based on the following rules:

### Rules

- A package is *bulky* if:
  - Its volume (width × height × length) is *≥ 1,000,000 cm³*, OR
  - Any one of its dimensions is *≥ 150 cm*.

- A package is *heavy* if:
  - Its mass is *≥ 20 kg*.

### Classification Logic

- REJECTED: If the package is both *bulky* and *heavy*.
- SPECIAL: If the package is *bulky* OR *heavy* (but not both).
- STANDARD: If the package is *neither bulky nor heavy*.

---
## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/praneetha0909/Coding_Assessment.git
   cd Coding_Assessment

Run the script: python Coding_Assessment.py
