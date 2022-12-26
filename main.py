from flask import Flask,jsonify,request

app = Flask("DMO_BE")


GRAPH_ROUTES=[
    "ARTICULATIONS",
    "HUNGARIAN"
]

def graph(type):
     
    if type=="ARTICULATIONS":
        return {"result":"arts"}
    elif type=="HUNGARIAN":
        return {"result":"hung"}

@app.route("/graph",methods=["POST"])
def root():
    content_type=request.content_type
    if content_type.lower() !="application/json":
        return "Invalid request Content-Type Header.",500
    body=request.get_json()
    if "graph_id" not in body:
        return "No graph_id supplied in request body.",500
    if "graph_id" in body and body["graph_id"] not in GRAPH_ROUTES:
        return f"Invalid graph_id: {body['graph_id']} supplied to request body.",400
    print(body["graph_id"],content_type)
    return jsonify(graph(body["graph_id"])),200

