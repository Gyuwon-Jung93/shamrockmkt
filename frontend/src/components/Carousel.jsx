import React from 'react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
// dd

function Carousel() {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
    pauseOnHover: true,
    fade: false,
  };

  const images = [
    {
      id: 'img1',
      src: 'https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    },
    {
      id: 'img2',
      src: 'https://images.unsplash.com/photo-1481437156560-3205f6a55735?q=80&w=1195&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    },
  ];

  return (
    <div className="carousel-container">
      <Slider {...settings}>
        {images.map((image) => (
          <div key={image.id} className="carousel-slide">
            <img src={image.src} alt={`Slide ${image.id}`} className="carousel-image" />
          </div>
        ))}
      </Slider>
    </div>
  );
}

export default Carousel;
