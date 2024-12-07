import React, { useEffect, useState } from "react";
import { instance } from "../../utils/axios";
import axios from "axios";

interface IPing {
    ping: number;
}
async function getPing(): Promise<IPing | null> {
    try {
        const url = "/ping";
        const ping: IPing = (await instance.get(url)).data;
        console.log(ping);
        return ping;
    } catch (error) {
        if (axios.isAxiosError(error)) {
            console.log(error, "err");
            console.log(error.response?.data.errText, "error");
        } else if (error instanceof Error) {
            console.log(error.message);
        }
        return null;
    }
}

const Ping = () => {
    const [ping, setPing] = useState<IPing | null>(null);

    useEffect(() => {
        getPing()
            .then((ping) => setPing(ping))
            .catch((err) => console.log(err));
    }, []);

    return (
        <>
            <p>Ping: {ping?.ping ? ping.ping : 0}</p>
        </>
    );
};

export default Ping;
