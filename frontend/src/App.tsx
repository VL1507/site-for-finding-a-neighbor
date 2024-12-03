import React from "react";
import "./App.css";
import { Route, Routes } from "react-router-dom";

import Home from "./components/home";
import Status from "./components/status";
import Login from "./components/auth/login";
import PrivateRoute from "./utils/router/privateRoute";
import Me from "./components/me";
import CreateProfile from "./components/create_profile";

function App() {
    return (
        <div className="App">
            <Routes>
                <Route element={<PrivateRoute />}>
                    <Route path="/status" element={<Status />} />
                </Route>

                <Route path="/" element={<Home />} />
                <Route path="/login" element={<Login />} />
                <Route path="/me" element={<Me />} />
                <Route path="/create_profile" element={<CreateProfile />} />
            </Routes>
        </div>
    );
}

export default App;
