import polars as pl 
import time
import typing

def leer() -> pl.DataFrame:
    q= pl.scan_csv("../data/diabetes.csv")
    df= q.collect()
    return df

def guardar_modelo(df: pl.DataFrame) -> None:
    id= time.time()
    df.write_json(f"../results/modelo{id}")

def node_to_dict(node):
    if node is None:
        return None

    # Leaf node
    if node.childs is None and node.next is None:
        return {
            "type": "leaf",
            "value": node.value
        }

    # Branch node
    if node.childs is None and node.next is not None:
        return {
            "type": "branch",
            "value": node.value,
            "next": node_to_dict(node.next)
        }
    
    # Decision node (feature -> Children)
    return {
        "type": "decision",
        "feature": node.value,
        "children": [
            {
                "value": child.value,
                "next": node_to_dict(child.next)
            }
            for child in node.childs
        ]
    }

def dict_to_node(d: dict):
    if d["type"]== "leaf":
        n= Node()
        n.value= d["value"]
        return n 

    if d["type"]== "branch":
        n= Node()
        n.value= d["value"]
        n.next= dict_to_node(d["next"])
        return n 

    n= Node()
    n.value= d["feature"]
    n.childs= []
    for child in d["children"]:
        c= Node()
        c.value= child["value"]
        c.next= dict_to_node(child["next"])
        n.childs.append(c)
    
    return n