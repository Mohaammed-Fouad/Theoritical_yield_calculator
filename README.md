# Theoretical Yield Calculator

This is a Python script that calculates the theoretical yield of a chemical reaction. It takes key information about your reactants and product as input and determines the maximum amount of product you can expect to form.

The code is designed to be interactive, prompting the user for all the necessary data in the terminal.

## Features

- **Molecular Weight Calculation:** Uses the **RDKit** library to accurately calculate the molecular weight of compounds from their SMILES codes.
- **Limiting Reactant Identification:** Automatically identifies the limiting reactant from the provided data.
- **Yield Calculation:** Computes the theoretical yield of the product in grams.

## How to Use

1.  **Install RDKit:** You need the RDKit library to run this script. If you don't have it, you can install it using `pip`:
    ```bash
    pip install rdkit
    ```
2.  **Run the script:** Navigate to the directory containing the file and run it from your terminal:
    ```bash
    python code.py
    ```
3.  **Follow the prompts:** The script will ask you for the following information for each reactant and the product:
    -   Name (e.g., 'ethene')
    -   SMILES code (e.g., 'C=C')
    -   Weight in grams
    -   Mole ratio from the balanced chemical equation

## Acknowledgment

This Python script was generated with the assistance of **Gemini**, a large language model.
