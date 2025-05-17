from flask import Flask, jsonify, request
from data import products  # Ensure this contains your product list

app = Flask(__name__)

# Homepage Route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product API!"}), 200

# GET /products - Returns all products or filters by category
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category", "").lower()
    filtered_products = [p for p in products if p["category"].lower() == category] if category else products
    return jsonify(filtered_products), 200

# GET /products/<id> - Returns a specific product by ID or 404
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)