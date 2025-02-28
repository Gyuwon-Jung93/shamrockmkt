import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

const Carousel = () => {
    const settings = {
        dots: true,
        infinite: true, // 무한 루프 활성화
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        pauseOnHover: true, // 마우스 오버 시 멈추도록 설정
        fade: false, // fade 효과가 적용되었을 경우 끄기
    };

    const images = [
        'https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'https://images.unsplash.com/photo-1481437156560-3205f6a55735?q=80&w=1195&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    ];

    return (
        <div className="carousel-container">
            <Slider {...settings}>
                {images.map((src, index) => (
                    <div key={index} className="carousel-slide">
                        <img src={src} alt={`Slide ${index}`} className="carousel-image" />
                    </div>
                ))}
            </Slider>
        </div>
    );
};

export default Carousel;
