import React from "react";
import Link from "next/link";
import "./searchPage.css";
import "../components/header.css";
import place from "../../public/data/place.json";
import Meta from "../meta";
import usersSearch from "../../public/data/users.json";

const searchPage = () => {
  //  можно использовать компонент Header здесь, чтобы не дублировать код, но
  //   так как данные хранятся сейчас по ссылке, новая страница их не получает,
  //   поэтому пока дублируем
  return (
    <>
      <Meta title="Your neiborn - Поисковик"></Meta>

      <div className="searchPage">
        <div className="userNav">
          <div className="userNav__left">
            <div className="logo">
              <Link href="/">
                <img src="/img/logo.png" alt="лого" />
              </Link>
            </div>
            <div className="likes">
              <img src="/img/Heart.png" alt="сердце" />
              <p>Лайки</p>
            </div>
            <div className="userSearch">
              <img src="/img/Search.png" alt="поиск" />
              <input type="text" placeholder="Поиск" />
            </div>
          </div>
          <div className="userNav__right">
            <div className="profile">
              <p>Максим Гринин</p>
              <img src="/img/User.png" alt="пользователь" />
            </div>
          </div>
        </div>
        <div className="searchPage__inner">
          <div className="searchPage__filter">
            <div className="searchPage__place">
              <p>Общежитие:</p>
              <div className="selectPage__wrap">
                <select
                  name="selectObshaga"
                  id="selectObshaga"
                  className="user__select"
                >
                  <option value="">-</option>
                  {place.map((value) => {
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
                <div className="selectPage__img">
                  <img src="/img/select-arrow.png" alt="arrow" />
                </div>
              </div>
            </div>
            <div className="searchPage__smoking">
              <p>Курение:</p>
              <div className="searchPage__radioGroup">
                <input
                  type="radio"
                  id="smoking1"
                  name="smoking-option"
                  value="Не курю"
                />
                <label htmlFor="smoking1">Не курю</label>
                <input
                  type="radio"
                  id="smoking2"
                  name="smoking-option"
                  value="Курю"
                />
                <label htmlFor="smoking2">Курю</label>
                <input
                  type="radio"
                  id="smoking3"
                  name="smoking-option"
                  value="Парю"
                />
                <label htmlFor="smoking3">Парю</label>
              </div>
            </div>
            <div className="searchPage__drink">
              <p>Курение:</p>
              <div className="searchPage__radioGroup">
                <input
                  type="radio"
                  id="drink1"
                  name="drink-option"
                  value="Не пью"
                />
                <label htmlFor="drink1">Не пью</label>
                <input
                  type="radio"
                  id="drink2"
                  name="drink-option"
                  value="По праздникам"
                />
                <label htmlFor="drink2">По праздникам</label>
                <input
                  type="radio"
                  id="drink3"
                  name="drink-option"
                  value="Вне праздников"
                />
                <label htmlFor="drink3">Вне праздников</label>
              </div>
            </div>
            <div className="searchPage__dream">
              <p>Сон:</p>
              <div className="selectPage__wrap">
                <select
                  name="selectTime"
                  id="selectTime"
                  className="user__select"
                >
                  <option value="">-</option>
                  <option value="20:00">20:00</option>
                  <option value="21:00">21:00</option>
                  <option value="22:00">22:00</option>
                  <option value="23:00">23:00</option>
                  <option value="24:00">24:00</option>
                  <option value="00:00">00:00</option>
                  <option value="01:00">01:00</option>
                  <option value="02:00">02:00</option>
                  <option value="03:00">03:00</option>
                  <option value="04:00">04:00</option>
                </select>
                <div className="selectPage__img">
                  <img src="/img/select-arrow.png" alt="arrow" />
                </div>
              </div>
              <div className="selectPage__wrap">
                <select
                  name="selectGetUp"
                  id="selectGetUp"
                  className="user__select"
                >
                  <option value="">-</option>
                  <option value="20:00">05:00</option>
                  <option value="21:00">06:00</option>
                  <option value="22:00">07:00</option>
                  <option value="23:00">08:00</option>
                  <option value="24:00">09:00</option>
                  <option value="00:00">10:00</option>
                  <option value="01:00">11:00</option>
                </select>
                <div className="selectPage__img">
                  <img src="/img/select-arrow.png" alt="arrow" />
                </div>
              </div>
            </div>
            <div className="searchPage__wordKey">
              <p>Слова в описании:</p>
              <textarea name="" id="" placeholder="Игры"></textarea>
              <div className="searchPage__wordKey--group">
                <div className="word1">Слово 1</div>
                <div className="word2">Большое слово 2</div>
                <div className="word3">Большое слово 2</div>
                <div className="word4">Слово 1</div>
                <div className="word5">Большое слово 2</div>
                <div className="word6">Слово 1</div>
              </div>
            </div>
          </div>
          <div className="searchPage__users">
            <div className="searchPage__user">
              <ul>
                {usersSearch.map((value) => {
                  return (
                    <li key={value.id}>
                      <p className="searchUser__name">{value.name}</p>
                      <p className="searchUser__place">{value.place}</p>
                      <div className="searchUser__img">
                        <img src="/img/student.png" alt="student" />
                      </div>
                    </li>
                  );
                })}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default searchPage;
