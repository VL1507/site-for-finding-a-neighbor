"use client";
import { useState } from "react";

import obshaga from "../public/data/place.json";
import Meta from "./meta";

export default function Home() {
  const [currentView, setCurrentView] = useState("initial");
  const [registerStep, setRegisterStep] = useState(1);
  const [loginData, setLoginData] = useState({
    email: "",
    password: "",
  });
  const [userData, setUserData] = useState({
    email: "",
    password: "",
    name: "",
    age: "",
    gender: "",
    day: "",
    month: "",
    year: "",
    selectObshaga: "",
  });
  const [date, setDate] = useState(null);

  const handleLoginClick = () => setCurrentView("login");
  const handleRegisterClick = () => setCurrentView("register");

  const handleGoBack = () => {
    if (currentView === "login") {
      setCurrentView("initial");
    } else if (currentView === "register") {
      if (registerStep > 1) {
        setRegisterStep(registerStep - 1);
      } else {
        setCurrentView("initial");
      }
    }
  };

  const handleLoginChange = (e) => {
    setLoginData({ ...loginData, [e.target.name]: e.target.value });
  };

  const handleRegisterChange = (e) => {
    setUserData({ ...userData, [e.target.name]: e.target.value });
  };

  const handleRegisterNext = () => {
    if (registerStep === 1) {
      setRegisterStep(2);
    } else if (registerStep === 2) {
      setRegisterStep(3);
    } else if (registerStep === 3) {
      setRegisterStep(4);
    } else if (registerStep === 4) {
      const day = parseInt(userData.day, 10);
      const month = parseInt(userData.month, 10) - 1;
      const year = parseInt(userData.year, 10);

      const newDate = new Date(year, month, day);

      if (isNaN(newDate)) {
        console.error("Invalid date entered!");
        alert("Введите корректную дату.");
        return;
      }

      setDate(newDate);
      setRegisterStep(5);
    } else if (registerStep === 5) {
      const selectObshaga = userData.selectObshaga;
      if (!selectObshaga) {
        alert("Выберите общежитие");
        return;
      }

      const queryString = new URLSearchParams({
        action: "registerSuccess",
        name: userData.name,
        email: userData.email,
        password: userData.password,
        gender: userData.gender,
        selectObshaga: selectObshaga,
        day: date.getDate(),
        month: date.getMonth() + 1,
        year: date.getFullYear(),
      });

      window.location.href = `/user?${queryString.toString()}`;
    }
  };

  const handleSubmit = (data, action) => {
    const queryString = new URLSearchParams({ action, ...data });
    window.location.href = `/user?${queryString.toString()}`;
  };

  /*Подсказка для Вас. На данный момент, как мы и обсуждали бэка тут нет, как и связи с ним. А чтобы работало без, сделал пока через ссылку. Все введенные данные можно получить на странице личного кабинета. Если будете делать бэк, от функции, очевидно, handleSubmit мы отказываемя и пишем код для запроса на сервер, по типу(лишь пример):
  
 import { redirect } from 'next/navigation';
 const handleRegisterNext = async () => {
    if (registerStep < 5) {
      // 
      setRegisterStep(registerStep + 1);
    } else {
      // 
      try {
        const response = await fetch('/api/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(userData),
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.message || 'Registration failed');
        }

      
        redirect('/login'); 
      } catch (error) {
        console.error('Registration error:', error);
        // Display error to the user
        alert('Registration failed: ' + error.message);
      }
    }
  };

  const handleLoginSubmit = async () => {
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(loginData),
      });

      if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.message || 'Login failed');
      }

      const data = await response.json();
      // Successful login; redirect to dashboard.
      redirect('/dashboard');
    } catch (error) {
      console.error('Login error:', error);
      alert('Login failed: ' + error.message);
    }
  };
  
  */

  const handleLoginSubmit = () => {
    handleSubmit(loginData, "loginSuccess");
  };

  return (
    <>
      <Meta title="Your neiborn - Главная"></Meta>
      <div className="mainPage">
        <div className="main__nav">
          <input className="main__search" type="text" placeholder="Поиск" />
          <p>
            Язык: <span>Русский</span>
          </p>
        </div>
        <div className="main__inner">
          <div className="main__block">
            {currentView === "initial" && (
              <>
                <h1>
                  <img src="/img/logo.png" alt="logo" />
                </h1>
                <h2 className="greetings">Твои новые соседи</h2>
                <button className="create" onClick={handleRegisterClick}>
                  Создать профиль
                </button>
                <button className="enter" onClick={handleLoginClick}>
                  Войти
                </button>
              </>
            )}

            {currentView === "login" && (
              <div className="main__wrap">
                <div className="container">
                  <button onClick={handleGoBack} className="back-button">
                    <img src="/img/назад.png" alt="back" />
                  </button>
                  <h2 className="login__enter">Войти</h2>
                  <input
                    className="enter__mail"
                    type="text"
                    name="email"
                    placeholder="Email"
                    onChange={handleLoginChange}
                  />
                  <input
                    className="enter__password"
                    type="password"
                    name="password"
                    placeholder="Пароль"
                    onChange={handleLoginChange}
                  />
                  <button
                    className="enter__enter"
                    onClick={handleLoginSubmit}
                    disabled={!loginData.password}
                  >
                    Войти
                  </button>
                  <div className="social">
                    <ul>
                      <li>
                        <a href="">
                          <img src="/img/tg.png" alt="tg" />
                        </a>
                      </li>
                      <li>
                        <a href="">
                          <img src="/img/vk.png" alt="vk" />
                        </a>
                      </li>
                      <li>
                        <a href="">
                          <img src="/img/google.png" alt="google" />
                        </a>
                      </li>
                      <li>
                        <a href="">
                          <img src="/img/yandex.png" alt="yandex" />
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            )}
            {currentView === "register" && (
              <div className="main__wrap">
                <div className="container">
                  <button onClick={handleGoBack} className="back-button">
                    <img src="/img/назад.png" alt="back" />
                  </button>
                  {registerStep === 1 && (
                    <>
                      <h2 className="login__enter">Регистрация</h2>
                      <input
                        className="enter__mail"
                        type="text"
                        name="email"
                        placeholder="Email"
                        onChange={handleRegisterChange}
                      />
                      <input
                        className="enter__password"
                        type="password"
                        name="password"
                        placeholder="Пароль"
                        onChange={handleRegisterChange}
                      />
                      <button
                        className={`enter__registr ${
                          !userData.password ? "disabled" : ""
                        }`}
                        onClick={handleRegisterNext}
                        disabled={!userData.password}
                      >
                        Создать профиль
                      </button>
                      <div className="social">
                        <ul>
                          <li>
                            <a href="">
                              <img src="/img/tg.png" alt="tg" />
                            </a>
                          </li>
                          <li>
                            <a href="">
                              <img src="/img/vk.png" alt="vk" />
                            </a>
                          </li>
                          <li>
                            <a href="">
                              <img src="/img/google.png" alt="google" />
                            </a>
                          </li>
                          <li>
                            <a href="">
                              <img src="/img/yandex.png" alt="yandex" />
                            </a>
                          </li>
                        </ul>
                      </div>
                    </>
                  )}

                  {registerStep === 2 && (
                    <>
                      <button onClick={handleGoBack} className="back-button">
                        <img src="/img/назад.png" alt="back" />
                      </button>
                      <h2 className="reg__title">Привет, давай знакомиться</h2>
                      <p className="reg__desc">
                        Расскажи о себе — это поможет создать профиль и сразу
                        начать общаться.
                      </p>
                      <button
                        onClick={() => {
                          setUserData({ ...userData, gender: "Мужской" });
                          handleRegisterNext();
                        }}
                      >
                        Я мужчина
                      </button>
                      <button
                        onClick={() => {
                          setUserData({ ...userData, gender: "Женский" });
                          handleRegisterNext();
                        }}
                      >
                        Я женщина
                      </button>
                    </>
                  )}
                  {registerStep === 3 && (
                    <>
                      <button onClick={handleGoBack} className="back-button">
                        <img src="/img/назад.png" alt="back" />
                      </button>
                      <h2 className="reg__title">Как тебя зовут?</h2>
                      <p className="reg__desc">
                        Будь собой в выборе имени — больше внимания получают
                        реальные профили.
                      </p>
                      <input
                        type="text"
                        name="name"
                        placeholder="Ваше имя"
                        onChange={handleRegisterChange}
                      />
                      <button
                        className={`next__btn ${
                          !userData.name ? "disabled" : ""
                        }`}
                        onClick={handleRegisterNext}
                        disabled={!userData.name}
                      >
                        <img src="/img/next.png" alt="next" />
                      </button>
                    </>
                  )}
                  {registerStep === 4 && (
                    <>
                      <button onClick={handleGoBack} className="back-button">
                        <img src="/img/назад.png" alt="" />
                      </button>
                      <h2 className="reg__title">
                        {userData.name}, выберите дату рождения
                      </h2>
                      <p className="reg__desc">
                        Используй настоящую, потом изменить её будет нельзя.
                      </p>
                      <div className="date__group">
                        <input
                          type="number"
                          name="day"
                          placeholder="01"
                          onChange={handleRegisterChange}
                          min="1"
                          max="31"
                          inputMode="numeric"
                          value={userData.day}
                          className="date"
                        />
                        <input
                          type="number"
                          name="month"
                          placeholder="01"
                          onChange={handleRegisterChange}
                          min="1"
                          max="12"
                          inputMode="numeric"
                          value={userData.month}
                          className="month"
                        />
                        <input
                          type="number"
                          name="year"
                          placeholder="2005"
                          onChange={handleRegisterChange}
                          inputMode="numeric"
                          value={userData.year}
                          className="year"
                        />
                      </div>

                      <button
                        className={`next__btn ${
                          !userData.day || !userData.month || !userData.year
                            ? "disabled"
                            : ""
                        }`}
                        onClick={handleRegisterNext}
                        disabled={
                          !userData.day || !userData.month || !userData.year
                        }
                      >
                        <img src="/img/next.png" alt="next" />
                      </button>
                    </>
                  )}
                  {registerStep === 5 && (
                    <>
                      <button onClick={handleGoBack} className="back-button">
                        <img src="/img/назад.png" alt="" />
                      </button>
                      <h2 className="reg__title">
                        {userData.name}, куда заселяемся
                      </h2>
                      <p className="reg__desc">
                        Покажем с тем же общежитием или гостиницей. Пошло не по
                        РАУ - измени в настройках.
                      </p>
                      <div className="select__wrap">
                        <select
                          className="main__select"
                          name="selectObshaga"
                          id="selectObshaga"
                          onChange={handleRegisterChange}
                        >
                          <option value="">Выберите место</option>
                          {obshaga.map((value) => {
                            return (
                              <option
                                className="regr__options"
                                key={value.id}
                                value={value.name}
                              >
                                {value.name}
                              </option>
                            );
                          })}
                        </select>
                        <div className="select__img">
                          <img src="/img/select-arrow.png" alt="arrow" />
                        </div>
                      </div>
                      <button
                        className="next__btn"
                        onClick={handleRegisterNext}
                      >
                        <img src="/img/next.png" alt="next" />
                      </button>
                    </>
                  )}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  );
}
