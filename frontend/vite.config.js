import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';
// https://vite.dev/config/
export default defineConfig({
    plugins: [react()],
    server: {
        fs: {
            allow: [
                path.resolve(
                    __dirname,
                    '/Users/jacob/Desktop/SelfStudy/ShamRockMarket/node_modules/slick-carousel/slick/fonts'
                ), // 📌 slick-carousel 폰트 허용
                path.resolve(__dirname, 'src'), // 📌 src 폴더를 Vite의 허용된 경로로 추가
                path.resolve(__dirname, 'node_modules'), // 📌 node_modules도 허용
            ],
        },
    },
});
