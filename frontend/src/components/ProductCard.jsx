import React from "react";
import { Link } from "react-router-dom";

const ProductCard = ({ product }) => {
  return (
    <div className="border rounded-lg shadow-md p-4">
      <img
        src={product.image_url}
        alt={product.title}
        className="w-full h-40 object-cover rounded"
      />
      <h2 className="text-lg font-semibold mt-2">{product.title}</h2>
      <p className="text-gray-500">{product.price} €</p>
      <Link
        to={`/product/${product.id}`}
        className="text-green-600 hover:underline"
      >
        View Details
      </Link>
    </div>
  );
};

export default ProductCard;
