// src/components/Navbar.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import Navbar from './Navbar';

test('renders Navbar component', () => {
    render(<Navbar />);
    const element = screen.getByText(/Shamrock Market/i);
    expect(element).toBeInTheDocument();
});
