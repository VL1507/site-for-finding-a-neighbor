import React from "react";
import { instance } from "../../../utils/axios";
import axios from "axios";

const fake_aouh = async () => {
    try {
        const url = "/fake_aouh";
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
    return (
        <>
            <h1>Это страница для авторизации</h1>
            <button onClick={fake_aouh}>Авторизоваться</button>
            <button onClick={get_info}>Узнать информацию</button>
        </>
    );
};

export default Login;
