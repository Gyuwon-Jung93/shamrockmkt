import { useEffect, useState } from 'react';
const Footer = () => {
    return (
        <footer className="bg-gray-800 text-white p-10 mt-10">
            <div className="grid grid-cols-3 gap-4">
                <div>
                    <h3 className="font-bold">회사</h3>
                    <p>Shamrock Market 소개</p>
                    <p>블로그</p>
                </div>
                <div>
                    <h3 className="font-bold">서비스</h3>
                    <p>중고거래</p>
                    <p>동네업체</p>
                </div>
                <div>
                    <h3 className="font-bold">소셜미디어</h3>
                    <p>Facebook</p>
                    <p>Instagram</p>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
