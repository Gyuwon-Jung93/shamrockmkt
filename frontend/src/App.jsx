import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import ProductDetail from './pages/ProductDetail';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Carousel from './components/Carousel';
function App() {
    return (
        <Router>
            <div className="flex flex-col min-h-screen">
                <Navbar />
                <Carousel />
                <div className="flex-grow">
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/product/:id" element={<ProductDetail />} />
                    </Routes>
                </div>

                {/* 하단 푸터 */}
                <Footer />
            </div>
        </Router>
    );
}

export default App;
