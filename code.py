# This script calculates the theoretical yield of a chemical reaction
# based on the SMILES codes, weights, and mole ratios of reactants.
# It uses the RDKit library for molecular weight calculations.

# To run this script, you must have RDKit installed.
# You can install it using pip:
# pip install rdkit

from rdkit import Chem
from rdkit.Chem.rdMolDescriptors import CalcExactMolWt

def calculate_theoretical_yield(reactants, product_smiles, mole_ratio_product):
    """
    Calculates the theoretical yield of a reaction.

    Args:
        reactants (dict): A dictionary where keys are reactant names and values are
                          dictionaries containing 'smiles', 'weight_g', and 'mole_ratio'.
                          Example: {'reactant_A': {'smiles': 'C1CC1', 'weight_g': 10.0, 'mole_ratio': 1}}
        product_smiles (str): The SMILES code for the product.
        mole_ratio_product (float): The mole ratio of the product in the balanced equation.

    Returns:
        A dictionary containing the theoretical yield in grams and the limiting reactant name,
        or an error message if the calculation fails.
    """
    moles_of_reactants = {}
    
    # Calculate molecular weight and moles for each reactant
    for name, data in reactants.items():
        smiles = data.get('smiles')
        weight_g = data.get('weight_g')
        
        if not smiles or not weight_g:
            return {"error": f"Invalid data for reactant '{name}'. Missing SMILES or weight."}
        
        try:
            mol = Chem.MolFromSmiles(smiles)
            if not mol:
                return {"error": f"Could not parse SMILES for reactant '{name}': {smiles}"}
            
            mol_weight = CalcExactMolWt(mol)
            moles = weight_g / mol_weight
            moles_of_reactants[name] = moles / data.get('mole_ratio', 1.0)
            
        except Exception as e:
            return {"error": f"An error occurred with reactant '{name}': {e}"}

    # Find the limiting reactant
    if not moles_of_reactants:
        return {"error": "No valid reactants provided."}
        
    limiting_reactant_name = min(moles_of_reactants, key=moles_of_reactants.get)
    moles_limiting = moles_of_reactants[limiting_reactant_name]
    
    # Calculate the theoretical moles of the product
    theoretical_moles_product = moles_limiting * mole_ratio_product
    
    # Calculate the molecular weight of the product
    try:
        product_mol = Chem.MolFromSmiles(product_smiles)
        if not product_mol:
            return {"error": f"Could not parse SMILES for product: {product_smiles}"}
        
        product_mol_weight = CalcExactMolWt(product_mol)
    except Exception as e:
        return {"error": f"An error occurred with the product SMILES: {e}"}
    
    # Calculate the theoretical yield in grams
    theoretical_yield_g = theoretical_moles_product * product_mol_weight
    
    return {
        "theoretical_yield_g": theoretical_yield_g,
        "limiting_reactant": limiting_reactant_name
    }

# --- Interactive User Interface ---
if __name__ == "__main__":
    print("--- Theoretical Yield Calculator ---")
    print("This tool calculates the theoretical yield of a reaction.")
    print("You will be asked to provide information for each reactant and the product.")
    
    reactants_data = {}
    
    try:
        num_reactants = int(input("\nEnter the number of reactants: "))
        if num_reactants <= 0:
            print("Please enter a positive number of reactants.")
        else:
            for i in range(num_reactants):
                name = input(f"\nEnter the name of reactant {i+1} (e.g., 'ethene'): ")
                smiles = input(f"Enter the SMILES code for {name}: ")
                weight_g = float(input(f"Enter the weight of {name} in grams: "))
                mole_ratio = float(input(f"Enter the mole ratio for {name}: "))
                reactants_data[name] = {
                    "smiles": smiles,
                    "weight_g": weight_g,
                    "mole_ratio": mole_ratio
                }
            
            product_smiles = input("\nEnter the SMILES code for the product: ")
            product_mole_ratio = float(input("Enter the mole ratio for the product: "))

            result = calculate_theoretical_yield(reactants_data, product_smiles, product_mole_ratio)

            if "error" in result:
                print(f"\nError: {result['error']}")
            else:
                print("\n--- Calculation Results ---")
                print(f"Limiting Reactant: {result['limiting_reactant']}")
                print(f"Theoretical Yield of Product: {result['theoretical_yield_g']:.2f} g")
    
    except ValueError:
        print("\nInvalid input. Please make sure to enter numbers for weight and mole ratios.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
