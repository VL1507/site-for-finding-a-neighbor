"use client";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import "../user/user.css";
import "../components/header.css";
import Meta from "../meta";

export default function SidePage() {
  const searchParams = useSearchParams();
  const action = searchParams.get("action");
  const name = searchParams.get("name");
  const age = searchParams.get("age");
  const gender = searchParams.get("gender");
  const obshaga = searchParams.get("selectObshaga");

  return (
    <>
      <Meta title="Your neiborn - Чужой личный кабинет"></Meta>
      <div className="sidePage">
        <div className="userPage__inner">
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
                  <p>Максим Гринин</p>
                </div>
                <div className="params__sex">
                  <img src="/img/User-info.png" alt="female" />
                  <p>Пол:</p>
                  <p>Мужской</p>
                </div>
                <div className="params__status">
                  <img src="/img/female.png" alt="female" />
                  <img src="/img/male.png" alt="male" />
                  <p>Статус:</p>
                  <p>Студент</p>
                </div>
                <div className="params__obshaga">
                  <img src="/img/Home1.png" alt="Home" />
                  <p>Общежитие:</p>
                  <p>Гостиница 6.2</p>
                </div>
                <div className="params__smoking">
                  <img src="/img/Smoking.png" alt="Smoking" />
                  <p>Курение:</p>
                  <p>Не курю</p>
                </div>
                <div className="params__drink">
                  <img src="/img/Alcogol.png" alt="Alcogol" />
                  <p>Алкоголь:</p>
                  <p>Не пью</p>
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
                  <p>23:00</p>
                  <p>-</p>
                  <p>7:00</p>
                </div>
                <div className="aboutMe">
                  <p>Информация:</p>
                  <p>
                    Люблю играть в волейбол, творческая личность, учусь на
                    прикладной информатике, немного интроверт, чистоплотный, на
                    выходных уезжай к родителям
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
