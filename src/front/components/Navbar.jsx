import { Link } from "react-router-dom";
import { useAuth } from '../hooks/useAuth';

export const Navbar = () => {
	const { isAuthenticated, logout } = useAuth();

	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
				</Link>
				<div className="ml-auto">
					<Link to="/demo">
						<button className="btn btn-primary">Check the Context in action</button>
					</Link>
				</div>
				{isAuthenticated() && (
                <button onClick={logout}>Cerrar Sesión</button>
            	)}
			</div>
		</nav>
	);
};