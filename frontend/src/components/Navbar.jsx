//import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <nav className="bg-white shadow-md p-4 flex justify-between items-center">
            <nav className="bg-white shadow-md p-4 flex justify-between items-center">
                <div className="text-xl font-bold text-green-600">Shamrock Market</div>
                <input type="text" placeholder="Search products..." className="border p-2 rounded-md w-1/3" />
                <div>
                    <button className="text-gray-700 mr-4">Login</button>
                    <button className="bg-green-600 text-white px-4 py-2 rounded-md">Sign Up</button>
                </div>
            </nav>
        </nav>
    );
};

export default Navbar;
