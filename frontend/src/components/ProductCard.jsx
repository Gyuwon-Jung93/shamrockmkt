import React from 'react';
import PropTypes from 'prop-types';

function ProductCard({ product }) {
  return (
    <div>
      <img src={product.image_url} alt={product.title} />
      <h2>{product.title}</h2>
      <p>
        {product.price}
        {' '}
        €
      </p>
    </div>
  );
}

ProductCard.propTypes = {
  product: PropTypes.shape({
    title: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    image_url: PropTypes.string.isRequired,
  }), // ✅ `isRequired` 제거하여 `defaultProps`를 사용할 수 있도록 수정
};

ProductCard.defaultProps = {
  product: {
    // ✅ 이제 `defaultProps` 사용 가능
    title: 'Unknown Product',
    price: 0,
    image_url: 'https://via.placeholder.com/150',
  },
};

export default ProductCard;
