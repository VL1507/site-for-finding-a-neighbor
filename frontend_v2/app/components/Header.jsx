import React from "react";
import "./header.css";
import Link from "next/link";
import { useSearchParams } from "next/navigation";

const Header = () => {
  const searchParams = useSearchParams();
  const name = searchParams.get("name");
  return (
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
        <Link href="/searchPage">
          <div className="userSearch">
            <img src="/img/Search.png" alt="поиск" />
            <input type="text" placeholder="Поиск" />
          </div>
        </Link>
      </div>
      <div className="userNav__right">
        <div className="profile">
          <p>{name}</p>
          <img src="/img/User.png" alt="пользователь" />
        </div>
      </div>
    </div>
  );
};

export default Header;
