import React from "react";
import { instance } from "../../../utils/axios";
import axios from "axios";
import { useNavigate, NavigateFunction } from "react-router-dom";

const fake_aouh = async (navigate: NavigateFunction) => {
    console.log("fake_aouh");
    try {
        const url = "/fake_aouh";
        const response = await instance.get(url);

        console.log(response);

        // console.log(response.data.redirect);

        // if (response.data.redirect) {
        //     window.location.href = response.data.redirect;

        //     navigate(response.data.redirect);
        // }
    } catch (error) {
        if (axios.isAxiosError(error)) {
            // if (error.response?.data.redirect) {

            //     navigate(error.response.data.redirect);
            // }
            console.log(error, "err");
            console.log(error.response?.data.errText, "error");
        } else if (error instanceof Error) {
            console.log(error.message);
        }
    }
};

const get_info = async () => {
    try {
        const url = "/get_info";
        const response = await instance.get(url);
        console.log(response);
    } catch (error) {
        if (axios.isAxiosError(error)) {
            console.log(error, "err");
            console.log(error.response?.data.errText, "error");
        } else if (error instanceof Error) {
            console.log(error.message);
        }
    }
};

const Login = () => {
    const navigate = useNavigate();
    return (
        <>
            <h1>Это страница для авторизации</h1>
            <button
                onClick={() => {
                    fake_aouh(navigate);
                    // navigate("/status");
                }}
            >
                Авторизоваться
            </button>
            <button onClick={get_info}>Узнать информацию</button>
        </>
    );
};

export default Login;
