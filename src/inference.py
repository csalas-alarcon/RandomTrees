import itertools
import pandas as pd
from sklearn.metrics import mean_squared_error, root_mean_squared_error
from dataWork import dict_to_node

class engine():
    SIZE= 100000

    def __init__(self, data: pd.DataFrame, pnode: Node):
        self.data= data 
        self.pnode= pnode 

    def traverse(data: pd.Series, tree: Node) -> float:
        # Leaf node
        if tree.childs is None and tree.next is None:
            return tree.value

        # Decision Node
        col= tree.value 
        value= data[col]
        for child in node.childs: # Branch Node
            if child.value== value:
                traverse(data, child.next) # Next decision node

    def get_results(portion: float) -> Union(list[float], int):
        # Check its valid
        if portion <= 0 or portion > 1:
            return 0

        results= []
        number= trunc(SIZE* portion)
        for _, row in self.data[:number].iterrows():
            res= traverse(row, self.pnode)
            results.append(res)
        
        return (results, number)

    def validation(results: list[float], length) -> Union(float, float, int):
        labels= self.data["diabetes_risk_score"].tolist()
        mse= mean_squared_error(labels, results)
        rmse= root_mean_squared_error(labels, results)

        return (mse, rmse, length)

def main():
    with open("decision_tree.json") as f:
        tree_dict= json.load(f)

    pnode= dict_to_node(tree_dict)



    
