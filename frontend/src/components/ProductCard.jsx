import PropTypes from 'prop-types';

const ProductCard = ({ product }) => {
    return (
        <div>
            <img src={product.image_url} alt={product.title} />
            <h2>{product.title}</h2>
            <p>{product.price} €</p>
        </div>
    );
};

ProductCard.propTypes = {
    product: PropTypes.shape({
        image_url: PropTypes.string.isRequired,
        title: PropTypes.string.isRequired,
        price: PropTypes.number.isRequired,
    }).isRequired,
};

export default ProductCard;
