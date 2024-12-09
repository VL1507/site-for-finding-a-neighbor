"use client";
import { useSearchParams } from "next/navigation";
import "./user.css";
import place from "../../public/data/place.json";
import Header from "../components/Header";
import Link from "next/link";
import Meta from "../meta";

export default function UserPage() {
  const searchParams = useSearchParams();
  const action = searchParams.get("action");
  const name = searchParams.get("name");
  const day = searchParams.get("day");
  const month = searchParams.get("month");
  const year = searchParams.get("year");
  const gender = searchParams.get("gender");
  const obshaga = searchParams.get("selectObshaga");
  const email = searchParams.get("email");
  const password = searchParams.get("password");

  return (
    <>
      <Meta title="Your neiborn - Личный кабинет пользователя"></Meta>
      <div className="userPage">
        <div className="userPage__inner">
          <Header />

          <div className="userPhotoGallery">
            <div className="blockPhoto__left">
              <img src="/img/student.png" alt="student" />
            </div>
            <div className="blockPhoto__center">
              <img src="/img/student.png" alt="" />
              <img src="/img/student.png" alt="" />
            </div>
            <div className="blockPhoto__right">
              <img src="/img/student.png" alt="" />
              <img src="/img/student.png" alt="" />
            </div>
          </div>
          <div className="userInfo">
            <div className="userInfo__inner">
              <div className="userInfo__params">
                <div className="params__name">
                  <p>Имя:</p>
                  <p>{name}</p>
                </div>
                <div className="params__sex">
                  <img src="/img/User-info.png" alt="female" />
                  <p>Пол:</p>
                  <p>{gender}</p>
                </div>
                <div className="params__status">
                  <img src="/img/female.png" alt="female" />
                  <img src="/img/male.png" alt="male" />
                  <p>Статус:</p>
                  <input
                    type="radio"
                    id="status1"
                    name="status-option"
                    value="Студент"
                  />
                  <label htmlFor="status1">Студент</label>
                  <input
                    type="radio"
                    id="status2"
                    name="status-option"
                    value="Преподаватель"
                  />
                  <label htmlFor="status2">Преподаватель</label>
                </div>
                <div className="params__obshaga">
                  <img src="/img/Home1.png" alt="Home" />
                  <p>Общежитие:</p>
                  <div className="selectPage__wrap">
                    <select
                      name="selectObshaga"
                      id="selectObshaga"
                      className="user__select"
                    >
                      <option value="">Выберите место</option>
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
                <div className="params__smoking">
                  <img src="/img/Smoking.png" alt="Smoking" />
                  <p>Курение:</p>
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
                <div className="params__drink">
                  <img src="/img/Alcogol.png" alt="Alcogol" />
                  <p>Алкоголь:</p>
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
                <div className="dream">
                  <img src="/img/dream.png" alt="dream" />
                  <p>Сон:</p>
                  <div
                    title="Укажите, когда вы чаще всего ложитесь и встаёте. Если у вас нет какого-то определённого времени, можете оставить эти поля нетронутыми."
                    className="hint"
                  >
                    <img src="/img/hint.png" alt="hint" />
                  </div>
                  <div className="selectPage__wrap">
                    <select
                      name="selectTime"
                      id="selectTime"
                      className="user__select"
                    >
                      <option value="">Ложусь</option>
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
                      <option value="">Встаю</option>
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
                <div className="aboutMe">
                  <p>Информация:</p>
                  <div
                    title="Расскажите о своих личностных качествах: характере, увлечениях, чистоплотности и другом, что вы считаете важным для своего соседа."
                    className="hint"
                  >
                    <img src="/img/hint.png" alt="hint" />
                  </div>
                  <textarea
                    name="aboutMe"
                    id="aboutMe"
                    placeholder="О себе"
                  ></textarea>
                </div>
                <div className="userInfo__btn">
                  <Link href="/sidePage">
                    <button>Опубликовать анкету</button>
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
{
}
