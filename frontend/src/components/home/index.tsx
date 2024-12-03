import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
    return (
        <div>
            <h1>Сервис для поиска соседей</h1>
            <a href="https://t.me/test_oauth_232453423_bot">
                Войти через телеграм
            </a>
            <Link to="/me">Аккаунт</Link>
        </div>
    );
};

export default Home;
