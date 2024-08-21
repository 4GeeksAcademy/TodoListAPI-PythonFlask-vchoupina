from flask import Flask, jsonify, request

app = Flask(__name__)

# Variable global todos
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 200

# Endpoint para eliminar una tarea específica
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    
    # Verificar si la posición es válida
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400
    
    # Eliminar la tarea en la posición especificada
    deleted_todo = todos.pop(position)
    print("Deleted todo:", deleted_todo)
    
    # Retornar la lista actualizada de todos en formato JSON
    return jsonify(todos), 200

if __name__ == '__main__':
    app.run(debug=True)
