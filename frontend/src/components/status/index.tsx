import React, { useEffect, useState } from "react";
import { instance } from "../../utils/axios";
import axios from "axios";

interface IUser {
    id: number;
    is_admin: boolean;
}
async function getUser(): Promise<IUser | null> {
    try {
        const url = "/get_user";
        const user: IUser = (await instance.get(url)).data;
        console.log(user);
        return user;
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
const Status = () => {
    const [user, setUser] = useState<IUser | null>(null);

    useEffect(() => {
        getUser()
            .then((user) => setUser(user))
            .catch((err) => console.log(err));
    }, []);

    return (
        <div>
            <p>
                Пользователь: {user?.id} {user?.is_admin}
            </p>
            <button id="logout_btn">Выйти</button>
        </div>
    );
};

export default Status;
