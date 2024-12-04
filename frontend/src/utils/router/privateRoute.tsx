import { Navigate, Outlet } from "react-router-dom";

const PrivateRoute = () => {
    const auth = true;
    console.log(auth);

    // const cookie = document.cookie;
    // console.log(cookie);

    return auth ? <Outlet /> : <Navigate to="login" />;
};

export default PrivateRoute;
