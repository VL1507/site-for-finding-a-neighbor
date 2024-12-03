import axios from "axios";

const backend_host = "127.0.0.1";
const backend_port = "8000";
const backend_api_path = "api/v1";

export const instance = axios.create({
    baseURL: `http://${backend_host}:${backend_port}/${backend_api_path}`,
    timeout: 1000,
    // headers: {

    // }
    withCredentials: true,
    // proxy: {
    //     host: "127.0.0.1",
    //     port: 8000,
    // },
});
